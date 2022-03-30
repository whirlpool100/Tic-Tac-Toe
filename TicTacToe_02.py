#Tic Tac Toe

#Modules
import random


#Game intro for player
def intro():

    print('================================================================================')
    print('Welcome to Tic Tac Toe'.center(80))
    print('--------------------------------------------------------------------------------')
    print("The rules are simple.".center(80))
    print("You need to have 3 of your markers in a row to win!".center(80))
    print('Each grid on the board would be assigned to a number as shown below.'.center(80))
    print("\n")
    print("\t     |     |     ".center(80))
    print("\t  1  |  2  |  3  ".center(80))
    print("\t_____|_____|_____".center(80))
    print("\t     |     |     ".center(80))
    print("\t  4  |  5  |  6  ".center(80))
    print("\t_____|_____|_____".center(80))
    print("\t     |     |     ".center(80))
    print("\t  7  |  8  |  9  ".center(80))
    print("\t     |     |     ".center(80))
    print("\n")
    print('Enter the number accordingly to place your marker on the grid of your choice.'.center(80))
    print('Have Fun!'.center(80))
    print('================================================================================')

def board_display(board):
    print('\n')
    print('\t     |     |     ')
    print('\t ' + board[1] + '   |  ' + board[2] + '  |   ' + board[3])
    print('\t_____|_____|_____')
    print('\t     |     |     ')
    print('\t ' + board[4] + '   |  ' + board[5] + '  |   ' + board[6])
    print('\t_____|_____|_____')
    print('\t     |     |     ')
    print('\t ' + board[7] + '   |  ' + board[8] + '  |   ' + board[9])
    print('\t     |     |     ')
    print('\n')

def letter_input():
    # Let player choose their letter to play with
    letters = ''

    while letters not in [1,2]:

        letters = int((input(f"Please pick a symbol. Enter 1 for 'X' and 2 for 'O': ")))

    # the function would return a list == [player letter, computer letter]
    if letters == 1:
        return ['X', 'O']
    else:
        return ['O', 'X']

def random_player_start():
    #Random player to go first
    if (random.randint(1,2)) == 1:
        return 'Player'
    else:
        return 'Computer'

def move_choice(board, letter, move):
    board[move] = letter

def space_check(board, move):
    return board[move] == ' '

def full_board_check(board):
    for x in range(1,10):
        if space_check(board,x):
            return False
    return True

def player_move(board):

    move = 0

    while move not in [1,2,3,4,5,6,7,8,9] or not space_check(board, move):
        move = int((input("Please choose your move: ")))
 
    return move

def win_check(board, letter):

    return ((board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[1] == letter and board[4] == letter and board[7] == letter) or
    (board[2] == letter and board[5] == letter and board[8] == letter) or
    (board[3] == letter and board[6] == letter and board[9] == letter) or 
    (board[1] == letter and board[5] == letter and board[9] == letter) or
    (board[3] == letter and board[5] == letter and board[7] == letter))

def play_again():

    choice = " "

    while choice not in [1,2]:

        choice = int((input(f"Would you like to continue playing? \nEnter 1 if you would like to continue or 2 if you would like to quit: ")))

    if choice == 1:
        return True
    else:
        return False


def random_move_choice(board, moves_list):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    
    possible_moves = []
    
    for i in moves_list:
        if space_check(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None

def board_copy(board):
    # Make a duplicate of the board list and return it the duplicate.

    copied_board = []

    for i in board:
        copied_board.append(i)
    return copied_board

def computer_move(board, computer_letter):
    # Given a board and the computer's letter, determine where to move and return that move.

    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # Algorithm for Tic Tac Toe AI:
    # First, check if we can win in the next move

    for i in range(1, 10):
        copy = board_copy(board)

        if space_check(copy, i):
            move_choice(copy, computer_letter, i)

            if win_check(copy, computer_letter):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = board_copy(board)
        
        if space_check(copy, i):
            move_choice(copy, player_letter, i)

            if win_check(copy, player_letter):
                return i

    # Try to take one of the corners, if they are free.

    move = random_move_choice(board, [1, 3, 7, 9])

    if move != None:
        return move

    # Try to take the center, if it is free.

    if space_check(board, 5):
        return 5

    # Move on one of the sides.

    return random_move_choice(board, [2, 4, 6, 8])

    # Return True if every space on the board has been taken. Otherwise return False.

intro()

while True:

    new_board = [' '] * 10
    player_letter, computer_letter = letter_input()
    turn = random_player_start()
    print('The ' + turn + ' will go first.')

    game_on = True

    while game_on:

        if turn == 'Player':

            # Player’s turn.
            board_display(new_board)
            move = player_move(new_board)
            move_choice(new_board, player_letter, move)

            if win_check(new_board, player_letter):
                board_display(new_board)
                print('Congratulations! You have won the game!')
                game_on = False

            else:
                if full_board_check(new_board):
                    board_display(new_board)
                    print('The game has ended in a draw!')
                    break

                else:
                    turn = 'Computer'
        else:
            # Computer’s turn.
            move = computer_move(new_board, computer_letter)
            move_choice(new_board, computer_letter, move)
            
            if win_check(new_board, computer_letter):
                board_display(new_board)
                print('The computer has won! You lose.')
                game_on = False

            else:
                if full_board_check(new_board):
                    board_display(new_board)
                    print('The game has ended in a draw!')
                    break

                else:
                    turn = 'Player'

    if not play_again():
        break

