
board=[ "-","-","-",
        "-","-","-",
        "-","-","-"]

game_still_going = True

Winner= None

current_player= "X"

def dis_board():
    print( board[0] + " | " + board[1] + " | " + board[2])
    print( board[3] + " | " + board[4] + " | " + board[5])
    print( board[6] + " | " + board[7] + " | " + board[8])

def handle_turn(player):

    print(player + "'s turn.")
    position=input("Chose a position from 1-9: ")

    valid = False

    while not valid:
    
        while position not in ['1','2','3','4','5','6','7','8','9']:
         position= input("invaid input.Chose a position from 1-9: ")


        position= int(position)-1

        if board[position] == "-":
            valid=True
        else:
            print("This place is already taken. Try again.")

    board[position]= player

    dis_board()

def check_if_game_over():
    check_if_win()

    check_if_tie()

def check_if_win():
    global Winner

    #checkrow
    row_winner = checkrow()
    #checkcol
    col_winner = checkcol()
    #checkdiagnol
    diagnol_winner = checkdiagnol()

    if row_winner:
        Winner= row_winner
    elif col_winner:
        Winner= col_winner
    elif diagnol_winner:
        Winner = diagnol_winner
    else:
        Winner=None
    return
    


def checkrow():

    global game_still_going

    #checking for the row
    row_1= board[0]==board[1]==board[2] != "-"
    row_2= board[3]==board[4]==board[5] != "-"
    row_3= board[6]==board[7]==board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False
    
    #return the row winner(X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    
    return

def checkcol():

    global game_still_going

    #checking for column
    col_1=board[0]==board[3]==board[6] != "-"
    col_2=board[1]==board[4]==board[7] != "-"
    col_3=board[2]==board[5]==board[8] != "-"

    if col_1 or col_2 or col_3:
        game_still_going=False
    
    #return the column winner( X or O)
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]

    return

def checkdiagnol():
    
    global game_still_going

    #check for diagnol
    diag_1=board[0]==board[4]==board[8] != "-"
    diag_2=board[2]==board[4]==board[6] != "-"

    if diag_1 or diag_2:
        game_still_going=False

    #return the diagnol winner (X or O)
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]

    return

def check_if_tie():

    global game_still_going

    if "-" not in board:
        game_still_going=False
    return

def flip_player():

    global current_player

    if current_player=="X":
        current_player="O"
    else:
        current_player="X"
    
    return 

def play_game():

    #display initial board
    dis_board()


    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()
        
        flip_player()

    # the game has ended
    if Winner == "X" or Winner =="O":
        print (Winner + " won.")
    elif Winner == None:
        print("Tie.")


    
#call function
play_game() 

