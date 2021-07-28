import random

while True:
    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)
    player = ' '

    while player not in choices:
        player = input('rock, paper, or scissors? ').lower()
        print('')
    if player == computer:
        print('Player:', player.lower())
        print('Computer:', computer)
        print("\nThere's a tie!")
    elif player == 'rock':
        if computer == 'paper':
            print('Player:', player.lower())
            print('Computer:', computer)
            print("\nYou lose!")
        if computer == 'scissors':
            print('Player:', player.lower())
            print('Computer:', computer)
            print("\nYou win!")
    elif player == 'paper':
        if computer == 'scissors':
            print('Player:', player.lower())
            print('Computer:', computer)
            print("\nYou lose!")
        if computer == 'rock':
            print('Player:', player.lower())
            print('Computer:', computer)
            print("\nYou win!")
    elif player == 'scissors':
        if computer == 'rock':
            print('Player:', player.lower())
            print('Computer:', computer)
            print("\nYou lose!")
        if computer == 'paper':
            print('Player:', player.lower())
            print('Computer:', computer)
            print("\nYou win!")

    play_again = input('\n\nPlay again? (yes/no): ').lower()

    if play_again != 'yes':
        break
print('Thank you for playing!')
