from IPython.display import clear_output
import random

def display_board(board):
    print(f'{board[1]}|{board[2]}|{board[3]}')
    print('- - -')
    print(f'{board[4]}|{board[5]}|{board[6]}')
    print('- - -')
    print(f'{board[7]}|{board[8]}|{board[9]}')

def player_input():
    player1 = ''
    while not(player1 == 'X' or player1 == 'O'):
        player1 = input("Please pick a marker 'X' or 'O'")
    return player1

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    diag_maj = board[1]==mark and board[5]==mark and board[9]==mark
    diag_min = board[3]==mark and board[5]==mark and board[7]==mark
    column = False
    row = False
    for x in range(1,4):
        column_check = board[x]==mark and board[x+3]==mark and board[x+6]==mark
        column = column or column_check
    for y in range(1,4,3):
        row_check = board[y]==mark and board[y+1]==mark and board[y+2]==mark
        row = row or row_check
    return diag_maj or diag_min or column or row

def choose_first():
    return str(random.randint(1,2))

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    result = True
    for x in range(1,10):
        result = result and not space_check(board,x)
    return result

def player_choice(board):
    position = 0
    while position not in range(1,10):
        position = int(input('Please enter a number: '))
    if space_check(board, position):
        return position
    else:
        return player_choice(board)

def replay():
    result = ''
    while not (result == 'Y' or result == 'N'):
        result = input('Do you want to play again? Y/N')
    return result == 'Y'

def new_game():
    winner = ''
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    players = {'1': '', '2': ''}
    markers = 'XO'


    player_number = choose_first()
    print(f'Player {player_number}, choose your marker')

    player_marker = player_input()
    players[player_number] = player_marker

    markers = markers.replace(player_marker,'')

    for key,value in players.items():
        if value == '':
            players[key] = markers

    while winner == '':
        if full_board_check(board):
            print('Tie game!')
            winner = 'nobody'
            break
        print(f'Player {player_number} goes next')
        position = player_choice(board)
        place_marker(board, players[player_number], position)
        display_board(board)
        if win_check(board,players[player_number]):
            winner = 'Player '+player_number
        if player_number == '1':
            player_number = '2'
        else:
            player_number = '1'
    print(f'Congratulations, {winner} wins!!')  

    
    if replay():
        clear_output()
        new_game()

print('Welcome to Tic Tac Toe!')       
new_game()