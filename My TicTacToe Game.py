

def display_board(board):
    print('\n'*100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
    pass











def player_input():
    placeholder = ''
    
    while placeholder != 'X' or placeholder != 'Y':
        placeholder = input('Player 1, Please decide on marker either X or O: ').upper()
        
        if placeholder == 'X':
            return ('X', 'O')
        elif placeholder == 'O':
            return ('O', 'X')
        else:
            continue

    
    pass











def place_marker(board, marker, position):
    #placeholder_board = board
    #placeholder_marker = marker
    #placeholder_position = position

    board[position] = marker

    
    
    pass











def win_check(board, mark):
    
    if (board[7] == mark and board[8] == mark and board[9] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[1] == mark and board[2] == mark and board[3] == mark) or (board[7] == mark and board[4] == mark and board[1] == mark) or (board[8] == mark and board[5] == mark and board[2] == mark) or (board[9] == mark and board[6] == mark and board[3] == mark) or (board[7] == mark and board[5] == mark and board[3] == mark) or (board[9] == mark and board[5] == mark and board[1] == mark):
        return True
 
    
    pass











import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    pass





def space_check(board, position):
    if board[position] == ' ':
        return True
    
    pass





def full_board_check(board):
    
    for i in range (1,10):
        if space_check(board,i):
            return False
    
    return True
    
    
    pass

















def player_choice(board):
    
    input_check = 'wrong'
    range_check = False
    
    while input_check.isdigit() == False or range_check == False:
        input_check = (input("Please key in your desired location between 1-9: "))
        
        if input_check.isdigit() == False:
            print('Kindly select a digit:')
            
        if input_check.isdigit() == True:
            #print('this is integer')
            if int(input_check) in range(0,10):
                #print('this is in range')
                if space_check(board,int(input_check)):
                    range_check = True
            else:
                print("you are out of range! please select location between 1-9")
                range_check = False
    
    return int(input_check)
    
    
    pass























def replay():
    choice = 'wrong'
    
    while choice not in ['Y','N']:
        choice = input('Keep Playinng? (Y or N): ')
        
        if choice not in ['Y','N']:
            print('sorry invalid choice')
            
    if choice == "Y":
        return True
    else:
        return False
    
    pass





print('Welcome to Tic Tac Toe!')

while True:
    empty_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + 'will go first!')
    
    playgame = input('are you ready to play! please key in y to proceed or key anything else to quit: ')
    
    if playgame.lower()[0] == 'y':
        gameon = True
    else:
        gameon = False
        
    while gameon:
        if turn == 'Player 1':
            display_board(empty_board)
            player_position = player_choice(empty_board)
            place_marker(empty_board,player1_marker,player_position)
            
            if win_check(empty_board,player1_marker):
                display_board(empty_board)
                print('congratulations! Player 2 you have won the game!!')
                gameon = False
                
            else:
                if full_board_check(empty_board):
                    display_board(empty_board)
                    print('The game is  a draw!!')
                    break
                else:
                    turn = 'Player 2'
                    
        else:
            display_board(empty_board)
            player_position = player_choice(empty_board)
            place_marker(empty_board,player2_marker,player_position) 
            
            if win_check(empty_board,player2_marker):
                display_board(empty_board)
                print('congratulations! Player 2 you have won the game!!')
                gameon = False
                
            else:
                if full_board_check(empty_board):
                    display_board(empty_board)
                    print('The game is  a draw!!')
                    break
                else:
                    turn = 'Player 1'
                    
    if replay() == False:
        break
                    


        
