# Marie Ramsay
# Prompts the user to select whether they want to convert Miles-to-Kilometers or Kilometers-to-Miles, then asks the user
# to enter the distance they wish to convert. Program converts value to the desired unit.
# Program will loop 15x.

import sys


# converts input from miles to kilometers 
def convert_miles_to_km(amount):
    the_answer = amount / 0.6214
    return the_answer


# converts input from kilometers to miles
def convert_km_to_miles(amount):
    the_answer = amount * 0.6214
    return the_answer


print("Welcome to the conversion calculator. This program will run 15 times.")

# use for in loop to run the procedure below 15X
for x in range(15):
    # keep track of what data set the process is on
    data_number = x + 1
    data_number = str(data_number)
    
    # ask user which conversion they want to do 
    print("Please enter which conversion you need to be done for conversion " + data_number + ":")
    print("A. Miles-to-Kilometers")
    print("B. Kilometers-to-Miles")
    
    # save the user's selection to a variable 
    conversion_selection = input()

    # decide which unit the input will be in 
    if (conversion_selection == "A") or (conversion_selection == "a"):
        unit_name = "miles"
    elif (conversion_selection == "B") or (conversion_selection == "b"):
        unit_name = "kilometers"
    else:
        sys.exit('Your input is invalid. Please enter A or B. The program will restart.')
    
    # ask the user for the value they want to convert
    print("Please enter how the amount of " + unit_name + " you want to convert:")

    # save the value to a variable
    convert_this = input()
    # change string to float
    convert_this = float(convert_this)

    # decide which function to send the variable to
    if unit_name == "miles":
        converted_amount = convert_miles_to_km(convert_this)
        converted_amount = str(converted_amount)
        convert_this = str(convert_this)
        print(convert_this + " " + unit_name + " converts to " + converted_amount + " kilometers.")
        print(" ")
    else:
        converted_amount = convert_km_to_miles(convert_this)
        converted_amount = str(converted_amount)
        convert_this = str(convert_this)
        print(convert_this + " " + unit_name + " converts to " + converted_amount + " miles.")
        print(" ")

    # if this is the last conversion, let the user know. 
    if data_number == "15":
        print("You have converted 15 values.")
        print("Thank you for using the Conversion Calculator!")

