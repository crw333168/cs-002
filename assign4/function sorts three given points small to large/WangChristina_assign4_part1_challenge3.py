"""
Christina Wang	7/24/22	CSCI-UA 2 - 002
Assignment #4 Problem #1 Challenge #3
"""

# next, write a new function called 'simple_sort_version' that accepts three values.  you can assume
# that your three values will always be the same data type (all ints, all floats or all strings).
# sort these values in ascending order and return them. 
# you may use any function that you've written so far in this assignment if you'd like to (maximum, minimum, etc)

def maximum(a,b,c):
    if a>=b and a>=c:
        return a
    elif a<=b and c<=b:
        return b
    elif a<=c and b<=c:
        return c

def minimum(a,b,c):
    if a<=b and a<=c:
        return a
    elif a>=b and c>=b:
        return b
    elif a>=c and b>=c:
        return c
def middle(a,b,c):
    if a>=b and a<=c or a<=b and a>=c:
        return a
    elif a<=b and c>=b or a>=b and c<=b:
        return b
    elif a<=c and b>=c or a>=c and b<=c:
        return c
    
def simple_sort_version(a,b,c):
    ans1 = minimum(a,b,c)
    ans2 = middle(a,b,c)
    ans3 = maximum(a,b,c)
    return ans1, ans2, ans3
    

# your function should work perfectly with the following lines of code
a,b,c = simple_sort_version(10,20,30)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version(10,30,20)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version(30,20,10)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version(30,20,20)
print (a,b,c) # 20 20 30
