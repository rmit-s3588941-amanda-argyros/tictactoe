board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def userMove():
    run = True
    while run:
        move = input("Which position would you like? Choose from 1-9")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceFree(move):
                    run = False
                    insertLetter("X", move)
                else:
                    print ("Sorry, that sapce is full, choose another space.")
            else:
                print("Out of range. Please enter a number between 1 and 9")
        except ValueError:
            print("No valid integer! Please enter a number between 1 and 9")

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def computerMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    # 1. check for win result
    for letter in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = letter
            if isWinner(boardCopy, letter):
                move = i
                return move

    # 2. check for block user

    # 3. choose corner location
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    # 4. choose center location
    if 5 in possibleMoves:
        move = 5
        return move

    # 5. choose edge location
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
 
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
 
    return move

def spaceFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print ('   |   |')
    print (' ' + board[1] + ' | ' + board[2] + ' | ' +  board[3])
    print ('   |   |')
    print ('------------')
    print ('   |   |')
    print (' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print ('   |   |')
    print ('------------')
    print ('   |   |')
    print (' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print ('   |   |')
    print ('------------')

# def printBoard():
#     board = ''

#     for i in range(-1,6):

#         if i%2==0:
#             board += '|      ' * 4
#             board += '\n|      |      |      |'

#         else:
#             board += ' _____ ' * 3

#         board += '\n'
#     print (board)

def isWinner(board, letter):
    return (board[1] == letter and board[2] == letter and board[3] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[7] == letter and board[8] == letter and board[9] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[3] == letter and board[5] == letter and board[7] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[3] == letter and board[6] == letter and board[9] == letter)


def boardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print ("Welcome to Tic Tac Toe")
    printBoard(board)

    while not (boardFull(board)):
        if not (isWinner(board, "O")):
            userMove()
            printBoard(board)
        else:
            print ("Sorry, computer won this time, try again?")
            break

        if not (isWinner(board, "X")):
            move = computerMove()
            if move == 0:
                print('Game is a Tied! No more spaces left to move.')
            else:
                insertLetter('O', move)
                print('Computer placed an O in position', move)
                printBoard(board)
        
        else:
            print ("You won! Congratulations!")
            break

    if boardFull(board):
        print ("Tied game")

main()
while True:
    newGame = input('Would you like to play another game? (Y/N)')
    if newGame.lower() == 'y' or newGame.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break