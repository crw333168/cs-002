"""
Christina Wang 7/14/22	CSCI-UA 2 - 002
Assignment #1 Problem #3
"""
#user inputs numbers
first_numberString  = input("Enter a number between 0 and 999: ")
second_numberString = input("Enter another number between 0 and 999: ")

#converting to integers
first_number  =int(first_numberString)
second_number =int(second_numberString)

#isolating ones, tens, hundreds
first_number_ones      = first_number%10
second_number_ones     =second_number%10
first_number_tens      =(first_number%100)//10
second_number_tens     =(second_number%100)//10
first_number_hundreds  =first_number//100
second_number_hundreds =second_number//100

#sums
sum_of_ones     = first_number_ones+second_number_ones
sum_of_tens     = first_number_tens+second_number_tens
sum_of_hundreds = first_number_hundreds+second_number_hundreds

#printing
print (format("Sum of ones", "<15s"), "=", first_number_ones, "+", second_number_ones, "=", sum_of_ones, sep=" ")
print (format("Sum of tens", "<15s"), "=", first_number_tens, "+", second_number_tens, "=", sum_of_tens, sep=" ")
print (format("Sum of hundreds", "<15s"), "=", first_number_hundreds, "+", second_number_hundreds, "=", sum_of_hundreds, sep=" ")
