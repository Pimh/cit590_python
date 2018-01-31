# CIT590 HW2 - Pig
# Pimkhuan (Pim) Hannanta-anan
# Due 9/13/2016
# This script launches a game called "Pig", a very simple game where two players
# takes turn to roll a die. The scores are added up over all the turns, and
# whoever reaches 100 points first or with a higher score wins. Run the script
# for more detailed instructions

import random

def main():

    # display the game instructions
    instructions()

    # initiate parameters
    score_com_tot = 0
    score_hum_tot = 0
    game_over = False
    
    while not game_over:
        # computer turn
        score_com_cur_turn = computer_move(score_com_tot,score_hum_tot)
        score_com_tot = score_com_tot + score_com_cur_turn

        # human turn
        score_hum_cur_turn = human_move(score_com_tot,score_hum_tot)
        score_hum_tot = score_hum_tot + score_hum_cur_turn

        # check if the game is over
        game_over = is_game_over(score_com_tot,score_hum_tot)

    # display the final results of the game
    show_results(score_com_tot,score_hum_tot)


def instructions():
# display the rules for the game
    print("RULES:")
    print("- Two players take turns;on each turn, a player rolls a six-sided die\
as many times as she wishes, or until she rolls a 1.")
    print("- Each number she rolls, except a 1, is added to her score this turn;\
but if she rolls a 1, her score for this turn is zero, and her turn ends.")
    print("- At the end of each turn, the score for that turn is added to the\
player's total score.")
    print("- The first player to reach or exceed 100 wins.")


def human_move(score_com,score_hum):

    score_hum_this_turn = 0
    keep_going = 1
    n_roll = 0

    # display computer and human scores
    print("\nGet ready for your next turn! :)")
    print(" computer score:", score_com)
    print(" player score:", score_hum)

    # calculate and display the score difference 
    score_diff = score_com - score_hum
    if score_diff >= 0:
        print(" you are trailing by", score_diff, "points")
    else:
        print(" you are leading by", -score_diff, "points")

    print("\nThis is a player turn!")       
    while keep_going:

        # the player always rolls the first roll of the current turn
        if n_roll == 0:
            is_roll = True
        else:
            # ask if the player wants to roll or stop for the subsequent rolls
            is_roll = ask_yes_or_no("\nRoll again? 'y'/'Y' for yes, 'n'/'N' for no: ")

        # if the player wishes to roll
        if is_roll:
            
            # player rolls the die
            roll_num = roll()
            n_roll = n_roll + 1
            print(" roll", n_roll, "player gets:", roll_num)

            # if the player gets 1
            if roll_num == 1:
                # stop the while loop
                keep_going = 0
                
                # return total score of zero
                score_hum_this_turn = 0
                print("\nSorry! you've lost all your score in this turn")
                return score_hum_this_turn
            
            # if the player gets anything except 1, add the value to the total score
            else:
                score_hum_this_turn = score_hum_this_turn + roll_num
                print(" your projected score is", score_hum_this_turn + score_hum)

        # if the player wishes to stop
        else:
            # stop the while loop
            keep_going = 0
            # return the total score
            return score_hum_this_turn

    
def computer_move(score_com,score_hum):

    score_com_this_turn = 0
    keep_going =1
    
    # set the number of times to roll, computer rolls 5 times every turn
    nroll_com = 5
    
    cur_roll = 1

    print("\nThis is a computer turn!")
    
    while keep_going and cur_roll <= nroll_com:
    
        # roll and display the result of each roll
        roll_num = roll()
        print(" roll", cur_roll, "computer gets:", roll_num)

        # calculate the total score of this turn
        if roll_num == 1:
            keep_going = 0
            score_com_this_turn = 0
        else:
            score_com_this_turn = score_com_this_turn + roll_num

        cur_roll += 1

    # return total score of this turn
    return score_com_this_turn

    
def is_game_over(score_com,score_hum):
# determine if the game is over
# return true if either player has >=100 and not tied; otherwise, false
    
    if score_com >= 100 or score_hum >= 100:
        if score_com == score_hum:
            return False
        else:
            return True
    else:
        return False
            
    
def roll():
# return a random number in range(1,6)

    roll_num = random.randint(1,6)
    return roll_num


def ask_yes_or_no(prompt):
# prompt the player a question if she wishes to continue rolling

    input_again = 1
    
    while input_again:
        # ask if the player wish to roll again
        player_yn = input(prompt)
        
        # take 'y'/'Y' for yes and 'n'/'N' for no, anything else repeat the question
        if player_yn == 'y' or player_yn == 'Y':
            return True
            input_again = 0
        elif player_yn == 'n' or player_yn == 'N':
            return False
            input_again = 0
        else:
            input_again = 1

    
def show_results(score_com,score_hum):
# call when the game has ended
# show the final result of the game - whether the human won or lost and how much

    if score_com > score_hum:
        score_diff = score_com - score_hum
        print("\nSorry! you lost by", score_diff, "points") 
    else:
        score_diff = score_hum - score_com
        print("\nCongratulations! you won by", score_diff, "points")


if __name__ == "__main__":
# run the main function
    main()
    
