"""
Christina Wang	7/18/22	CSCI-UA 2 - 002
Assignment #3 Problem #2
"""

import math

#input
num=int(input("Please enter a positive number greater than 1: "))
#ensure input is positive integer>1
while True:
    if num <2:
        print("Invalid entry. Try again.")
        num=int(input("Please enter a positive number greater than 1: "))
        continue
    if num>=1:
        break

#list to contain all numbers in factorial
numbers=[1]

#calculations
#uses for loop to illustrate list
#uses math.factorial to get factorials
for i in range(2, num+1):
    if i < num:
        numbers.append(i)
        print(num, "! -> ", end="")
        print(*numbers, sep=" X ", end="")
        print(" =", "{:,}".format(math.factorial(i)))
        i +=1
        continue
    if i == num:
        numbers.append(num)
        print(num, "! -> ", end="")
        print(*numbers, sep=" X ", end="")
        print(" =", "{:,}".format(math.factorial(num)))
        break
