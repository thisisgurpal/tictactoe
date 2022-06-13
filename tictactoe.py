theBoard = {'11': ' ' , '12': ' ' , '13': ' ' ,
            '21': ' ' , '22': ' ' , '23': ' ' ,
            '31': ' ' , '32': ' ' , '33': ' ' }

def printBoard(board):
    print(board['11'] + '|' + board['12'] + '|' + board['13'])
    print('-----')
    print(board['21'] + '|' + board['22'] + '|' + board['23'])
    print('-----')
    print(board['31'] + '|' + board['32'] + '|' + board['33'])

printBoard(theBoard)

def checkWin(turn, theBoard):
    if((theBoard['11'] == theBoard['12'] == theBoard['13'] != ' ') or 
    (theBoard['21'] == theBoard['22'] == theBoard['23'] != ' ') or
    (theBoard['31'] == theBoard['32'] == theBoard['33'] != ' ') or
    (theBoard['11'] == theBoard['21'] == theBoard['31'] != ' ') or
    (theBoard['12'] == theBoard['22'] == theBoard['32'] != ' ') or
    (theBoard['13'] == theBoard['23'] == theBoard['33'] != ' ') or
    (theBoard['11'] == theBoard['22'] == theBoard['33'] != ' ') or
    (theBoard['13'] == theBoard['22'] == theBoard['31'] != ' ')):
        return 1
    elif(turn == 9):
        return 2
    else:
        return 3



def startGame():
    
    for turn in range(1,10):
        if (turn%2 == 0):
            character='O'
        else:
            character='X'
        pos = ""
        while(pos not in theBoard or theBoard[pos] != ' '):
            pos = input(f"{character}'s turn. Enter the position = ")
            if pos in theBoard and theBoard[pos] == ' ':
                theBoard[pos]=character
                break
            elif pos in theBoard and theBoard[pos] != ' ':
                print("Position already filled.")
            else:
                print("Incorrect position, choose again.")
                
        printBoard(theBoard)
        result = checkWin(turn, theBoard)
        if(result == 2):
            print("It's a draw.")
            break
        elif(result == 1):
            print(f"{character} wins!")
            break
    
    print("Game Over.")



        

startGame()


