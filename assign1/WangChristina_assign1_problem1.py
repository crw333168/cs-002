"""
Christina Wang 7/14/22	CSCI-UA 2 - 002
Assignment #1 Problem #1
"""

#test comment
#this portion is for inputting the names
first_name = input("Please enter name #1: ")
second_name = input("Please enter name #2: ")
third_name = input("Please enter name #3: ")
print( )

#this portion introduces the names in every order
print ("Here are your names in every possible order:")
print ("--------------------------------------------")
print( )

#this portion lists the names
#1, Names are displayed in the order First Name, Second Name, Third Name
print ("1", end=". ")
print (first_name, second_name, third_name, sep=" <> ")
print( )
#2, Names are displayed in the order First Name, Third Name, Second Name
print ("2", end=". ")
print (first_name, third_name, second_name, sep=" <> ")
print( )
#3, Names are displayed in the order Second Name, First Name, Third Name
print ("3", end=". ")
print (second_name, first_name, third_name, sep=" and ", end="!")
print( )
print( )
#4, Names are displayed in the order Second Name, Third Name, First Name
print ("4", end=". ")
print (second_name, third_name, first_name, sep=" and ", end="!")
print( )
print( )
#5 Names are displayed in the order Third Name, Second Name, First Name
print ("5", end=". ")
print (third_name)
print (second_name)
print (first_name)
print( )
#6 Names are displayed in the order Third Name, First Name, Second Name
print ("6", end=". ")
print (third_name)
print (first_name)
print (second_name)
