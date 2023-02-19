"""
Christina Wang 7/14/22	CSCI-UA 2 - 002
Assignment #2 Problem #3
"""
#menu choices
print ("                Menu Choices                 ")
print ("---------------------------------------------")
print ("1. My Internet  is not working.")
print ("2. My cable is not working.")
print ("3. My bill is wrong.")
print ("4. I want to upgrade my plan.")
print ( )

#asks the user the question and converts their answer to an integer
choiceString = input("Choose from the following options (Enter a value 1 - 4): ")
choice = int(choiceString)

#defines what is an acceptable response to the following questions
yes = {'Y', 'y'}
no = {'N', 'n'}

#choice 1
#in cases where the user answers unacceptably, the program tells them so and invites them to call the company number
if choice == 1:
    print ()
    modem = input("Is your modem on?(Y/N): ")
    if modem in no:
        print ()
        print ("Plug your modem into the nearest outlet to turn on your modem. If you still cannot connect to the Internet, restart this program. Note, this program will now terminate. Goodbye!") 
    elif modem in yes:
        print ()
        router = input ("Is your router on? (Y/N): ")
        if router in no:
            print ()
            print("Plug your router into the nearest outlet to turn on your router. If you still cannot connect to the Internet, restart this program. Note, this program will now terminate. Goodbye!")
        elif router in yes:
            print ()
            red = input("Does your router emit a red light? (Y/N) ")
            if red in yes:
                print ()
                print("Unplug your router and wait thirty seconds. Then plug your router into the nearest outlet to restart your router. If you still cannot connect to the Internet, restart this program. Note, this program will now terminate. Goodbye!")
            elif red in no:
                print ()
                wifi = input("Are both your computer and wifi on? (Y/N) ")
                if wifi in no:
                    print ()
                    print("If your computer is not on, please turn it on by pressing the power button. Also make sure your computer's wifi is on.  If you still cannot connect to the Internet, restart this program. Note, this program will now terminate. Goodbye!")
                elif wifi in yes:
                    print ()
                    print("It looks like you may need additional support. Please call 555-555-5555 for additional support with this matter. Thank you for your patience.")
                elif not wifi in yes or no:
                    print ()
                    print("You entered an invalid menu choice. It looks like you may need additional support.  Please call 555-555-5555 for additional support. Thank you for your patience.")
            elif not red in yes or no:
                print ()
                print("You entered an invalid menu choice. It looks like you may need additional support.  Please call 555-555-5555 for additional support. Thank you for your patience.")
        elif not router in yes or no:
            print ()
            print("You entered an invalid menu choice. It looks like you may need additional support.  Please call 555-555-5555 for additional support. Thank you for your patience.")            
    elif not modem in yes or no:
        print ()
        print("You entered an invalid menu choice. It looks like you may need additional support.  Please call 555-555-5555 for additional support. Thank you for your patience.")

#choice 2
#in cases where the user answers unacceptably, the program tells them so and invites them to call the company number
if choice == 2:
    print ()
    cable = input("Is your cable box on? (Y/N) ")
    if cable in no:
        print ()
        print ("Plug your cable box into the nearest outlet to turn on your cable box. If you still do not receive a cable signal, please restart this program. Note, this program will now terminate. Goodbye!")
    elif cable in yes:
        print ()
        tv = input("Is your TV on? (Y/N) ")
        if tv in no:
            print ()
            print ("Plug your TV into the nearest outlet and press the power button on your remote to turn on your TV. If you still do not receive a cable signal, restart this program. Note, this program will now terminate. Goodbye!")
        if tv in yes:
            print ()
            print ("It looks like you may need additional support. Please call 555-555-5555 for additional support with this matter. Thank you for your patience.")
        elif not tv in yes or no:
            print ()
            print("You entered an invalid menu choice. It looks like you may need additional support.  Please call 555-555-5555 for additional support. Thank you for your patience.")
    elif not cable in yes or no:
        print ()
        print("You entered an invalid menu choice. It looks like you may need additional support.  Please call 555-555-5555 for additional support. Thank you for your patience.")
    
#choice 3
#in cases where the user answers unacceptably, the program tells them so and invites them to call the company number
if choice == 3:
    print ()
    payment = input("Were you late on your last payment? (Y/N) ")
    if payment in yes:
        print ()
        print ("If you were late on your last payment, you will be charged an additional 5% interest fee. Therefore, your bill may be more than usual. If you would like to contest your charge, please call 555-555-5555 for additional support with this matter. Thank you for your patience. Note, this program will now terminate. Goodbye! ")
    elif payment in no:
        print ()
        print ("It looks like you may need additional support. Please call 555-555-5555 for additional support with this matter. Thank you for your patience.")
    elif not payment in yes or no:
        print ()
        print("You entered an invalid menu choice. It looks like you may need additional support.  Please call 555-555-5555 for additional support. Thank you for your patience.")

#choice 4
if choice == 4:
    print ()
    print("It looks like you may need additional support. Please call 555-555-5555 for additional support with this matter. Thank you for your patience.")

#choice errors
#in cases where the user answers unacceptably, the program tells them so and invites them to call the company number
if choice >4:
    print ()
    print("You entered an invalid menu choice. It looks like you may need additional support.  Please call 555-555-5555 for additional support. Thank you for your patience.")
