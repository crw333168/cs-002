"""
Christina Wang	7/14/22	CSCI-UA 2 - 002
Assignment #1 Problem #2
"""
import random

#get a random number between 1 and 10

num = random.randint(1,10)

#asks the user the question
print("I'm thinking of a number between 1 and 10!")
guessString1=input("What's your guess? ")

#uses the first guess to assess if the user got the number
guess1= int(guessString1)

if guess1 == num:
    print ("You got it!")
    print ("The secret number was ", num, ".")
    print ("It took you 1 try to guess the number.")
elif guess1 > num:
    print ("Too high, try again.")
    guessString2=input("What's your guess? ")
elif guess3 < num:
    print ("Too low try again.")
    guessString2=input("What's your guess? ")

#uses the second guess to assess if the user got the number
guess2= int(guessString2)

if guess2 == num:
    print ("You got it!")
    print ("The secret number was ", num, ".")
    print ("It took you 2 tries to guess the number.")
elif guess2 > num:
    print ("Too high, try again.")
    guessString3=input("What's your guess? ")
elif guess3 < num:
    print ("Too low try again.")
    guessString3=input("What's your guess? ")

#uses the third guess to assess if the user got the number
guess3= int(guessString3)

if guess3 == num:
    print ("You got it!")
    print ("The secret number was ", num, ".")
    print ("It took you 3 tries to guess the number.")
elif guess3 > num:
    print ("The secret number was ", num, ".")
    print ("You didn't guess the number.")
elif guess3 < num:
    print ("The secret number was ", num, ".")
    print ("You didn't guess the number.")


