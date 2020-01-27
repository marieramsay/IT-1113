# Marie Ramsay
# Asks user to enter their name, and the number of books that he
# or she has purchased this month and displays their name and the number of points
# they have earned for the month based on the number of books purchased. Program runs once per user.
customerName = 0
books = 0
points = 0
print("Welcome Customer!")
print("Please enter your name.")
# save user's name to variable
customerName = input()
print("Please enter the number of books you have purchased this month.")
# save books purchased to variable (integer)
books = input()
books = int(books)
# determine number of points awarded based on number of books purchased
if books == 0:
    points = 0
elif 1 <= books <= 3:
    points = 5
elif 4 <= books <= 6:
    points = 10
elif 7 <= books <= 8:
    points = 15
elif books == 9:
    points = 20
else:
    points = 25
# save points awarded to variable (string)
yourPoints = str(points)
# display awarded points
print("Thank you! Here is your receipt:")
print(customerName + "  " + yourPoints)
print("Have a great day!")

