#import random function
import random
choices = ["Rock", "Paper", "Scissors"]
#initial player choice o fals at first
player = False
#initialize score to zero at the beginning
computer = 0
player_score = 0
#iteration
while True:
    #accept player choice
    player = input("Rock, Paper or  Scissors?").capitalize()
    #set computer input from random option selected
    computer = random.choice(choices)
    ## Conditions of Rock,Paper and Scissors
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            computer+=1
        else:
            print("You win!")
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!")
            computer+=1
        else:
            print("You win!")
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "wins", player)
            computer+=1
        else:
            print("You win!")
            player_score+=1
    elif player=='End':
        #declare reslts if game is terminated and declare scores
        print("Final Scores:")
        print(f"computer:{computer}")
        print(f"Player:{player_score}")
        break
