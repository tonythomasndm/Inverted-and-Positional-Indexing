# git clone https://github.com/tonythomasndm/CSE508_Winter2024_A1_Dataset.git
# mkdir preprocessed_files


import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

#Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

additional_path=""
# for google collab use -/content/
#Looping through the dataset
for i in range(1,1000):
  num= "% s" % i
  read_path=additional_path+'CSE508_Winter2024_A1_Dataset/text_files/file' + num + '.txt'
  file_read=open(read_path,'r')
  text=file_read.read()

  # Lower the text
  text = text.lower()

  # Tokenize the text
  tokens = word_tokenize(text)

  # Remove stopwords
  stop_words = set(stopwords.words('english'))
  tokens = [token for token in tokens if token not in stop_words]

  # Remove punctuations
  tokens = [token for token in tokens if token not in string.punctuation]

  # Remove blank space tokens
  tokens = [token for token in tokens if token.strip()]

  sentence=""
  for token in tokens:
    sentence=sentence+token+' '

  #Saving the Preprocessed Files
  file_write=open(additional_path+'preprocessed_files/file'+ num +'.txt','w')
  file_write.write(sentence)
  file_read.close()
  file_write.close()

#Printing Sample 5 random documents before and after preprocessing
import random

# Generate 5 random numbers between 1 and 999
random_numbers = random.sample(range(1, 1000), 5)

for i in random_numbers:
  num= "% s" % i
  read_path=additional_path+'CSE508_Winter2024_A1_Dataset/text_files/file' + num + '.txt'
  file_read=open(read_path,'r')
  text=file_read.read()
  print("\nDoc "+num+" before preprocessing")
  print(text)
  file_read.close()
  file_read=open(additional_path+'preprocessed_files/file'+ num +'.txt','r')
  text=file_read.read()
  print("\nDoc "+num+" after preprocessing")
  print(text)
  file_read.close()
  print("-"*170)

#Creating unigram inverted index
inverted_index={}
total_docs=set()
for i in range(1,1000):
  num= "% s" % i
  file_read=open(additional_path+'preprocessed_files/file'+ num +'.txt','r')
  text=file_read.read()
  tokens=text.split()
  doc_id="file"+num+".txt"
  total_docs.add(doc_id)
  for token in tokens:
    if token not in inverted_index:
        inverted_index[token] = set()
    inverted_index[token].add(doc_id)

#Storing the Inverted Index
import pickle
f=open(additional_path+"inverted_index.txt","wb")
pickle.dump(inverted_index,f)

#Loading the inverted Index
f=open(additional_path+"inverted_index.txt",'rb')
inverted_index = pickle.load(f)

def andOp(docs1,docs2):
    return docs1.intersection(docs2)

def orOp(docs1,docs2):
    return docs1.union(docs2)

def andNotOp(docs1,docs2,total_docs):
    not_docs2 = total_docs.difference(docs2)
    return docs1.intersection(docs2)

def orNotOp(docs1,docs2,total_docs):
    not_docs2 = total_docs.difference(docs2)
    return docs1.union(not_docs2)

def queryTextPreProcess(text):
  # Lower the text
  text = text.lower()

  # Tokenize the text
  tokens = word_tokenize(text)

  # Remove stopwords
  stop_words = set(stopwords.words('english'))
  tokens = [token for token in tokens if token not in stop_words]

  # Remove punctuations
  tokens = [token for token in tokens if token not in string.punctuation]

  # Remove blank space tokens
  tokens = [token for token in tokens if token.strip()]

  return tokens

tokensInp=[]
operatorsInp=[]

print("\nInverted Index Queries ---")
#Taking Queries
n=int(input())
for i in range(0,n):
  queryText=input()
  operators=input().lower().split(",")
  operatorsInp.append(operators)
  tokens=queryTextPreProcess(queryText)
  tokensInp.append(tokens)

#Processing Queries
for i in range(0,n):

  print("\nQuery",(i+1),":", end=" ")
  operators=operatorsInp[i]
  tokens=tokensInp[i]
  query=tokens[0]
  op_count=0
  docs=inverted_index[tokens[0]]
  q=len(tokens)

  for iQ in range(1,q):
      op=operators[op_count].strip()
      query=query+' '+op.upper()
      term=tokens[iQ].strip()
      op_count+=1
      if term not in inverted_index:
          inverted_index[term]=set()
      if op == 'and':
        docs=andOp(docs,inverted_index[term])
      elif op =='or':
        docs=orOp(docs,inverted_index[term])
      elif op =='and not':
        docs=andNotOp(docs,inverted_index[term],total_docs)
      elif op=='or not':
        docs=orNotOp(docs,inverted_index[term],total_docs)
      query=query+' '+term
  print(query)
  print("Number of documents retrieved :", len(docs))
  if len(docs):
    print("Names of the documents retrieved : ",end="")
    for i in docs:
      print(i,end=", ")
  else:
    print("Names of the documents retrieved: None")

#Creating positional index
positional_index={}
total_docs=set()
for i in range(1,1000):
  num= "% s" % i
  file_read=open(additional_path+'preprocessed_files/file'+ num +'.txt','r')
  wordPosition=1
  text=file_read.read()
  tokens=text.split()
  doc_id="file"+num+".txt"
  total_docs.add(doc_id)
  for token in tokens:
    if token not in positional_index:
        positional_index[token] ={}
        positional_index[token]={doc_id:set()}
    elif doc_id not in positional_index[token]:
        positional_index[token][doc_id] = set()
    positional_index[token][doc_id].add(wordPosition)
    wordPosition+=1

#Storing the Positional Index
import pickle
f=open(additional_path+"positional_index.txt","wb")
pickle.dump(positional_index,f)

#Loading the positional Index
f=open(additional_path+"positional_index.txt",'rb')
inverted_index = pickle.load(f)

def queryTextPreProcess(text):
  # Lower the text
  text = text.lower()

  # Tokenize the text
  tokens = word_tokenize(text)

  # Remove stopwords
  stop_words = set(stopwords.words('english'))
  tokens = [token for token in tokens if token not in stop_words]

  # Remove punctuations
  tokens = [token for token in tokens if token not in string.punctuation]

  # Remove blank space tokens
  tokens = [token for token in tokens if token.strip()]

  return tokens

tokensInp=[]
operatorsInp=[]
print('\nPositional Index ---')
#Taking Queries
n=int(input())
for i in range(0,n):
  queryText=input()
  tokens=queryTextPreProcess(queryText)
  tokensInp.append(tokens)

#Recursive Function
docs=[]
def fn(index,tokens,currentWordPos,currentDoc):
  if(index==len(tokens)):
    docs.append(currentDoc)
    return
  else:
    if tokens[index] not in positional_index.keys():
      return
    if currentDoc in positional_index[tokens[index]]:
      if currentWordPos+1 in positional_index[tokens[index]][currentDoc]:
        fn(index+1,tokens,currentWordPos+1,currentDoc)
    else:
      return

#Processing Queries
for i in range(0,n):
  tokens=tokensInp[i]
  wordPosition=0
  currentDoc=""
  for doc in positional_index[tokens[0]]:
    for position in positional_index[tokens[0]][doc]:
      fn(1,tokens,position,doc)

  print("\nNumber of documents retrieved :", len(docs))
  if len(docs):
    print("Names of the documents retrieved : ",end="")
    for i in docs:
      print(i,end=", ")
  else:
    print("Names of the documents retrieved: None")
  docs=[]