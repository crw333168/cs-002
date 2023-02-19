"""
Christina Wang	8/5/22	CSCI-UA 2 - 002
Assignment #6 Problem #1c
"""
##picking the word

import random

#open file for reading
words = open('words.txt', 'r')

#read all data as one long string
alldata=words.read()

#cut apart string based on \n"
splitdata= alldata.split("\n")

#pick a random word from list
num=random.randint(0, len(splitdata))
wordle=str.upper((splitdata[num]))

#close file
words.close()

##format

print (format("WORDLE", '^28s'))
print("------------------------------")

##run it 6 times
printguess=[]
for i in range(6):
    guess=input("Guess the word: ")
##bad guess
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

##printing list
    while len(printguess) > 1:
        print(*printguess[:-1], sep="")
        break
        
##check guess
    count = 0
    for letter in str.lower(guess):
        if letter == str.lower(wordle[count]):
            printguess.append(str.upper(letter))
            printguess.append("* ")
            print(str.upper(letter), "*", sep="", end=" ")
            count += 1
        elif letter.lower() in wordle.lower():
            printguess.append(str.upper(letter))
            printguess.append("? ")
            print(str.upper(letter), "?", sep="", end=" ")
            count += 1
        else:
            printguess.append(str.upper(letter))
            printguess.append("  ")
            print (str.upper(letter), end= "  ")
            count += 1
    printguess.append("\n")
    print()
    print()
##correct+how many tries
    if str.upper(guess) == wordle:
        print("Correct: The Wordle is ", str.upper(guess))
        print("You guessed the Wordle in ", i+1, " tries.")
        break
##incorrect
print("Sorry, you did not guess the Wordle. The Wordle is ", wordle)
    
