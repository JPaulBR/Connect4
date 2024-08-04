# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

# import random
import random

# Create a matrix of 0's
def createMatrix():
    boarGame = [[0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0]]
    return boarGame

# Show a decent matrix for the user 
def ShowMatrix(matrix):
    header = "  A B C D E F G  "
    print(header)
    for i in range(0,6):
        line = str(i + 1) + " "
        for j in range(0,7):
            line += str(matrix[i][j]) + " "
        print(line)

# Defining a points for each position
def definingPointMatrix():
    pointMatrix = [[3,4,5,7,5,4,3],
                   [4,6,8,10,8,6,4],
                   [5,7,11,13,11,7,5],
                   [5,7,11,13,11,7,5],
                   [4,6,8,10,8,6,4],
                   [3,4,5,7,5,4,3]]
    return pointMatrix

# Valid if a player won by row
def winByRow():
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if (board[i][j] == PLAYER or board[i][j] == AI):
                currentPlayer = PLAYER if board[i][j] == PLAYER else AI
                slots = 0
                slotsNeeded = 4
                cont = j
                while cont < len(board[0]):
                    if board[i][cont] != currentPlayer:
                        break
                    slots += 1
                    cont += 1
                j = cont
                if slots == slotsNeeded:
                    winner = currentPlayer
                    return True
    return False

# Valid if a player won by column
def winByColumn():
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if (board[i][j] == PLAYER or board[i][j] == AI):
                currentPlayer = PLAYER if board[i][j] == PLAYER else AI
                slots = 0
                slotsNeeded = 4
                cont = i
                while cont < len(board):
                    if board[cont][j] != currentPlayer:
                        break
                    slots += 1
                    cont += 1
                if slots == slotsNeeded:
                    winner = currentPlayer
                    return True
    return False

# Valid if a player won by diagonal
def winByDiagonal():
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if (board[i][j] == PLAYER or board[i][j] == AI):
                currentPlayer = PLAYER if board[i][j] == PLAYER else AI
                if (validateDiagonal(i,j,currentPlayer,"left") or validateDiagonal(i,j,currentPlayer,"right")):
                    winner = currentPlayer
                    return True
    return False

# Valid if a winner in diagonal way (right or left)
def validateDiagonal(i,j,currentPlayer,direction):
    slots = 0
    slotsNeeded = 4
    diagonal = -1 if direction == "left" else 1
    while i < len(board) and j < len(board[0]):
        if board[i][j] != currentPlayer:
            break
        slots += 1
        i += 1
        j += diagonal
    return slots == slotsNeeded

#Check if it's a tie                    
def isTie():
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if board[i][j] == EMPTY_SLOT:
                return False
    return True

# Check if game has ended
def IsFinishGame():
    if (winByRow()):
        return True
    elif (winByColumn()):
        return True
    elif (winByDiagonal()):
        return True
    elif (isTie()):
        return True
    else:
        return False 

# define our clear function
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def showThinkingMessage():
    message = "Thinking"
    point = 0
    for i in range(0,7):
        if point == 3:
            message = "Thinking"
            point = 0
        message += "."
        point += 1
        print("AI turns")
        print(message)
        sleep(0.3)
        clear()

# Set Token in a specif slot of the board
def setSlotPlayer(column,currentPlayer):
    bottom = 5
    while(bottom >= 0):
        if board[bottom][column] == EMPTY_SLOT:
            board[bottom][column] = currentPlayer
            return True
        bottom -= 1
    return False

# Validate the player position chosen
def PlayerPlaying():
    while (True):
        ShowMatrix(board)
        print()
        print("Your turn")
        option = input("Enter your row position: ")
        if (int(option) >= len(board[0])):
            print("**** Invalid position ****")
            sleep(1)
            clear()
        elif (setSlotPlayer(int(option),PLAYER)):
            break
    clear()

# main program
def main():
    print("--------------------   Connect4 game programmed by Jean Paul Barrit   --------------------")
    turn = PLAYER
    while (not IsFinishGame()):
        clear()
        if turn == PLAYER:
            PlayerPlaying()
            print("Board updated")
            ShowMatrix(board)
            turn = AI
        else:
            showThinkingMessage()
            #bestMove = minmaxAlphaBeta() TO BE DEFINED
            column = random.choice([0,1,2,3,4,5,6])
            setSlotPlayer(column,AI)
            turn = PLAYER
    playerWinner = "AI" if winner == PLAYER else "PLAYER"
    print("GAME ENDED "+playerWinner+" has won")


board = createMatrix()
POINT_MATRIX = definingPointMatrix()
EMPTY_SLOT = 0
PLAYER = 1
AI = 2
winner = -1
main()