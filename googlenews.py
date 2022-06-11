from gensim import models
from math import *
import random

wv = models.KeyedVectors.load_word2vec_format(
    './GoogleNews-vectors-negative300.bin', binary=True)
#loads the vector model trained by the Google News dataset

num = 1
guesses = []

def printguesses(array):
    print('%-8r %8r %16.2r %24r' % ("#", "Guess", "Similarity", "Ranking"))
    for g in guesses:
        r = wv.rank(word,g)
        bar = ""
        numbars = (1000 - r) // 100
        for x in range(numbars):
            bar += '|'
        while (len(bar) < 10):
            bar += '-'
        #sets progression bar up
        print('%-8d %8r %16.2f %24d %r' % (num, g, wv.similarity(word, g), wv.rank(word,g), bar))

    
words = []
file = open("1-1000.txt", 'r')
for x in range(995):
    w = file.readline()
    f = w.replace("\n","")
    words.append(f)
#print(words)

#randomly select from top 1000 common english words
word = words[random.randint(0,994)]


while(True):
    guess = input("Guess a word: ") #takes input
    if guess == 'new game':
        word = words[random.randint(0,994)]
        print("New word selected.")
        num = 1
        continue
    if guess == 'give up':
        print("You lose. The word was " + word + " D: ")
        continue
    if guess == 'custom word':
        word = input("")
        num = 1
        continue
    try: #checks if input is a valid word
        wv[guess]
    except:
        print("Invalid word. Try again")
        continue
    
    print('%-8r %8r %16r %24r' % ("#", "Guess", "Similarity", "Ranking")) #prints display
    if (guess == word):
        r = 0
    else:
        r = wv.rank(word,guess)
    bar = ""
    numbars = (1001 - r) // 100
    for x in range(numbars):
        bar += '|'
    while (len(bar) < 10):
        bar += '-'
        #sets progression bar up
    print('%-8d %8r %16.2f %24d %r' % (num, guess, wv.similarity(word, guess), r, bar))
    guesses.append(guess)
    num += 1
    if guess == word:
        print("YOU WON! You can continue inputting words or start a new game with 'new game'")
    #printguesses(guesses)
    

#important functions
# .most_similar
# .n_similarity
# .rank
# use
