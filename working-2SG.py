# importing Numpy for some necessary operations
import numpy as np

# =============================
# Welcome to the 2 Squares Game! 
# ------------------------------
#||  01  |  02  |  03  |  04  || 
# ---------------------------
#||  05  |  06  |  07  |  08  || 
# ---------------------------
#||  09  |  10  |  11  |  12  || 
# ---------------------------
#||  13  |  14  |  15  |  16  || 
# =============================

# Author: CS112 - 2022 & | Moustafa Aly Hashem | ID: 20210394
# Version: 1.0
# Date: 10 March 2022

# 1- Build game board
# 2- Display game board
# 3- nActions = 0

# 4- While (nActions != 8) 
#       5- Get player X action
#       6- Update game board
#       7- Get player O action
#       8- Update game board
#        9- If 2 cells are left
#               - see their values
#               - if adjacent -> x wins
#               - if not      -> o wins
#       10- if (nActions == 8)
#           10.a Break
#       11- nActions += 1
# 12- Print ("Draw")

board = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', \
         '14', '15', '16']

# Displaying the board 1st time...
def display_board():
    print (" =============================")
    print (" Welcome to the 2 Squares Game! ")
    print (" ------------------------------")
    print ("|| " ,  board[0],  " | ",  board[1],  " | ",    board[2],  " | ",   board[3],  " || ")
    print (" ---------------------------")
    print ("|| " ,  board[4],  " | ",  board[5],  " | ",    board[6],  " | ",   board[7],  " || ")
    print (" ---------------------------")
    print ("|| ",   board[8],  " | ",  board[9],  " | ",    board[10], " | ",   board[11], " || ")
    print (" ---------------------------")
    print ("|| ",   board[12], " | ",  board[13], " | ",    board[14], " | ",   board[15], " || ")
    #print (" ---------------------------")
    print (" =============================")

# Get 1st response from player
def get_player_action1 (player):
    is_valid = False
    message1 = "Please choose 1st cell from 1 to 16 for player " + player + ": "
    global action1
    while (not is_valid):
        action1 = input (message1)
        if not (action1).isdigit():
            continue
        else:
            is_valid = True
            action1 = int(action1)
            is_valid = is_valid and int(action1) > 0 and int(action1) <= 16
            is_valid = is_valid and board[action1 -1] != 'X'
    return action1

#temp = action1

# Get 2nd response from player
def get_player_action2 (player):
    is_valid = False
    message2 = "Please choose 2nd cell from 1 to 16 for player " + player + ": "
    while (not is_valid):
        action2 = input (message2)
        if not (action2).isdigit():
            continue
        else:
            is_valid = True
            action2 = int(action2)
            is_valid = is_valid and int(action2) > 0 and int(action2) <= 16
            is_valid = is_valid and board[action2 -1] != 'X'
            #Goto label;
    return action2


def update_game_board (action1, action2, player):
    board [action1 - 1] = player
    board [action2 - 1] = player
    display_board()


def is_winner():
    counter = 0
    for  i in board:
      temp1 = np.zeros(16)
      if (i != 'XX'):
        counter = counter + 1
        temp1[counter] = i
        if (counter == 2):
          if ((abs(temp1[1] - temp1[2]) != 1)  and \
              (abs(temp1[1] - temp1[2]) != 4)):
               cond = True
        else:
          cond = False
    return cond


def play_game():
    display_board()
    n_actions = 0

    while (n_actions != 8):

        # Flags initialization
        flag_x      = True
        flag_o      = True
        boarders1   = False
        boarders2   = False

        action1 = get_player_action1 ('X')
        action2 = get_player_action2 ('X')

        #=================================
        #    wrong input from player X
        #=================================
        while(flag_x):
            if   ((int(action1)==4 or int(action1)==8 or int(action1)==12)  and \
                  (int(action2)==5 or int(action2)==9 or int(action2)==13)):
                  boarders1 = True
            elif ((int(action2)==4 or int(action2)==8 or int(action2)==12) and \
                  (int(action1)==5 or int(action1)==9 or int(action1)==13)):
                  boarders2 = True
            else:
                  boarders1 = False
                  boarders2 = False

            if  ((abs(int(action1) - int(action2)) > 1)  and \
                 (abs(int(action1) - int(action2)) != 4)):
                  print ('Attention! 2nd input is not valid! please enter an adjacent cell')
                  action2 = get_player_action2 ('X')
            elif(boarders1 or boarders2):
                  print ('Attention! 2nd input is not valid! please enter an adjacent cell')
                  action2 = get_player_action2 ('X')
            elif(abs(int(action1) == int(action2))):
                  print ('Attention! 2nd input was entered before! please choose another cell')
                  action2 = get_player_action2 ('X')
            else:
                 flag_x = False
        #=================================

        # updating the board with actions from player X
        update_game_board (action1, action2, 'XX')
        if (is_winner()):
            print ('X wins! CONGRATULATIONS!!')
            break
        n_actions += 1
        if (n_actions == 8):
            break

        # Getting actions from player O
        action1 = get_player_action1 ('O')
        action2 = get_player_action2 ('O')

        #=================================
        #    wrong input from player O
        #=================================
        while(flag_o):
            if   ((int(action1)==4 or int(action1)==8 or int(action1)==12)  and \
                  (int(action2)==5 or int(action2)==9 or int(action2)==13)):
                  boarders1 = True
            elif ((int(action2)==4 or int(action2)==8 or int(action2)==12) and \
                  (int(action1)==5 or int(action1)==9 or int(action1)==13)):
                  boarders2 = True
            else:
                  boarders1 = False
                  boarders2 = False

            if  ((abs(int(action1) - int(action2)) > 1)  and \
                 (abs(int(action1) - int(action2)) != 4)):
                  print ('Attention! 2nd input is not valid! please enter an adjacent cell')
                  action2 = get_player_action2 ('X')
            elif((boarders1 or boarders2)):
                  print ('Attention! 2nd input is not valid! please enter an adjacent cell')
                  action2 = get_player_action2 ('X')
            elif(abs(int(action1) == int(action2))):
                  print ('Attention! 2nd input was entered before! please choose another cell')
                  action2 = get_player_action2 ('X')
            else:
                 flag_o = False
        #=================================

        # updating the board with actions from player O
        update_game_board (action1, action2, 'XX')
        if (is_winner()):
            print ('O wins! CONGRATULATIONS!!')
            break
        n_actions += 1

    if (not is_winner()):
        print ('Draw')

#############################
play_game()
