# Information Retrieval Assignment 1

## Dataset

The dataset for this assignment is available in directory 'CSE508_Winter2024_A1_Dataset'
Additionally, a directory named `preprocessed_files` is created to store the preprocessed files.

## Data Preprocessing

The data preprocessing steps are as follows:

1. **Import Required Libraries:**
   - Imported `word_tokenize` and `stopwords` functions from the `nltk` module for data preprocessing.
   - Downloaded punctuation and stopwords resources from `nltk`.

2. **Setting Up Paths:**
   - Created a variable `additional_path` to store path values (`/content/` for Google Colab or other necessary path values).
   
3. **Reading and Processing Files:**
   - Loop through file indices from 1 to 999, formatting the string for the path name.
   - Read files from the formatted string path name.
   - Convert all text to lowercase.
   - Tokenize the text using the `word_tokenize` function.
   - Remove English stopwords.
   - Remove punctuations.
   - Remove blank space tokens.

4. **Saving Preprocessed Files:**
   - Write the preprocessed text back into the `preprocessed_files` directory with the same name as the original file.
   - Merge all tokens into a single sentence using space as a delimiter.
   - Close all file pointers.

## Sample Output

To verify preprocessing, 5 random files are selected and their contents before and after preprocessing are displayed.

## Creating a Unigram Inverted Index

1. **Initialize Data Structures:**
   - Created an empty dictionary `inverted_index` to store the inverted index. The dictionary keys are tokens and values are posting lists containing file names.
   
2. **Building the Inverted Index:**
   - Read preprocessed files one by one.
   - Tokenize the text using split with space as the delimiter.
   - Maintain a list `total_docs` to store the document names.
   - For each token, add the document ID (file name) to the postings list. If the token is new, create a new entry in the dictionary.

## Storing and Loading Inverted Index

- Utilized the `pickle` module to store the inverted index using `pickle.dump()` and load it using `pickle.load()`.

## Query Operations for Inverted Index

1. **Implemented Boolean Query Functions:**
   - Created functions for AND, OR, AND NOT, and OR NOT operations using set logic.
   - Used `total_docs` to find differences for the NOT operator.
   
2. **Handling Input:**
   - Created lists `operatorsInp` and `tokensInp` to store input values.
   - Input the number of queries (`n`).
   - Preprocess operators by converting to lowercase and splitting by “,” delimiter.
   - Preprocess query text similarly to the data preprocessing step, storing operators in `operatorsInp` and tokens in `tokensInp`.
   
3. **Performing Queries:**
   - For each query, construct the boolean query format in the variable `query`.
   - Handle missing tokens by creating a token with an empty set if it is not present in the inverted index.
   - Perform operations according to the provided operators.
   - Assumption: Number of tokens should be equal to the number of operators + 1.

4. **Output:**
   - Print the number of documents and names of the documents retrieved.

## Query Results

### Query 1: `live AND music`
- Number of documents retrieved: 1
- Names of the documents retrieved: `file22.txt`

### Query 2: `works AND NOT nicely`
- Number of documents retrieved: 95
- Names of the documents retrieved:
  - `file333.txt`
  - `file192.txt`
  - ...

## Creating Positional Index

1. **Initialize Data Structures:**
   - Created a positional index dictionary, `positional_index`, where the key is a token and the value is another dictionary. This inner dictionary stores the document ID as the key and a set of positions of the token as the value.
   - Used 1-based indexing for token positions in the documents.
   
2. **Building the Positional Index:**
   - Read preprocessed files one by one and tokenize the text.
   - If the token is not in `positional_index`, add it with an empty dictionary. Then, add the document ID with an empty set, and add the token position to this set.
   - If the token is already present but the document ID is not, add the document ID with an empty set and then add the token position to this set.

## Storing and Loading Positional Index

- Utilized the `pickle` module to store the positional index using `pickle.dump()` and load it using `pickle.load()`.

## Query Operations for Positional Index

1. **Handling Input:**
   - Initialized an empty `tokensInp` list to store the input tokens for all queries.
   - Input the number of queries (`n`) and then input `n` lines of queries.
   - Preprocess the query text similarly to the data preprocessing step and store them in the `tokensInp` list.
   
2. **Processing Queries:**
   - For each query, store all tokens in the variable `tokens`.
   - For each document containing the first token, perform a nested search for the position of the token.
   - Call a recursive function to search for the next token at adjacent positions.
   
3. **Recursive Function for Query Processing:**
   - Base Case: If the index equals the size of tokens, the current document contains all tokens in adjacent positions. Store the document name in the `docs` list.
   - If the token is not in `positional_index`, exit the function.
   - If the current document contains the next token at an adjacent position, call the function recursively with the next token index, token list, current word position + 1, and the current document.
   - Else, do nothing.

4. **Output:**
   - Print the number of documents and names of the documents retrieved.

## Query Results

### Query 1: `live music`
- Number of documents retrieved: 1
- Names of the documents retrieved: `file22.txt`

### Query 2: `works nicely`
- Number of documents retrieved: 2
- Names of the documents retrieved: `file32.txt`, `file472.txt`
