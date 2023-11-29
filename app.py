# Import the random module for generating random choices
import random

# Define the valid choices for the game as a tuple
valid_choices = ("rock", "paper", "scissors")

# Initialize counters for the number of wins by the player, the computer, and ties
player_wins = 0
computer_wins = 0
ties = 0

# Ask the user for the number of rounds they want to play
rounds = input("How many rounds do you want to play? ")

# Function to get the player's choice
def get_player_choice():
    # Ask the player for their choice
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    # If the player's choice is not valid, ask again until a valid choice is made
    while player_choice not in valid_choices:
        player_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return player_choice

# Function to get the computer's choice
def get_computer_choice():
    # The computer's choice is a random selection from the valid choices
    return random.choice(valid_choices)

# Function to determine the winner of a round
def determine_winner(player_choice, computer_choice):
    # If the player's choice is the same as the computer's, it's a tie
    if player_choice == computer_choice:
        global ties
        ties += 1
        return "It's a tie!"
    # Define the conditions for the player to win
    if (player_choice == "rock" and computer_choice == "scissors") or \
    (player_choice == "scissors" and computer_choice == "paper") or \
    (player_choice == "paper" and computer_choice == "rock"):
        global player_wins
        player_wins += 1
        return "You win!"
    # If none of the above conditions are met, the computer wins
    else:
        global computer_wins
        computer_wins += 1
        return "You lose!"
    
#Function to print the scores
def print_scores():
    print('--' *20)
    print('Computer Score: ', computer_wins)
    print('Player Score: ', player_wins)
    print('Ties: ', ties)

# Function to play a round of the game
def play_game():
    player_choice = get_player_choice()
    print(' ' * 20)
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    print(f"-->> You chose {player_choice}, computer chose {computer_choice}. {result}")
    print(' ' * 20)

# Function to handle the end of the game
def end_game():
    print('--' *20)
    print('End of the gamee!!'.upper())
    print_scores()
    if player_wins > computer_wins:
        print("You won the game!")
    elif computer_wins > player_wins:
        print("You lost the game!")
    else:
        print("The game was a tie!")
    print('--' *20)
    print('--' *20)

# Play the game for the number of rounds specified by the user
for round in range(int(rounds)):
    print_scores()
    print('--' *20)
    print(f"Round {round + 1}")
    print('--' *20)
    #Function to play the game
    play_game()
    # If it's the last round, end the game
    if round == int(rounds) - 1:
        end_game()
    # If it's not the last round, ask the user if they want to continue playing
    else:
        user_continue = input("Quit game? (y/N): ")
        # If the user doesn't want to continue, end the game and break the loop
        if user_continue == "y":
            end_game()
            break