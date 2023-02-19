"""
Christina Wang 7/14/22	CSCI-UA 2 - 002
Assignment #1 Problem #2
"""

#Assignment 2 Problem 2
# Fix and explain the errors in this program

#display title
#print("Temperature Converter")
#print("----------------------')
#syntax error- delimiters do not match
print("Temperature Converter")
print("----------------------")

# ask for temperature in farenheight
fTempString = input("Enter a temperature in Fahrenheit: ")
print("Calculating....\n")

# calculate celsius, kelvin, and rankine
#celsius = (fTemp-32)*(5/9) 
#kelvin = fTemp + 273.15 
#rankine = ftemp + 459.67 
#syntax error: trying to put a string into a math operation without converting
#syntax error: inconsistent variable names with rankine, capitalizse T in ftemp
#logic error: improperly calculating Kelvin
fTemp= float(fTempString)
celsius = (fTemp-32)*(5/9) 
kelvin = celsius + 273.15 
rankine = fTemp + 459.67

#display results
#print(format("Celsius:", '<8s'), format(celsius, '>10.2s'), "C")
#print(format("Kelvin:",'<8s'), format(rankine, '>10.2f'), "K")
#print(format("Rankine:", '<8s'), format(kelvin, '>10.2f'), "R" 
#syntax error- first line formats floating point value with 's' instead of 'f'
#syntax error- final line was not closed with )
#logic error- switched rankine and kelvin's results
print(format("Celsius:", '<8s'), format(celsius, '>10.2f'), "C")
print(format("Kelvin:",'<8s'), format(kelvin, '>10.2f'), "K")
print(format("Rankine:", '<8s'), format(rankine, '>10.2f'), "R")
