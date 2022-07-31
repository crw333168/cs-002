"""
Christina Wang	7/24/22	CSCI-UA 2 - 002
Assignment #4 Problem #1 Challenge #2
"""

#function: maximum
#input: x, y
#processing: compares two values
#output: returns the maximum of the two values

def maximum(a,b):
    if a>b:
        return a
    elif a<b:
        return b
    
#function: minimum
#input: x, y
#processing: compares two values
#output: returns the minimum of the two values

def minimum(a,b):
    if a>b:
        return b
    elif a<b:
        return a
a = 5
b = 10
c = 15
d = 20

ans1 = maximum(a,b)
ans2 = maximum(a,c)
ans3 = maximum(a,d)
print (ans1,ans2,ans3) # 10 15 20

ans4 = minimum(d,c)
ans5 = minimum(d,b)
ans6 = minimum(d,a)
print (ans4,ans5,ans6) # 15 10 5

ans7 = maximum( maximum(a,b), maximum(c,d) )
print ("The biggest is:", ans7)
