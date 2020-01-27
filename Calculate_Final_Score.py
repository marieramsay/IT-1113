# Marie Ramsay
# Determines an athlete’s final score for the event, from 5 scores.
# The highest and lowest scores are discarded and then the average of the rest of the scores is calculated.


def find_final_score(the_scores):
    # find the min score
    min_position = the_scores.index(min(the_scores))
    # remove the min score
    the_scores.pop(min_position)
    # find the max score
    max_position = the_scores.index(max(the_scores))
    # remove the max score
    the_scores.pop(max_position)
    # find the average of the scores
    score_total = sum(the_scores)
    score_avg = score_total / len(the_scores)
    print(the_scores)
    return score_avg


scores = []
for x in range(5):
    # keep track of what data set the process is on
    score_number = x + 1
    score_number = str(score_number)

    # ask user which conversion they want to do
    print("Please enter Judge # " + score_number + "'s score:")

    # save the score to a variable
    the_score = input()
    the_score = float(the_score)
    # append the score to the list
    scores.append(the_score)
print(scores)
final_score = find_final_score(scores)
print("The athletes final score is: " + str(final_score))

