#Tic Tac Toe

#Modules
import random

#Game intro for players
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

        letters = int((input(f"Player 1, please pick a symbol. Enter 1 for 'X' and 2 for 'O': ")))

    # the function would return a list == [player 1 letter, player 2 letter]
    if letters == 1:
        return ['X', 'O']
    else:
        return ['O', 'X']

def random_player_start():
    #Random player to go first
    if (random.randint(1,2)) == 1:
        return 'Player 1'
    else:
        return 'Player 2'

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

intro()

while True:
    newBoard = [' '] * 10
    p1_letter, p2_letter = letter_input()
    turn = random_player_start()
    print(turn + ' will go first.')
    
    game_on = True

    while game_on:
        if turn == 'Player 1':
                
            board_display(newBoard)
            position = player_move(newBoard)
            move_choice(newBoard, p1_letter, position)

            if win_check(newBoard, p1_letter):
                board_display(newBoard)
                print('Congratulations! Player 1 has won the game!')
                game_on = False
            else:
                if full_board_check(newBoard):
                    board_display(newBoard)
                    print('The game has ended in a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            
            board_display(newBoard)
            move = player_move(newBoard)
            move_choice(newBoard, p2_letter, move)

            if win_check(newBoard, p2_letter):
                board_display(newBoard)
                print('Congratulations! Player 2 has won the game!')
                game_on = False

            else:
                if full_board_check(newBoard):
                    board_display(newBoard)
                    print('The game is a draw!')
                    break

                else:
                    turn = 'Player 1'

    if not play_again():
        break
