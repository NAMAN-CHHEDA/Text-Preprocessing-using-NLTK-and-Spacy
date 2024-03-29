# -*- coding: utf-8 -*-
"""TEXT_PROCESSING_USING_NLTK_AND_SPACY.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jeI4n95baDuvhvmuCmSBDeUhtz9uEZka
"""

import numpy as np
import pandas as pd
import string as st
import re
import nltk
from nltk import PorterStemmer, WordNetLemmatizer
import nltk.corpus
import os
nltk.download('all')

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

"""CORPUS"""

import nltk
from nltk.corpus import gutenberg
nltk.download('gutenberg')

hamlet=nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')

w=[]
for words in hamlet[:100]:
  w.append(words)
arr = np.array(w)

arr1=np.array2string(arr)
print(arr1)

"""DATASET"""

df=pd.read_csv('/content/twitter_training.csv')
temp = df.iloc[:, -1].tolist()

dataset_w=[]
for item in temp[:20]:
  if (isinstance(item,float)):
    dataset_w.append(str(item))
  else:
    dataset_w.append(item)

dataset_text = " ".join(dataset_w)
print(dataset_text)

"""WORD AND SENTENCE TOKENIZATION"""

#PLAINTEXT
str1=" My name is Naman Chheda. I am 20 years old. I am studying in DJ Sanghvi"
print(word_tokenize(str1))
print(sent_tokenize(str1))
print()

#CORPUS
print(word_tokenize(arr1))
print(sent_tokenize(arr1))
print()

#DATASET
print(word_tokenize(dataset_text))
print(sent_tokenize(dataset_text))
print()

"""REMOVING STOPWORDS"""

def remove_stopwords(text):
  stop_words = set(stopwords.words("english"))
  word_tokens = word_tokenize(text)
  filtered_text = [word for word in word_tokens if word not in stop_words]
  return filtered_text

#PLAINTEXT
print(remove_stopwords(str1))
print()

#CORPUS
print(remove_stopwords(arr1))
print()

#DATASET
print(remove_stopwords(dataset_text))

"""CONVERTING TO LOWERCASE"""

def text_lowercase(str1):
  return str1.lower()

#PLAINTEXT
print(text_lowercase(str1))
print()

#CORPUS
print(text_lowercase(arr1))
print()

#DATASET
print(text_lowercase(dataset_text))
print()

"""REMOVING NUMBERS"""

def remove_numbers(text):
  result = re.sub(r'\d+', '', text)
  return result

#PLAINTEXT
print(remove_numbers(str1))
print()

#CORPUS
print(remove_numbers(arr1))
print()

#DATASET
print(remove_numbers(dataset_text))
print()

"""REMOVING PUNCTUATION"""

import string
def remove_punctuation(text):
  translator = str.maketrans('', '', string.punctuation)
  return text.translate(translator)

#PLAINTEXT
print(remove_punctuation(str1))
print()

#CORPUS
print(remove_punctuation(arr1))
print()

#DATASET
print(remove_punctuation(dataset_text))
print()

"""REMOVING WHITESPACES"""

def remove_whitespace(text):
  return " ".join(text.split())

#PLAINTEXT
print(remove_whitespace(str1))
print()

#CORPUS
print(remove_whitespace(arr1))
print()

#DATASET
print(remove_whitespace(dataset_text))
print()

"""COUNT WORD FREQUENCY"""

from nltk.probability import FreqDist

def word_frequency(text):
  frequency_dist = FreqDist(text)
  for word, freq in frequency_dist.items():
    print(f"{word} -> {freq}")

#PLAINTEXT
str2=word_tokenize(str1)
print(word_frequency(str2))
print()

#CORPUS
arr2=word_tokenize(arr1)
print(word_frequency(arr2))
print()

#DATASET
dataset_text1=word_tokenize(dataset_text)
print(word_frequency(dataset_text1))
print()

"""PORTER STEMMER"""

#PLAINTEXT
ps = PorterStemmer()
words = word_tokenize(str1)
for w in words:
    print(w, " : ", ps.stem(w))

#CORPUS

corpus_stemmed_words=[ps.stem(word) for word in arr2]
text_after_stemming = ' '.join(corpus_stemmed_words)
print(text_after_stemming)
print()

#DATASET
dataset_stemmed_words=[ps.stem(word) for word in dataset_text1]
print(text_after_stemming)
text_after_stemming = ' '.join(dataset_stemmed_words)
print()

"""LANCESTER STEMMER"""

from nltk.stem import LancasterStemmer

ls = LancasterStemmer()

#Plaintext:
stemmed_words=[ls.stem(word) for word in str2]
text_after_stemming = ' '.join(stemmed_words)
print(text_after_stemming)
print()

#CORPUS
corpus_stemmed_words=[ls.stem(word) for word in arr2]
text_after_stemming = ' '.join(corpus_stemmed_words)
print(text_after_stemming)
print()

#DATASET
dataset_stemmed_words=[ls.stem(word) for word in dataset_text1]
text_after_stemming = ' '.join(dataset_stemmed_words)
print(text_after_stemming)
print()

"""LEMMITIZATION"""

lemmatizer = WordNetLemmatizer()
def lemmatize_word(text):
  word_tokens = word_tokenize(text)

  lemmas = [lemmatizer.lemmatize(word, pos ='v') for word in word_tokens]
  return lemmas

#PLAINTEXT
print(lemmatize_word(str1) )
text2="Programmers program with programming languages"
print(lemmatize_word(text2))
print()

#CORPUS
print(lemmatize_word(arr1))
print()

#DATASET
print(lemmatize_word(dataset_text))
print()

"""SPACY LIBRARY

"""

from spacy.lang.en import English
import spacy
import numpy as np

nlp= spacy.load('en_core_web_sm')

x=" My name is Naman Chheda. I am 20 years old. I am studying in DJ Sanghvi"

doc=nlp(x)

"""WORD TOKENIZATION"""

tokens=[tokens.text for tokens in doc ]
print(tokens)

"""SENTENCE TOKENIZATION"""

py_doc = nlp(x)
for sent in py_doc.sents:
    print(sent.text)

"""REMOVING STOPWORDS"""

stopwords_tokens =[token.text for token in doc if not token.is_stop]
print(stopwords_tokens)

"""LEMMITIZATION"""

y="Walking, walked, walks are all forms of walking"
doc2=nlp(y)

" ".join([token.lemma_ for token in doc2])

"""CORPUS"""

import nltk
from nltk.corpus import gutenberg
nltk.download('gutenberg')

hamlet=nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')

w=[]
for words in hamlet[:100]:
  w.append(words)
corpus_text = " ".join(w)
corpus1=nlp(corpus_text)
print(corpus1)

"""CORPUS WORD TOKENIZATION"""

corpus_tokens=[tokens for tokens in corpus1]
print(corpus_tokens)

"""CORPUS SENTENCE TOKENIZATION"""

for sent in corpus1.sents:
    print(sent.text)

"""CORPUS REMOVING STOPWORDS"""

stopwords_tokens =[token.text for token in corpus1 if not token.is_stop]
print(stopwords_tokens)

"""CORPUS LEMMITIZATION"""

" ".join([token.lemma_ for token in corpus1])