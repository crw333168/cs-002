"""
Christina Wang	8/4/22	CSCI-UA 2 - 002
Assignment #6 Problem #1b
"""
##picking the word

import random

#open file for reading
words = open('words.txt', 'r')

#read all data as one long string
alldata=words.read()

#cut apart string based on \n"
splitdata= alldata.split("\n")

print("The Wordle is ", end="")

#pick a random word from list
num=random.randint(0, len(splitdata))
wordle=str.upper((splitdata[num]))
print(wordle)

#close file
words.close()

##format

print ("           WORDLE            ")
print("------------------------------")


##bad guess
guess=input("Guess the word: ")
while True:
    if len(guess) !=5:
        print("You must enter a 5 letter word")
        guess=input("Guess the word: ")
        continue
    elif guess.isalpha() != True:
        print("You must enter a 5 letter word")
        guess=input("Guess the word: ")
        continue
    elif guess not in splitdata:
        print("Invalid word")
        guess=input("Guess the word: ")
        continue

##good guess
    else:
        break

#check guess
count = 0
for letter in guess:
    if letter == str.lower(wordle[count]):
        print(str.upper(letter), "*", sep="", end=" ")
        count += 1
    elif letter.lower() in wordle.lower(): 
        print(str.upper(letter), "?", sep="", end=" ")
        count += 1
    else:
        print (str.upper(letter), end= " ")
        count += 1
