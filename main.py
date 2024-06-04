import random

options = ['rock', 'paper', 'scissors']

while True:
    computer = random.choice(options)
    player = None

    while player not in options:
        player = input('rock, paper, or scissors?: ').lower()

    print(f"computer: {computer}")
    print(f"player: {player}")

    if player == computer:
        print("Tie")
    elif player == 'rock':
        if computer == 'paper':
            print("You lose!")
        else:  # computer == 'scissors'
            print("You win!")
    elif player == 'paper':
        if computer == 'scissors':
            print("You lose!")
        else:  # computer == 'rock'
            print("You win!")
    elif player == 'scissors':
        if computer == 'rock':
            print("You lose!")
        else:  # computer == 'paper'
            print("You win!")

    play_again = input('Play again? (yes/no): ').lower()

    if play_again != 'yes':
        break

print('Bye!')