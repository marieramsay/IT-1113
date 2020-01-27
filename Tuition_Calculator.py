# Marie Ramsay
# Calculates and displays tuition for the next 7 years, starting with 2020. The base tuition is $7,180 for the year 2019
# and increases by 3.5% every year.


print("Welcome to the Tuition Calculator for Kennesaw State University!")
print("Here is the predicted tuition for KSU for the next 7 years:")

final_tuition = 7180  # base tuition for 2019
year = 2020  # this will keep track of which year it is
i = 1  # initiating the counter
while i < 8:
    final_tuition = final_tuition + (final_tuition * .035)  # equation to calculate the current years tuition
    final_tuition = float(final_tuition)
    final_tuition = round(final_tuition, 2)  # round final tution to 2 decimal places
    this_year = str(year)  # converts to string so it can be printed
    your_tuition = str(final_tuition)  # convert to string so it can be printed
    print(this_year + ":  $" + your_tuition)
    i += 1  # increase counter
    year += 1  # increase to the next year
