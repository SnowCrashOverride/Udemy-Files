
player1_list = []
player2_list = []


def player_marker_input(): 
    
    player1 = ' '
    player2 = ' '
    player1 = input("Player 1 choose X or O: ").upper()
    while player1 != 'X' and player1 != 'O':
        player1 = input("Player 1 choose X or O: ")
    if player1 == 'X':
        player2 = 'O'
        print ("Player 1 is X, Player 2 is O")
    else:
        player2 = 'X'
        print ("Player 1 is O, Player 2 is X")
    
    return (player1, player2)   
        


def player1_space_input(player1_marker, board_list):

    while True:

        player1 = int(input("Player 1 enter the number of the space you'd like to play: "))
        
        if player1 == 1 and board_list[0] == " ":
            board_list.pop(0)
            board_list.insert(0, player1_marker)
            player1_list.append(1)
            break
        elif player1 == 2 and board_list[1] == " ":
            board_list.pop(1)
            board_list.insert(1, player1_marker)
            player1_list.append(2)
            break
        elif player1 == 3 and board_list[2] == " ":
            board_list.pop(2)
            board_list.insert(2, player1_marker)
            player1_list.append(3)
            break
        elif player1 == 4 and board_list[3] == " ":
            board_list.pop(3)
            board_list.insert(3, player1_marker)
            player1_list.append(4)
            break
        elif player1 == 5 and board_list[4] == " ":
            board_list.pop(4)
            board_list.insert(4, player1_marker)
            player1_list.append(5)
            break
        elif player1 == 6 and board_list[5] == " ":
            board_list.pop(5)
            board_list.insert(5, player1_marker)
            player1_list.append(6)
            break
        elif player1 == 7 and board_list[6] == " ":
            board_list.pop(6)
            board_list.insert(6, player1_marker)
            player1_list.append(7)
            break
        elif player1 == 8 and board_list[7] == " ":
            board_list.pop(7)
            board_list.insert(7, player1_marker)
            player1_list.append(8)
            break
        elif player1 == 9 and board_list[8] == " ":
            board_list.pop(8)
            board_list.insert(8, player1_marker)
            player1_list.append(9)
            break
        else:
            print("That space is already taken")

    return (player1_list)
        

def player2_space_input(player2_marker, board_list):

    while True:

        player2 = int(input("Player 2 enter the number of the space you'd like to play: "))
        
        if player2 == 1 and board_list[0] == " ":
            board_list.pop(0)
            board_list.insert(0, player2_marker)
            player2_list.append(1)
            break
        elif player2 == 2 and board_list[1] == " ":
            board_list.pop(1)
            board_list.insert(1, player2_marker)
            player2_list.append(2)
            break
        elif player2 == 3 and board_list[2] == " ":
            board_list.pop(2)
            board_list.insert(2, player2_marker)
            player2_list.append(3)
            break
        elif player2 == 4 and board_list[3] == " ":
            board_list.pop(3)
            board_list.insert(3, player2_marker)
            player2_list.append(4)
            break
        elif player2 == 5 and board_list[4] == " ":
            board_list.pop(4)
            board_list.insert(4, player2_marker)
            player2_list.append(5)
            break
        elif player2 == 6 and board_list[5] == " ":
            board_list.pop(5)
            board_list.insert(5, player2_marker)
            player2_list.append(6)
            break
        elif player2 == 7 and board_list[6] == " ":
            board_list.pop(6)
            board_list.insert(6, player2_marker)
            player2_list.append(7)
            break
        elif player2 == 8 and board_list[7] == " ":
            board_list.pop(7)
            board_list.insert(7, player2_marker)
            player2_list.append(8)
            break
        elif player2 == 9 and board_list[8] == " ":
            board_list.pop(8)
            board_list.insert(8, player2_marker)
            player2_list.append(9)
            break
        else:
            print("That space is already taken")

    return (player2_list)
  

def check_winner(player1_list, player2_list):
    count = 0
    
    win_1 = [1, 2, 3]
    win_2 = [4, 5, 6]
    win_3 = [7, 8, 9]
    win_4 = [1, 4, 7]
    win_5 = [2, 5, 8]
    win_6 = [3, 6, 9]
    win_7 = [1, 5, 9]
    win_8 = [3, 5, 7]

    if all(i in player1_list for i in win_1) or \
       all(i in player1_list for i in win_2) or \
       all(i in player1_list for i in win_3) or \
       all(i in player1_list for i in win_4) or \
       all(i in player1_list for i in win_5) or \
       all(i in player1_list for i in win_6) or \
       all(i in player1_list for i in win_7) or \
       all(i in player1_list for i in win_8):
        return False
    elif all(i in player2_list for i in win_1) or \
       all(i in player2_list for i in win_2) or \
       all(i in player2_list for i in win_3) or \
       all(i in player2_list for i in win_4) or \
       all(i in player2_list for i in win_5) or \
       all(i in player2_list for i in win_6) or \
       all(i in player2_list for i in win_7) or \
       all(i in player2_list for i in win_8):
        return False
    else:
        return True


def display_board(board_list):
    s1 = board_list[0]
    s2 = board_list[1]
    s3 = board_list[2]
    s4 = board_list[3]
    s5 = board_list[4]
    s6 = board_list[5]
    s7 = board_list[6]
    s8 = board_list[7]
    s9 = board_list[8]

    board ="""
     %s | %s | %s
    ---|---|---
     %s | %s | %s
    ---|---|---
     %s | %s | %s
     
    """ % (s7, s8, s9, s4, s5, s6, s1, s2, s3)

    print (board)
            

def main():
    player1_list = []
    player2_list = []
    board_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player1_marker, player2_marker = player_marker_input()
    count = 0
    display_board(board_list)

    while True:
   
        player1_list = player1_space_input(player1_marker, board_list)
        display_board(board_list)
        player1_list.sort()
        check_winner(player1_list, player2_list)
        if check_winner(player1_list, player2_list) == False:
            print ("Player 1 is the true champion! Congradulations!")
            break
        count += 1
        if count == 9:
            print ("It's a tie! Nobody wins!")
            break
     
        player2_list = player2_space_input(player2_marker, board_list)
        display_board(board_list)
        player2_list.sort()
        check_winner(player1_list, player2_list)
        if check_winner(player1_list, player2_list) == False:
            print ("Player 2 has overcome all odds and is the true winner! Amazing!")
            break
        count += 1
        if count == 9:
            print ("It's a tie! Nobody wins!")
            break

        
if __name__ == '__main__':
    main()

