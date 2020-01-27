# Marie Ramsay
# This program allows users to enter the golf score for each player. Then writes the information to a text file.
# The text file will be named "golf.txt" and will be created in the same the folder as the script.
# Refer to "Document_Golf_Scores_Part2" for the second part of the program

# save this data in a file named golf.txt. Please note, there are 16 players in the tournament
writer = open("golf.txt", "w+")

for x in range(16):

    # keep track of what data set the process is on
    data_number = x+1
    data_number = str(data_number)

    # accept as input each player's first name, last name, and golf score and then for each player
    print("Please enter Player " + data_number + "'s first and last name:")
    # save the user's selection to a variable
    player_name = input()
    print("Please enter Player " + data_number + "'s golf score:")
    # save the user's selection to a variable
    player_score = input()

    # write the data to the golf.txt
    writer.write(player_name + ',' + player_score + '\n')

    # if this is the last conversion, let the user know.
    if data_number == "16":
        print("You have entered all 16 players.")
        print("Please navigate to the second program!")
