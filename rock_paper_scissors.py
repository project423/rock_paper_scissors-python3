from random import choice

print('Welcome to rock paper scissors')
# player_two = input("Enter player twos choice: ")
# player_one = player_one.lower()
play = True
while play:
    player_one = input("Enter player ones choice: ").lower()
    player_two = choice(['rock', 'paper', 'scissors'])
    if player_one == player_two:
        print('It is a tie')
    elif player_one == 'rock':
        if player_two == 'scissors':
            print('Player one wins')
        elif player_two == 'paper':
            print('Player two wins')
    elif player_one == 'scissors':
        if player_two == 'rock':
            print('Player two wins')
        elif player_two == 'paper':
            print('Player one wins')
    elif player_one == 'paper':
        if player_two == 'rock':
            print('Player one wins')
        elif player_two == 'scissors':
            print('Player two wins')
    print(f'Player one chose {player_one}, and the computer chose {player_two}')
    play_again = input("Do you want to play again y/n?").lower()
    if play_again != 'y':
        play = False
        
    