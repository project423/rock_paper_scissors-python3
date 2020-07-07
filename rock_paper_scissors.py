from random import choice

print('Welcome to rock paper scissors')
# player_two = input("Enter player twos choice: ")
# player_one = player_one.lower()
play = True
score = [0,0]
while play and max(score) < 3:
    player_one = input("Enter player ones choice: ").lower()
    player_two = choice(['rock', 'paper', 'scissors'])
    if player_one == player_two:
        print('It is a tie')
    elif player_one == 'rock':
        if player_two == 'scissors':
            print('Player one wins')
            score[0] +=1
        elif player_two == 'paper':
            print('Player two wins')
            score[1] +=1
    elif player_one == 'scissors':
        if player_two == 'rock':
            print('Player two wins')
            score[1] +=1
        elif player_two == 'paper':
            print('Player one wins')
            score[0] +=1
    elif player_one == 'paper':
        if player_two == 'rock':
            print('Player one wins')
            score[0] +=1
        elif player_two == 'scissors':
            print('Player two wins')
            score[1] +=1
    print(f'Player one chose {player_one}, and the computer chose {player_two}')
    print(f'The computer has a score of {score[1]} and you have a score of {score[0]}')
    if score[0] == 3:
        print('Congrats you win!')
    elif score[1] == 3:
        print('Sorry, the computer won')
    if max(score) == 3:
        score = [0,0]
        play_again = input("Do you want to play again y/n? ").lower()
        if play_again != 'y':
            
            play = False
        
    