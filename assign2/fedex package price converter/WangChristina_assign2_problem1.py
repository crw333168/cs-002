"""
Christina Wang	7/14/22	CSCI-UA 2 - 002
Assignment #1 Problem #1
"""
#Introduction
print("Thank you for chosing FedEx! We look forward to delivering your package.")
pkge_weightString=input("What is the weight of your package? ")
ship_speed=input("Select your shipping speed: (s)tandard or (e)xpress ")
print()

#calculating
print("Calculating....")
print()

#math
#calculates weight rate based on package weight
pkge_weight=float(pkge_weightString)
if pkge_weight <= 2:
    weight_rate = 1.5
if pkge_weight >2 and pkge_weight <= 6:
    weight_rate = 3
if pkge_weight >6 and pkge_weight <= 10:
    weight_rate = 4
if pkge_weight > 10:
    weight_rate = 4.75
#calculates ship rate based on shipping speed
if ship_speed == "e":
    ship_rate = 10
elif pkge_weight < 30:
        ship_rate = 5
else: ship_rate = 0
#calculates weight charge, shipping charge, and total cost
weight_chrge= pkge_weight*weight_rate
ship_chrge= ship_rate
total_cost=weight_chrge+ship_rate

#formats the numbers to have two decimals
weight_chrge2dec = format(weight_chrge, '.2f')
ship_chrge2dec = format(ship_chrge, '.2f')
total_cost2dec= format(total_cost, '.2f')

#tells the user the pricing
print ("Weight Charge: ", pkge_weightString, " lb(s) x $", weight_rate, " = $",  weight_chrge2dec)
print("Shipping Charge: $", ship_chrge2dec)
print("Total Cost: $", total_cost2dec)
