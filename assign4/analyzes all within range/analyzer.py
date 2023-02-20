"""
Christina Wang	7/30/22	CSCI-UA 2 - 002
Assignment #4 Problem #2 Analyzer
"""
# function:   is_even 
# input:      a positive integer 
# processing: determines if the supplied number is even 
# output:     boolean

def is_even(x):
    if x%2 == 0:
        return True
    else:
        return False

# function:   is_odd
# input:      a positive integer
# processing: determines if the supplied number is odd
# output:     boolean

def is_odd(x):
    if x%2 != 0:
        return True
    else:
        return False

# function:   is_prime
# input:      a positive integer
# processing: determines if the supplied number is prime. a prime number is
#             a number that only has two factors - the number 1 and itself.
#             for example, 17 is prime because it only has two factors (1 and 17).
#             in order to determine this you might need to count the # of factors
#             between 1 and the number you are testing. a note on efficiency: if you are
#             testing a number (say, 15) and you find a factor (say, 3) - do you need to even continue
#             to find additional factors?
# output:     boolean

def is_prime(x):
    for i in range(2,x):
        if (x%i) == 0:
            return False
    return True

# function:   is_perfect
# input:      a positive integer
# processing: determines if the supplied number is perfect. a perfect number
#             is a number that is equal to the sum of its factors (i.e. the
#             number 6 is perfect because 6 = 1 + 2 + 3)
# output:     boolean

def is_perfect(x):
    sum1 = 0
    for i in range (1,x):
        if(x%i == 0):
            sum1 = sum1 + i
    if (sum1 == x):
        return True
    else:
        return False

# function:   is_abundant
# input:      a positive integer
# processing: determines if the supplied number is abundant. an abundant number
#             is a number that is less than the sum of its factors (i.e. the
#             number 12 is abundant because 12 < 1 + 2 + 3 + 4 + 6)
# output:     boolean

def is_abundant(x):
    sum1 = 0
    for i in range (1,x):
        if(x%i == 0):
            sum1 = sum1 + i
    if (sum1 > x):
        return True
    else:
        return False
