"""
Christina Wang	7/18/22	CSCI-UA 2 - 002
Assignment #3 Problem #3a
"""
#3a

#input
num=int(input("Enter a positive number to test: "))

count=1

#testing numbers
print()
while count !=num:
    count +=1
    if num%count !=0:
        print(count, " is NOT a divisor of ", num, " ... continuing")
        continue
    if count == num:
        break
    if num%count ==0:
        print(count, " is a divisor of ", num, " ... stopping")
        print()
        print(num, "is not a prime number.")
        break

#prime reveal
if count == num:
    print()
    print(num, "is a prime number!")
