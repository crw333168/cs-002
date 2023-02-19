"""
Christina Wang	8/17/22	CSCI-UA 2 - 006
Assignment #8 Problem #3
"""

class Smartphone:
    again = True
    def __init__(self, capacity, name):
        self.capacity = capacity
        self.name = name
        self.appdict={}
        self.now_capacity=0
        print("Smartphone created!")

    def add_app(self, appname, appsize):
        self.appname=appname
        self.appsize=appsize
        if appsize+self.now_capacity > self.capacity:
            print("Cannot install app, no available space")
        else:
            self.appdict[self.appname] = int(self.appsize)
            self.now_capacity += self.appsize

    def report(self):
        print("Name: ", self.name)
        print("Capacity: ", self.now_capacity, " out of ", self.capacity, " GB")
        print("Available space: ", int(self.capacity-self.now_capacity))
        print("Apps installed: ", len(self.appdict))
        for key in self.appdict :
            print("* ", key, " is using ", self.appdict.get(key), " GB")

    def remove_app(self, appname):
        self.appname=appname
        print("App removed: ", self.appname)
        self.now_capacity -= int(self.appdict.get(self.appname))

    def has_app(self, appname):
        if appname in self.appdict:
            return True
        else:
            return False



smartphone = Smartphone(int(float(input("Size of your new smartphone (32, 64, or 128 GB): "))), input("Smartphone name: "))

while smartphone.again == True:
    
    value=input("(r)eport, (a)dd app, r(e)move app or (q)uit: ")
    if value == "q":
        print("Goodbye!")
        smartphone.again = False
    else:
        if value == "r":
            smartphone.report()
        elif value == "a":
            appname= input("App name to add: ")
            appsize =int(float(input("App size in GB: ")))
            smartphone.add_app(appname, appsize)
        elif value == "e":
            appname= input("App name to remove: ")
            smartphone.remove_app(appname)
    print()
        
