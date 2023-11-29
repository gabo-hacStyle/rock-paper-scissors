import random

#valid choices as a tuple  
valid_choices = ("rock", "paper", "scissors")
#Count to see who is winning
player_wins = 0
computer_wins = 0
ties = 0

rounds = input("How many rounds do you want to play? ")

def get_player_choice():
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        while player_choice not in valid_choices:
            player_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
        return player_choice

def get_computer_choice():
        return random.choice(valid_choices)

def determine_winner(player_choice, computer_choice):
        if player_choice == computer_choice:
            global ties
            ties += 1
            return "It's a tie!"
        if (player_choice == "rock" and computer_choice == "scissors") or \
        (player_choice == "scissors" and computer_choice == "paper") or \
        (player_choice == "paper" and computer_choice == "rock"):
            global player_wins
            player_wins += 1
            
            return "You win!"
        else:
            global computer_wins
            computer_wins += 1
            return "You lose!"
def play_game():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    print(f"You chose {player_choice}, computer chose {computer_choice}. {result}")
     
for round in range(int(rounds)):
    print('--' *20)
    print('Computer Score: ', computer_wins)
    print('Player Score: ', player_wins)
    print('Ties: ', ties)
    print('--' *20)
    print(f"Round {round + 1}")
    print('--' *20)
    play_game()
    if round == int(rounds) - 1:
        print('--' *20)
        print('--' *20)
        print('Computer Score: ', computer_wins)
        print('Player Score: ', player_wins)
        print('Ties: ', ties)
        if player_wins > computer_wins:
            print("You won the game!")
        elif computer_wins > player_wins:
            print("You lost the game!")
        else:
            print("The game was a tie!")
        print('--' *20)
        print('--' *20)
    else:
        user_continue = input("Do you want to play again? (y/n): ").lower()
        if user_continue != "y":
            print('--' *20)
            print('--' *20)
            print('Computer Score: ', computer_wins)
            print('Player Score: ', player_wins)
            print('Ties: ', ties)
            if player_wins > computer_wins:
                print("You won the game!")
            elif computer_wins > player_wins:
                print("You lost the game!")
            else:
                print("The game was a tie!")
            print('--' *20)
            print('--' *20)
            break