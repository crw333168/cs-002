"""
Christina Wang	8/17/22	CSCI-UA 2 - 006
Assignment #8 Problem #2
"""

import random

class Gumball_Machine:
    def __init__(self, capacity):
        print("Gumball Machine created with ", int(capacity), " random gumballs")
        self.money = float(format(0, ".2f"))
        self.lst=[]
        colorlist=["red", "green", "blue"]
        for i in range(int(capacity)):
            colorpick= random.choice(colorlist)
            self.lst.append(colorpick)

    def report(self):
        print("Gumball Machine Report:")
        print("  * Gumballs in machine: ", len(self.lst))
        print("  * Money in machine: $", float(format(self.money, '.2f')))

    def dispense(self, coin):
        if coin != float(.25):
            print("Invalid coin, no gumball will be dispensed")
        elif len(self.lst)==0:
            print("Machine is empty, no gumball will be dispensed")
        else:
            gum=random.choice(self.lst)
            print("Accepting ", coin, "; Dispensing a ", gum ," gumball")
            self.lst.remove(gum)
            self.money += float(format(coin, ".2f"))

    def count_gumballs_by_type(self, gumtype):
        frequency = {}
        for item in self.lst:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1
        if gumtype != "red" and gumtype !="blue" and gumtype !="green":
            print("There are no gumballs of that type in the machine.")
        elif gumtype == "red":
            print("There are ", frequency.get("red"), " gumballs of type red in the machine.")
        elif gumtype == "green":
            print("There are ", frequency.get("green"), " gumballs of type green in the machine.")
        elif gumtype == "blue":
            print("There are ", frequency.get("blue"), " gumballs of type blue in the machine.")
