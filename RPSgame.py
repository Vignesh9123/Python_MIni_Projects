import random, sys, time

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses and ties.


wins = 0
losses = 0
ties = 0

while True: # The main game loop
    print(str(wins) + " Wins" , str(losses) + " Losses" ,str(ties) + " Ties  ")
    while True: # Taking the player input
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input()
        if player_move == 'q':
            print('The game is quit')
            sys.exit() # quit the program
        elif player_move == 'r' or player_move == 'p' or player_move== 's':
            break
        print('Please type only r, p, s or q. ')

    # Display what the player chose

    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    # Display what the computer chose

    comp_no = random.randint(1, 3)
    if comp_no == 1:
        comp_move = 'r'
        time.sleep(1)
        print("ROCK")
    elif comp_no == 2:
        comp_move = "p"
        time.sleep(1)
        print("PAPER")
    elif comp_no == 3:
        comp_move = 's'
        time.sleep(1)
        print("SCISSORS")

    # Display and Record the win/loss/tie

    if player_move == comp_move:
        print('It is a Tie!')
        ties = ties + 1
    elif player_move == 'r' and comp_move == 's':
        print('You Win!')
        wins = wins + 1
    elif player_move == 'p' and comp_move == 'r':
        print("You Win!")
        wins = wins + 1
    elif player_move == 's' and comp_move == 'p':
        print('You Win!')
        wins = wins + 1
    elif player_move == 'r' and comp_move == 'p':
        print("You Lose!")
        losses = losses + 1
    elif player_move == 'p' and comp_move == 's':
        print("You Lose!")
        losses = losses + 1
    elif player_move == 's' and comp_move == 'r':
        print("You Lose!")
        losses = losses