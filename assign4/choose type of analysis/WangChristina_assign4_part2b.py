"""
Christina Wang	7/30/22	CSCI-UA 2 - 002
Assignment #4 Problem #2b
"""

import analyzer

print("Main Menu")
print(" ")
print("1 - Find all prime numbers within a given range")
print("2 - Find all perfect numbers within a given range")
print("3 - Find all abundant numbers within a given range")
print("4 - Chart all even, odd, prime, perfect and abundant numbers within a given range")
print("5 - Quit")
print(" ")
print(" ")
choice= int(input("Your choice: "))
while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
    print("I don't understand that ...")

if choice == 1:
    startnum=int(input("Enter starting number (positive only): "))
    while startnum <=0:
        print("Invalid, try again")
        startnum=int(input("Enter starting number (positive only): "))
    endnum=int(input("Enter ending number: "))
    while endnum < startnum:
        print("Invalid, try again")
        endnum=int(input("Enter ending number: "))    

    print(" ")
    print("All prime numbers between ", startnum, "and ", endnum)
    print("##############")
    for i in range(startnum, endnum):
        if analyzer.is_prime(i) == True:
            print(i)
    print("##############")


if choice == 2:
    startnum=int(input("Enter starting number (positive only): "))
    while startnum <=0:
        print("Invalid, try again")
        startnum=int(input("Enter starting number (positive only): "))
    endnum=int(input("Enter ending number: "))
    while endnum < startnum:
        print("Invalid, try again")
        endnum=int(input("Enter ending number: "))    

    print(" ")
    print("All perfect numbers between ", startnum, "and ", endnum)
    print("##############")
    for i in range(startnum, endnum):
        if analyzer.is_perfect(i) == True:
            print(i)
    print("##############")

if choice == 3:
    startnum=int(input("Enter starting number (positive only): "))
    while startnum <=0:
        print("Invalid, try again")
        startnum=int(input("Enter starting number (positive only): "))
    endnum=int(input("Enter ending number: "))
    while endnum < startnum:
        print("Invalid, try again")
        endnum=int(input("Enter ending number: "))    

    print(" ")
    print("All abundant numbers between ", startnum, "and ", endnum)
    print("##############")
    for i in range(startnum, endnum):
        if analyzer.is_abundant(i) == True:
            print(i)
    print("##############")

if choice == 4:
    startnum=int(input("Enter starting number (positive only): "))
    while startnum <=0:
        print("Invalid, try again")
        startnum=int(input("Enter starting number (positive only): "))
    endnum=int(input("Enter ending number: "))
    while endnum < startnum:
        print("Invalid, try again")
        endnum=int(input("Enter ending number: "))    

    print(format("Number", '<10s'), end="")
    print(format("Even", '<10s'), end="")
    print(format("Odd", '<10s'), end="")
    print(format("Prime", '<10s'), end="")
    print(format("Perfect", '<10s'), end="")
    print(format("Abundant", '<10s'))
    for i in range(startnum, endnum+1):
        print(i, end="")
        print(format(" ", '<10s'), end="")
        if analyzer.is_even(i)==True:
            print(format("x", '<10s'), end="")
        elif analyzer.is_even(i)==False:
            print(format(" ", '<10s'), end="")
        if analyzer.is_odd(i)==True:
            print(format("x", '<10s'), end="")
        elif analyzer.is_odd(i)==False:
            print(format(" ", '<10s'), end="")
        if analyzer.is_prime(i)==True:
            print(format("x", '<10s'), end="")
        elif analyzer.is_prime(i)==False:
            print(format(" ", '<10s'), end="")
        if analyzer.is_perfect(i)==True:
            print(format("x", '<10s'), end="")
        elif analyzer.is_perfect(i)==False:
            print(format(" ", '<10s'), end="")
        if analyzer.is_abundant(i)==True:
            print(format("x", '<10s'))
        elif analyzer.is_abundant(i)==False:
            print(format(" ", '<10s'), end="")
        print()

if choice == 5:
    print(" ")
    print("Goodbye!")
