#
# Author: Adrian Martinez
# Description: Program creates a 1D chess set with two knights and a king for each player.
# King moves through empty spaces until it reaches a space, killing that piece. Knights move two
# spaces left or right. Game is over when a users king is killed.
#

import os, sys

cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, cwd)
from graphics import graphics

W_KNIGHT = 'WKn'
W_KING = 'WKi'
B_KNIGHT = 'BKn'
B_KING = 'BKi'
EMPTY = '   '
WHITE = 'White'
BLACK = 'Black'
LEFT = 'l'
RIGHT = 'r'


def is_valid_move(board, position, player):
    '''
    Function verifies whether user has input a valid move based on whether position is a valid
    index on the board list and the index position is one of the players positions
    :param board: List containing current piece positions
    :param position: Input designated position on list of which piece to move
    :param player: whether player is WHITE or BLACK
    :return: Boolean True or False, allowing player move
    '''
    if player == WHITE:     # Checks whether move is valid by checking position against user
        if board[position] == W_KNIGHT or board[position] == W_KING:
            return True
    if player == BLACK:
        if board[position] == B_KNIGHT or board[position] == B_KING:
            return True
    return False


def move_knight(board, position, direction):
    '''
    Function moves knight in input direction. New position is either two up or two down the
    original position, depending on user input of left or right. left moves position two down the
    list/board, right moves the position two up the list/board. Old position is replaced with EMPTY.
    :param board: List containing current piece positions
    :param position: Input designated position on list of which piece to move
    :param direction: Input direction moving the piece either left or right on list/board
    :return: none
    '''
    if direction == LEFT:                   # Moves knight left
        if board[position] == W_KNIGHT:
            board[position - 2] = W_KNIGHT  # Moves piece two left or right
            board[position] = EMPTY
        else:
            board[position - 2] = B_KNIGHT
            board[position] = EMPTY
    elif direction == RIGHT:                # Moves knight right
        if board[position] == W_KNIGHT:
            board[position + 2] = W_KNIGHT
            board[position] = EMPTY
        else:
            board[position + 2] = B_KNIGHT
            board[position] = EMPTY


def move_king(board, position, direction):
    '''
    Function moves king left or right on board, depending on user input. The king will move until
    it either reaches another piece, killing it, or reaches end of the board.
    :param board: List containing current board piece positions
    :param position: Input designated position on list of which piece to move
    :param direction: Input direction moving the piece either left or right on list/board
    :return: none
    '''
    piece = board[position]         # Sets initial position in temporary variable
    board[position] = EMPTY         # Sets old position to EMPTY
    king_moves = True
    while king_moves:               # loops until king hits a piece on the board
        if direction == LEFT:
            position -= 1
        else:
            position += 1
        if board[position] != EMPTY or position == len(board) - 1 or position == 0:
            board[position] = piece
            king_moves = False


def print_board(board):
    '''
    Function prints out current board to a standard output
    :param board: List containing current piece positions
    :return:
    '''
    print('+-----------------------------------------------------+')
    for i in range(len(board)):             # prints out pieces by position in list
        print('|', board[i], '', end='')
    print('|\n+-----------------------------------------------------+')


def draw_board(board, gui):
    '''
    Function displays board on graphical canvas with current piece positions
    :param board: List containing current piece positions
    :param gui: graphic interface module to display canvas
    :return:
    '''
    x_coord = 50
    gui.rectangle(50, 100, 542, 44, 'red3')                 # background for 1D board
    gui.text(225, 30, '1 Dimensional Chess', 'black', 25)   # Title
    gui.line(50, 100, 592, 100, 'black', 3)                 # Top line
    while x_coord <= 600:                                   # Prints out eight vertical lines
        gui.line(x_coord, 100, x_coord, 145, 'black', 3)
        x_coord += 60
    gui.line(50, 145, 592, 145, 'black', 3)                 # Bottom line
    x_coord = 53
    color = ''
    for i in board:                                         # Sets variables for printing out pieces
        if i == W_KING:
            i = 'king'
            color = 'white'
        elif i == W_KNIGHT:
            i = 'knight'
            color = 'white'
        elif i == B_KING:
            i = 'king'
            color = 'black'
        elif i == B_KNIGHT:
            i = 'knight'
            color = 'black'
        gui.text(x_coord, 115, i, color, 15)                # Prints out piece positions
        x_coord += 60
    gui.update_frame(10)


def is_game_over(board):
    '''
    Function checks whether user has lost king, determining whether a user has won or lost
    :param board: List containing current pieces positions
    :return:
    '''
    if B_KING not in board:     # Checks whether black king is on the board
        print_board(board)
        print('White wins!')
        return True
    if W_KING not in board:     # Checks whether white king is on board
        print_board(board)
        print('Black wins!')
        return True
    return False


def move(board, position, direction):
    '''
    Function determines which piece user is moving, if a knight is being moved, move_knight
    function called, if king move_king function called
    :param board: List containing current piece positions
    :param position: User input for which piece to move
    :param direction: User input for which direction to move piece
    :return: none
    '''
    if board[position] == W_KNIGHT or board[position] == B_KNIGHT:
        move_knight(board, position, direction)
    else:
        move_king(board, position, direction)


def main():
    gui = graphics(700, 200, '1 Dimensional Chess')

    # This is the starting board.
    # This board variable can and should be passed to other functions
    # and changed as moves are made.
    board = [W_KING, W_KNIGHT, W_KNIGHT, EMPTY, EMPTY, EMPTY, B_KNIGHT, B_KNIGHT, B_KING]

    # White typically starts in chess.
    # This will change between WHITE and BLACK as the turns progress.
    player = WHITE

    # This variable will be updated to be True if the game is over.
    # The game is over after one of the kings dies.
    is_game_won = False

    # This loop controls the repetitive nature of the turns of the game.
    while not is_game_won:

        print_board(board)

        # Draw the board
        draw_board(board, gui)

        position = int(input(player + ' enter index:\n'))
        direction = input(player + ' enter direction (l or r):\n')

        # If the desired move is valid, then call the move function.
        # Also, change the player variable.
        if is_valid_move(board, position, player):
            if player == WHITE:
                move(board, position, direction)
                player = BLACK
            else:
                move(board, position, direction)
                player = WHITE
            is_game_won = is_game_over(board)


main()

