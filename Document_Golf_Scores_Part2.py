# Marie Ramsay
# This program reads the data on the text file (golf.txt) created by "Document_Golf_Scores_Part1"
# It then displays the golf players' names and whether or not they made par

# open the golf.txt file to read
file = open('golf.txt', 'r')
# reads the player array from the file
player_records = file.readlines()
# define par variable
par = 80
# print the data
for player in player_records:
    player_name = player.split(',')[0]
    player_score = player.split(',')[1]
    player_score = int(player_score)

    # determine and mark each player as being either over, under, or at par
    # If the score is = Par, then display 'Made Par'
    # If the score is < Par, then display 'Under Par'
    # If the score is > Par, then display 'Over Par'
    if player_score == par:
        par_rate = "Made Par"
    elif player_score < par:
        par_rate = "Under Par"
    else:
        par_rate = "Over Par"

    # display them with appropriate headings above the data being displayed.
    print(player_name + "\n" + par_rate + "\n")

# closes the file
file.close()

