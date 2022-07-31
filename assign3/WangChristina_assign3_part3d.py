"""
Christina Wang	7/18/22	CSCI-UA 2 - 002
Assignment #3 Problem #3d
"""

#input
startnum=int(input("Start number: "))
endnum=int(input("End number: "))

#variables
count=1
numbers=[]

#get primes
for i in range(startnum, endnum):
    while count !=i:
        count +=1
        if i%count !=0:
            #prime potential
            continue
        if count == i:
            numbers.append(i)
            i +=1
            count =1
            break
        if i%count ==0:
            #not prime
            i +=1
            count =1
            break

#format

print(*numbers)
