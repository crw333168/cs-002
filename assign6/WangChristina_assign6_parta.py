"""
Christina Wang	8/4/22	CSCI-UA 2 - 002
Assignment #6 Problem #1a
"""
import random

#open file for reading
words = open('words.txt', 'r')

#read all data as one long string
alldata=words.read()

#cut apart string based on \n"
splitdata= alldata.split("\n")

print("Opening file...")
print("12962 words extracted.")
print("The Wordle is ", end="")

#pick a random word from list
num=random.randint(0, len(splitdata))
print(str.upper((splitdata[num])))

#close file
words.close()
