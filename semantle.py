import nltk
import warnings
import gensim
import glob
import os
from nltk.tokenize import sent_tokenize, word_tokenize
from gensim.models import Word2Vec
warnings.filterwarnings(action = 'ignore')



while (True):
    #list all the .txt files in the directory
    my_files = glob.glob('*.txt')
    print("\nText files available for analysis: ")
    for files in my_files:
        print("\t- " + files)

    #takes user input the file
    text = input("Choose a text file: ")
    if not(text in my_files):
        print("Invalid input.\n")
        continue

    #Read given file
    sample = open("./"  + text, 'r')
    s = sample.read()
     

    # Replaces escape character with space
    f = s.replace("\n", " ")
     
    data = []
     
    # iterate through each sentence in the file
    for i in sent_tokenize(f):
        temp = []
         
        # tokenize the sentence into words
        for j in word_tokenize(i):
            temp.append(j.lower())
     
        data.append(temp)
     
    # Create CBOW model
    
    model1 = gensim.models.Word2Vec(data, min_count = 1,
                                  vector_size = 100, window = 5)

    # Create Skip Gram model
    model2 = gensim.models.Word2Vec(data, min_count = 1, vector_size = 100,
                                                 window = 5, sg = 1)
    word1 = input("Give a word: ")
    word2 = input("Another: ")
    print("\n CBOW model:") #words around a word used to predict the word
    print("\nWord vector of " + word1)
    print(model1.wv[word1])
    print("\nWord vector of " + word2)
    print(model1.wv[word2])
    print("\nCosine similarity between " + word1 + " and " + word2)
    print(model1.wv.similarity(word1,word2))

    print("\n Skip Gram model:") #word tries to predict words before and after
    print("\nWord vector of " + word1)
    print(model2.wv[word1])
    print("\nWord vector of " + word2)
    print(model2.wv[word2])
    print("\nCosine similarity between " + word1 + " and " + word2)
    print(model2.wv.similarity(word1,word2))
    
    # Print results
    #print("Cosine similarity between 'alice' " +
                 #  "and 'wonderland' - CBOW : ",
        #model1.wv.similarity('alice', 'wonderland'))
         
# alice wonderland
# ship kill
