# Marie Ramsay
# Calculates income tax based on information from the user
import sys

gross_income = 0
income_tax = 0

print("What was your total income for 2018?")

gross_income = input()
gross_income = float(gross_income)
# Tests if income text is less than $10,000, greater than or equal to $10,000 but less than or equal to $50,000,
# or greater than $50,000.
if gross_income < 10000:
    income_tax = gross_income*.23

elif 10000 <= gross_income <= 50000:
    income_tax = gross_income*.45

else:
    income_tax = gross_income*.61

print("What was is your martial status? \n a. single \n b. married")


martial_status = input()
# Tests marital status. If user's input was not one of the choices, code will stop.
if martial_status == "a" or martial_status == "A":
    income_tax = income_tax
elif martial_status == "b" or martial_status == "B":
    income_tax = income_tax - 24.62
else:
    sys.exit('Your input is invalid. Please start over.')


print("What is the elevation of your home? \n a. below sea level \n b. at sea level \n c. above sea level")
elevation = input()
# Test the elevation of user home. If user's input is not one of the choices, code will stop running.
if elevation == "a" or elevation == "A":
    income_tax = income_tax + 18.32
elif elevation == "b" or elevation == "B":
    income_tax = income_tax
elif elevation == "c" or elevation == "C":
    income_tax = income_tax
else:
    sys.exit('Your input is invalid. Please start over.')

# rounds income tax to 2 decimal places
income_tax = round(income_tax, 2)
your_income_tax = str(income_tax)


print("Your income tax for 2019 is $" + your_income_tax + ".")
print("Have a great day!")