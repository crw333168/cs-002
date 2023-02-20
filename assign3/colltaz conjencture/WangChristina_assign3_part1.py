"""
Christina Wang	7/18/22	CSCI-UA 2 - 002
Assignment #3 Problem #1
"""

#input
num=int(input("Enter a positive number: "))
while True:
    if num <1:
        print("Invalid entry. Try again")
        num=int(input("Enter a positive number: "))
        continue
    if num>=1:
        break
       
#calculating
print()
print("Calculating....")
print()

#define variables
count=0
evcount=0
oddcount=0
increase=0
numbers=[num]

#calculations

while num != 1:
    count +=1
    if num % 2 == 0:
        evcount +=1
        if len(numbers) == 1:
            print(count, ". ", num, " -> Even!")
        elif numbers[-1] > numbers[-2]:
            increase +=1
            print(count, ". ", num, " -> Even! Increased!")
        else:
            print(count, ". ", num, " -> Even!")
        num=int(num/2)
        numbers.append(num)
        continue
    else:
        oddcount +=1
        print(count, ". ", num, " -> Odd!")
        num=int(3*num+1)
        numbers.append(num)
        continue

if num == 1:
    count +=1
    oddcount +=1
    print(count, ". 1 -> Odd!")
    
#summary
avg= sum(numbers)/len(numbers)
print()
print("It took a total of ", count-1, " steps to reach the Collatz conjencture.")
print("Along the way, there were ", evcount, "even numbers.")
print("Along the way, there were ", oddcount, "odd numbers.")
print("Along the way, there were ", increase, "increases.")
print("The average number in the sequence is ", format(avg, '.2f'))
