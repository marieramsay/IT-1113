# Marie Ramsay
# Prompts the user for the name of the item AND the price of each item, and then simply displays whatever the user
# typed in on the screen with new formatting
itemName = 0
itemPrice = 0
print("Welcome Customer!")
print("Please enter the name of your item.")
itemName = input()
print("Please enter the price of the item")
itemPrice = input()
print("Thank you! Here is your receipt:")
print("Item: " + itemName + "    Price: " + itemPrice)
print("Have a great day!")
