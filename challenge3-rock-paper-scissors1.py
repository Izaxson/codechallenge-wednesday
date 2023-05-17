#
# import random function
import random
#get user input as choice
def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ")
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
#get computer choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
#function to compare computer and user input to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Main program
print("Welcome to Rock, Paper, Scissors!")
#iterate to for player to continue lating or end game
play_again = 'yes'

while play_again.lower() == 'yes':
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"Computer chooses: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input("Do you want to play again? (yes/no): ")

print("Thank you for playing!")
