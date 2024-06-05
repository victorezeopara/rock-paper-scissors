import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_player_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()