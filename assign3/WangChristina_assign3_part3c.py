"""
Christina Wang	7/18/22	CSCI-UA 2 - 002
Assignment #3 Problem #3c
"""

#input
startnum=int(input("Start number: "))
endnum=int(input("End number: "))
while startnum <0 or endnum <0:
    print("Start and end must be positive")
    print()
    startnum=int(input("Start number: "))
    endnum=int(input("End number: "))
while startnum > endnum and startnum>0 and endnum>0:
    print ("End number must be greater than start number")
    print()
    startnum=int(input("Start number: "))
    endnum=int(input("End number: "))

#variable
count= 1

print()
for i in range (startnum, endnum+1):
    while count !=i:
        count +=1
        if i%count !=0:
            #prime potential
            continue
        if count == i:
            print(i)
            i +=1
            count =1
            break
        if i%count ==0:
            #not prime
            i +=1
            count =1
            break

