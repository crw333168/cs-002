"""
Christina Wang	7/18/22	CSCI-UA 2 - 002
Assignment #3 Problem #3b
"""

#variable
count=1

#start with 1
print("1 is technically not a prime number.")

#evaluate the rest of the numbers
for i in range (1001):
    while count !=i:
        count +=1
        if i%count !=0:
            #prime potential
            continue
        if count == i:
            print(i, " is a prime number!")
            i +=1
            count =1
            break
        if i%count ==0:
            #not prime
            i +=1
            count =1
            break
