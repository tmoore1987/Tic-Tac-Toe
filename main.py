import random


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

#global variables

currentPlayer = 'O'
winner = None
playing = True


def printBoard(board):
    print(board[0] + ' | ' + board [1] + ' | ' + board[2])
    print('----------')
    print(board[3] + ' | ' + board [4] + ' | ' + board[5])
    print('----------')
    print(board[6] + ' | ' + board [7] + ' | ' + board[8])


#main function

while playing:
    def game():
        global currentPlayer
        global winner
        printBoard(board)
        inp = int(input('Enter number 1-9:'))                   
        if inp >= 1 and inp <=9 and board[inp - 1] == '-':      # takes input 1-9 and checks to see that the space is available
            board[inp -1] = currentPlayer                       # set space = to current player
        else:
            print(f'Spot is already taken. Please select another spot!')

        #check if winner
        if board[0] == board[1]==board[2] and board[0] != '-':
            winner = board[0]
            print(f'The winner is {winner}.')
            return True
        elif board[3] == board[4]== board[5] and board[3] !='-':
            winner = board[3]
            print(f'The winner is {winner}.')
            return True
        elif board[6] == board[7]== board[8] and board[6] !='-':
            winner = board[6]
            print(f'The winner is {winner}.')
            return True

        
        if board[0] == board[3]==board[6] and board[0] != '-':
            winner = board[0]
            print(f'The winner is {winner}.')
            return True
        elif board[1] == board[4]== board[7] and board[1] !='-':
            winner = board[1]
            print(f'The winner is {winner}.')
            return True
        elif board[2] == board[5]== board[8] and board[2] !='-':
            winner = board[2]
            print(f'The winner is {winner}.')
            return True

        
        if board[0] == board[4]==board[8] and board[0] != '-':
            winner = board[0]
            print(f'The winner is {winner}.')
            return True
        elif board[2] == board[4]== board[6] and board[2] !='-':
            winner = board[2]
            print(f'The winner is {winner}.')
            return True
    # if list does not contain a space, all spaces must be taken up thefore it's a tie.   
    if '-' not in board:                    
        printBoard(board)
        print(f"It's a tie!")
        playing = False

    #switch player
    
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'


# ADD COMPUTER PLAYER
# ADD RESTART FUNCTION

    game()







    
    
