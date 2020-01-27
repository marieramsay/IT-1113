# this program allows users to enter the amount of rainfall for each month in a year.
# the program will then calculates the total yearly rainfall, the average, the month with the lowest
# rainfall and the month with the most amount of rainfall

# create a list of months
the_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
# create a empty list for the rainfall amounts
rainfall_by_month = []
# loop through list to enter 12 rainfall amounts
for i in range(12):
    print("Please enter rainfall for " + the_months[i] + ":")
    # save user input as element in list
    the_rainfall = float(input())
    rainfall_by_month.append(the_rainfall)
# calculate total rainfall
total_rainfall = sum(rainfall_by_month)
# calculate average rainfall
avg_rainfall = total_rainfall / 12
avg_rainfall = round(avg_rainfall, 2)
# find lowest amount of rainfall
min_rainfall = min(rainfall_by_month)
# find highest amount of rainfall
max_rainfall = max(rainfall_by_month)
# get the position of the lowest rainfall amount and use it to match with corresponding month in the month array
min_position = rainfall_by_month.index(min_rainfall)
# get the position of the highest rainfall amount and use it to match with corresponding month in the month array
max_position = rainfall_by_month.index(max_rainfall)


print("Total rainfall: " + str(total_rainfall) + " inches")
print("Average rainfall: " + str(avg_rainfall) + " inches")
print("Month with highest rainfall: " + str(the_months[max_position]))
print("Month with lowest rainfall: " + str(the_months[min_position]))
