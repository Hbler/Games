### Pierian Data Udemy Course - Milestone 1 Project ###

'''
Your assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.

Here are the requirements:

    2 players should be able to play the game (both sitting at the same computer)
    The board should be printed out every time a player makes a move
    You should be able to accept input of the player position and then place a symbol on the board
'''

### Steps
# create and display a board and a reference for input -ok
# define win condition -ok
# get first player's icon, validate it, update player order (list) -ok
# check turn -ok
# chek which squares are available -ok
# get input from a player and validate it -ok
# update and diplay board -ok
# after fifth turn start checking win condition -ok
# if someone win -ok
#   congratulate winner -ok
#   check if players want rematch -ok
#   refresh board -ok
# else, repeat from get input -ok

### Base Functions

## Board Functions

def display_board(board):
    
    board_position = board
    
    
    print('\nThis is the current board:\n')
    print(f' {board_position[0]} | {board_position[1]} | {board_position[2]}')
    print('-----------')
    print(f' {board_position[3]} | {board_position[4]} | {board_position[5]}')
    print('-----------')
    print(f' {board_position[6]} | {board_position[7]} | {board_position[8]}')

def display_ref():
    '''Displays a 3 x 3 "board" with numeric references for the each square'''

    print('These are the numbers for each square \n')
    print(' 0 | 1 | 2')
    print('-----------')
    print(' 3 | 4 | 5')
    print('-----------')
    print(' 6 | 7 | 8')

def update_board(position, board):
    '''Takes position, updates the board with player icon in position, displays board'''
    
    icon = order[check_player(tc)] # is 'X' or 'O'
    
    board[position] = icon

    print('\n' * 100)    
    display_board(board)
    
    return board

def refresh_board(board):
    '''Refreshes the board for a new game'''
    
    for i in range(len(board)):
        board[i] = ' '
        
    return board

## Check status functions

def check_player(num):
    """"Checks who's turn it is based on the turn counter number (turn counter is a global variable)"""
    
    if num%2 == 0:
        return 1
    else:
        return 0


def check_win(board):
    '''Check if any of the players won by comparing "squares" on a board (list)
    considering that the items in the list will be only X or O'''
    
    if board[0:3] == ['X','X','X'] or board[0:3] == ['O','O','O'] or board[3:6] == ['X','X','X'] or board[3:6] == ['O','O','O'] or board[6:] == ['X','X','X'] or board[6:] == ['O','O','O'] or board[0::3] == ['X','X','X'] or board[0::3] == ['O','O','O'] or board[1::3] == ['X','X','X'] or board[1::3] == ['O','O','O'] or board[2::3] == ['X','X','X'] or board[2::3] == ['O','O','O'] or board[0::4] == ['X','X','X'] or board[0::4] == ['O','O','O'] or board[2:8:2] == ['X','X','X'] or board[2:8:2] == ['O','O','O']:
        return True
    else:
        return False

def what_is_available(board):
    '''Checks which squares still available on the board, returns a list of strings'''
    
    available = []
    
    for sq in range(len(board)):
        if board[sq] == ' ':
            available.append(str(sq))
            
    return available

def new_game():
    '''Checks if players want to play again'''
    turns = 1
    game = 0
    options = ['Y','N']
    
    while game not in options:
        
        game = input(f'\nDo you want to play again? {options} ')
        
        if game.upper().replace(' ','') == 'Y':
            game = True
            return game, turns
        elif game.upper().replace(' ','') == 'N':
            print('\nThanks for Playing!')
            game = False
            return game, tc
        else:
            print('\n' * 100)
            print("Sorry, I didn't get that. Try again. ")
            game = 0

## Get inputs and other base functions

def get_icon():
    '''Gets the Icon the first player will use in the game'''
    
    p1_icon = 0
    icons = ['X','O']
    
    while p1_icon not in icons:
        
        first_player = input('\nFirst Player, please choose your Icon (X or O) ')
        p1_icon = first_player.upper().replace(' ','')

        
        if p1_icon not in icons:
            print('\n' * 100)
            print("\nThat's not a valid Icon, try again. 2 \n")

            
    return p1_icon

def players_order(icon):
    '''Creates a list with the order of players, based on the icon chosen by the first player'''
    
    p_order = []
    
    if icon == 'X':
        p_order.append(icon)
        p_order.append('O')
    else:
        p_order.append(icon)
        p_order.append('X')
        
    return p_order

def get_position(lst):
    '''Gets the square the player wants to tag'''
    
    sqr = 'wrong'
    options = lst
    
    while sqr not in options:
        
        print(f"\nIt's {order[check_player(tc)]}'s turn.")
        
        sqr = input (f'\nPlease choose a position on the board {options}\nTo check current board type B\nTo check the reference type R\n\n' )
        
        if sqr.upper().replace(' ','') == 'B':
            print('\n' * 100)
            display_board(bp) # bp is a global variable
            sqr = 'wrong'
        elif sqr.upper().replace(' ','') == 'R':
            print('\n' * 100)
            display_ref()
            sqr = 'wrong'
        elif sqr not in options:
            print('\n' * 100)
            print("Sorry, that square isn't available or it isn't a valid option.\nTry again \n")
            sqr = 'wrong'
            
    return int(sqr)

### Let's Play

## Global Variables
go = True # game on?
bp = [' ',' ',' ',' ',' ',' ',' ',' ',' '] # board positions
tc = 1 # turn counter

## Game

while go:
    
    if tc == 1:
        display_board(bp) # ...
        first_player = get_icon() # get's the icon of the first player
        order = players_order(first_player) # a list with the icons as strings
        is_available = what_is_available(bp) # a list with available spaces as strings
        play = get_position(is_available) # a position (num) as integer
        bp = update_board(play, bp) # updates board (duh, lol)
        tc += 1 # updates counter
    elif tc < 5:
        is_available = what_is_available(bp)
        play = get_position(is_available)
        bp = update_board(play, bp)
        tc += 1
    else:
        if check_win(bp): # checks if someone won, returns bool
            print(f'\nCongratulations {order[check_player(tc - 1)]} you won!')
            go, tc = new_game() # returns bool and resets the counter
            bp = refresh_board(bp) # ...
        elif tc >= 10:
            print('\nSorry no more possible winners.')
            go, tc = new_game()
        else:
            is_available = what_is_available(bp)
            play = get_position(is_available)
            bp = update_board(play, bp)
            tc += 1

### code by Hbler
