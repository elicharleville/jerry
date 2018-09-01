#git pull https://github.com/elicharleville/jerry.git
#git push -u origin master
from enum import Enum
from pprint import pprint
import move

# 2d numpy array
# single digit ints as notifierss
# pawn :    1
# bishop:   2
# knight:   3
# rook:     4
# queen:    5
# king:     6
# black pieces are negative ints 

#    -Evaluate  - returns move 
#    -Search( board)
#    -GetLegalMoves()
#    -MakeMove()
#    -CheckIfMate()
#    -print() -- returns nice view of board layout

# definitions
P, B, N, R, Q, K = 1, 2, 3, 4, 5, 6
p, b, n, r, q, k = -1, -2, -3, -4, -5, -6
WHITE = 1
BLACK = -1


# need some helper functions:
# checkDiag() --used to help show how far I move diagonally
# checkCross() -- shows how far I can move horizontally 
# checkCheck() -- check if the king is in trouble check-- probably needs to be called after every move
# ^^ because of pins 

def printMoveList(moveList):
    for i in moveList:
        print(i.mString)



def inBound(row, col):
    if row < 8 and row >= 0 and col < 8 and col >= 0:
        return True
    else: 
        return False

class Board:
    def __init__(self, nextTurn, check, board = None):
        #from move import Move
        self.nextTurn = nextTurn  
        self.check = check 
        if board is None:
            self.board = [[r, n, b, q, k, b, n, r],                                           
                        [p, p, p, p, p, p, p, p],                                           
                        [0, 0, 0, 0, 0, 0, 0, 0],                                           
                        [0, 0, 0, 0, 0, 0, 0, 0],                                           
                        [0, 0, 0, 0, 0, 0, 0, 0],                                           
                        [0, 0, 0, 0, 0, 0, 0, 0],                                           
                        [P, P, P, P, P, P, P, P],                                             
                        [R, N, B, Q, K, B, N, R]]
        else:
            self.board = board 
        
                  
    #prints the board in graphics mode
    def printBoard(self):
        rNum = 8
        #cArray = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h']
        for row in range(0, 8): #print row by row
            print(str(rNum) + "  ", end= '')
            for c in range(0,8): 
                if self.board[row][c] == p:
                    print("p ", end= '')
                elif self.board[row][c] == b:
                    print("b ", end= '')
                elif self.board[row][c] == n:
                    print("n ", end= '')
                elif self.board[row][c] == r:
                    print("r ", end= '')
                elif self.board[row][c] == q:
                    print("q ", end= '')
                elif self.board[row][c] == k:
                    print("k ", end= '')
                elif self.board[row][c] == P:
                    print("P ", end= '')
                elif self.board[row][c] == B:
                    print("B ", end= '')
                elif self.board[row][c] == N:
                    print("N ", end= '')
                elif self.board[row][c] == R:
                    print("R ", end= '')
                elif self.board[row][c] == Q:
                    print("Q ", end= '')
                elif self.board[row][c] == K:
                    print("K ", end= '')
                else:
                    print(". ", end= '')
            print()            
            rNum = rNum - 1
        print()
        print("   a b c d e f g h")

    def getLegalMoves(self): #return list of moves
        moveList = []

        if self.nextTurn == WHITE:  
            sideConst = 1 
        else:
            sideConst = -1 

        for row in range(0, 8):
            for col in range(0,8):
                tSquare = self.board[row][col] * sideConst
                if tSquare > 0:
                    if tSquare == 1:
                        moveList += self.getPawnMoves(row, col)
                    elif tSquare == 2:
                        moveList += self.getbishopMoves(row, col)
                    elif tSquare == 4: #TODO add case for knight
                        moveList += self.getRookMoves(row, col)
                    elif tSquare == 5: 
                        moveList += self.getQueenMoves(row, col)
                    elif tSquare == 6:
                        moveList += self.getKingMoves(row, col)

        return moveList
        
    def getPawnMoves(self, row, col): 
        #1. check if pawn is in starting positon based on what side its on
        #2. if so, give ability to move up two squares
        moveList = []
        if self.nextTurn == WHITE:
            # handle checking for double jumping for pawn--WHITE
            if self.board[row - 1][col] == 0: 
                moveList.append(move.Move([[row, col],[row - 1, col]]))
            if row == 6:    
                if self.board[row - 2][col] == 0: 
                    moveList.append(move.Move([[row, col],[row - 2, col]]))

            # checking if black pieces are in immediate diag
            if self.board[row - 1][col - 1] < 0:
                moveList.append(move.Move([[row, col],[row - 1, col -1]]))
            if self.board[row - 1][col + 1] < 0:
                moveList.append(move.Move([[row, col],[row - 1, col + 1]]))
            
        else: #BLACK
            if self.board[row + 1][col] == 0: 
                moveList.append(move.Move([[row, col],[row + 1, col]]))
            if row == 1: 
                if self.board[row + 2][col] == 0:
                    moveList.append(move.Move([[row, col],[row + 2, col]]))

            # checking if white pieces are in imediate diag
            if self.board[row + 1][col - 1] > 0:
                moveList.append(move.Move([[row, col],[row + 1, col - 1]]))
            if self.board[row + 1][col + 1] > 0:
                moveList.append(move.Move([[row, col],[row + 1, col + 1]]))
        return moveList
  
    def getbishopMoves(self, row, col):
        moveList = self.checkDiag(row,col)
        return moveList

    def getKnightMoves(self, row, col):
        print()
    def getRookMoves(self, row, col):
        moveList = self.checkCross(row, col)
        return moveList
    def getKingMoves(self, row, col): #TODO if a move puts the king in check, its illegal
        #TODO moves off the board should not be attempted to access 
        moveList = []

        if self.nextTurn == WHITE: # sideConst is used when determining which pieces are friend or foe 
            sideConst = 1 
        else:
            sideConst = -1 

        inB = inBound(row - 1, col)


        tSquare = self.board[row - 1][col] * sideConst
        if inB:
            if tSquare != 0 and inB:
                if tSquare < 0:
                    moveList.append(move.Move([[row, col],[row - 1, col]])) # top
            elif tSquare == 0: 
                moveList.append(move.Move([[row, col],[row - 1, col]]))


        inB = inBound(row, col - 1)

        tSquare = self.board[row][col - 1] * sideConst
        if inB:
            if tSquare != 0:
                if tSquare < 0:
                    moveList.append(move.Move([[row, col],[row , col - 1]])) #left
            elif tSquare == 0: 
                moveList.append(move.Move([[row, col],[row , col - 1]]))
        


        inB = inBound(row + 1, col)
        tSquare = self.board[row + 1][col] * sideConst
        if inB:
            if self.board[row + 1][col] != 0:
                if tSquare < 0:
                    moveList.append(move.Move([[row, col],[row + 1, col]])) #down 
            elif tSquare == 0: 
                moveList.append(move.Move([[row, col],[row + 1, col]]))


        inB = inBound(row, col + 1)
        tSquare = self.board[row][col + 1] * sideConst
        if inB:
            if tSquare != 0:
                if tSquare < 0:
                    moveList.append(move.Move([[row, col],[row , col + 1]])) #right 
            elif tSquare == 0: 
                moveList.append(move.Move([[row, col],[row , col + 1]]))


        inB = inBound(row - 1, col + 1)
        tSquare = self.board[row - 1][col + 1] * sideConst
        if inB:
            if tSquare != 0:
                if tSquare < 0:
                    moveList.append(move.Move([[row, col],[row - 1, col + 1]])) #top right diag
            elif tSquare == 0: 
                moveList.append(move.Move([[row, col],[row - 1, col + 1]]))

        inB = inBound(row - 1, col + 1)
        tSquare = self.board[row - 1][col - 1] * sideConst
        if inB:
            if tSquare != 0:
                if tSquare < 0:
                    moveList.append(move.Move([[row, col],[row - 1, col - 1]])) #top left diag
            elif tSquare == 0: 
                moveList.append(move.Move([[row, col],[row - 1, col - 1]])) 

        inB = inBound(row + 1, col - 1)
        tSquare = self.board[row + 1][col - 1] * sideConst
        if inB:
            if tSquare != 0:
                if tSquare < 0:
                    moveList.append(move.Move([[row, col],[row + 1, col - 1]])) #bottom left diag
            elif tSquare == 0: 
                moveList.append(move.Move([[row, col],[row + 1, col - 1]]))

        inB = inBound(row - 1, col + 1)
        tSquare = self.board[row + 1][col + 1] * sideConst
        if inB:
            if tSquare != 0:
                if tSquare < 0:
                    moveList.append(move.Move([[row, col],[row + 1, col + 1]])) #bottom right diag
            elif tSquare == 0: 
                moveList.append(move.Move([[row, col],[row + 1, col + 1]]))
        
        return moveList


    def getQueenMoves(self, row, col):
        diagList = self.checkDiag(row, col)
        crossList = self.checkCross(row, col)
        moveList = diagList + crossList
        return moveList 
    def checkDiag(self, row, col): #returns list of moves
        # need to check both diagonal
        # ultimately, both loops put moves into the returning list 
        
        moveList = []
        tRow = row
        tCol = col 


        if self.nextTurn == WHITE: # sideConst is used when determining which pieces are friend or foe 
            sideConst = 1 
        else:
            sideConst = -1 
        
        
        while True: #top edge---- first diagonal--downward sloping
            tRow -= 1
            tCol -= 1 
            if tCol < 0 or tCol > 7 or tRow < 0 or tRow > 7:
                break

            tSquare = self.board[tRow][tCol]
            tSquare *= sideConst

            if tSquare != 0:
                if tSquare < 0:
                    moveList.append(move.Move([[row, col],[tRow, tCol]])) # want to add move before breaking if its an enemy  
                    break
                else:
                    break
            moveList.append(move.Move([[row, col],[tRow, tCol]]))
        
        tRow = row
        tCol = col

        while True: #bottom edge
            tRow += 1
            tCol += 1 
            if tCol < 0 or tCol > 7 or tRow < 0 or tRow > 7:  
                break

            tSquare = self.board[tRow][tCol]
            tSquare *= sideConst


            if tSquare != 0:
                if tSquare < 0:
                    moveList.append(move.Move([[row, col],[tRow, tCol]])) # want to add move before breaking if its an enemy  
                    break
                else:
                    break
            moveList.append(move.Move([[row, col],[tRow, tCol]]))

        #second diagonal -- upward sloping 
        tRow = row
        tCol = col

        while True: # top edge 
            tRow -= 1
            tCol += 1 
            if tCol < 0 or tCol > 7 or tRow < 0 or tRow > 7:
                break

            tSquare = self.board[tRow][tCol]
            tSquare *= sideConst

            if tSquare != 0:
                if tSquare < 0:
                    moveList.append(move.Move([[row, col],[tRow, tCol]])) # want to add move before breaking if its an enemy  
                    break
                else:
                    break
            moveList.append(move.Move([[row, col],[tRow, tCol]]))

        tRow = row
        tCol = col
        
        while True: # bottom edge 
            tRow += 1
            tCol -= 1 
            if tCol < 0 or tCol > 7 or tRow < 0 or tRow > 7:
                break
            
            
            tSquare = self.board[tRow][tCol]
            tSquare *= sideConst

            if tSquare != 0:
                if tSquare < 0:
                    moveList.append(move.Move([[row, col],[tRow, tCol]])) # want to add move before breaking if its an enemy  
                    break
                else:
                    break
            moveList.append(move.Move([[row, col],[tRow, tCol]]))
        
        return moveList
    def checkCross(self, row, col): 
        moveList = []
        tRow = row
        tCol = col

        if self.nextTurn == WHITE: # sideConst is used when determining which pieces are friend or foe 
            sideConst = 1 
        else:
            sideConst = -1 

        # need to check vertical and horizontal lines 

        while True: #vertical first -- vert top
            tRow -= 1
            if tRow < 0 or tRow > 7:
                break
            tSquare = self.board[tRow][tCol]
            tSquare *= sideConst

            if tSquare != 0:
                if tSquare < 0:
                    moveList.append(move.Move([[row, col],[tRow, tCol]]))
                    break
                else: 
                    break
            moveList.append(move.Move([[row, col],[tRow, tCol]]))

        tRow = row
        tCol = col
        while True: # vert bottom
            tRow += 1
            if tRow < 0 or tRow > 7:
                break
            tSquare = self.board[tRow][tCol]
            tSquare *= sideConst


            if tSquare != 0:
                if tSquare < 0:
                    moveList.append(move.Move([[row, col],[tRow, tCol]]))
                    break
                else: 
                    break
            moveList.append(move.Move([[row, col],[tRow, tCol]]))

        tRow = row
        tCol = col
        while True: #-- horiz left
            tCol -= 1
            if tCol < 0 or tCol > 7: #TODO  optimize these checking methods to only check necessary bounds
                break
            tSquare = self.board[tRow][tCol]
            tSquare *= sideConst


            if tSquare != 0:
                if tSquare < 0:
                    moveList.append(move.Move([[row, col],[tRow, tCol]]))
                    break
                else: 
                    break
            moveList.append(move.Move([[row, col],[tRow, tCol]]))
        
        tRow = row
        tCol = col
        while True: #-- horiz right
            tCol += 1
            if tCol < 0 or tCol > 7: 
                break
            tSquare = self.board[tRow][tCol]
            if tSquare != 0:
                break
            moveList.append(move.Move([[row, col],[tRow, tCol]]))
        
        return moveList

    def checkCheck(self, row, col):
        print()

#test code/ main
if __name__ == "__main__":
    newBoard = Board(WHITE, False)
    newBoard.board = [[0, 0, 0, 0, 0, 0, 0, 0],  
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, 0, Q, 0, 0, 0, 0],                                           
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, 0, 0, 0, 0, 0, 0],                                             
                    [0, 0, 0, 0, 0, 0, 0, 0],]
    
    testBoard = Board(WHITE, False)
    testBoard.board = [[0, 0, 0, 0, 0, 0, 0, 0],  
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, p, 0, p, 0, 0, 0],                                           
                    [0, 0, 0, P, 0, 0, 0, 0],                                             
                    [0, 0, 0, 0, 0, 0, 0, 0],]
    
    diagBoard = Board(WHITE, False)
    diagBoard.board = [[0, 0, 0, 0, 0, 0, 0, 0],  
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, P, 0, 0, 0, p, 0, 0],                                           
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, 0, Q, 0, 0, 0, 0],                                           
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, 0, 0, 0, 0, 0, 0],                                             
                    [0, 0, 0, 0, 0, 0, 0, 0],]

    horizBoard = Board(WHITE, False)
    horizBoard.board = [[0, 0, 0, 0, 0, 0, 0, 0],  
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, 0, P, 0, 0, 0, 0],                                           
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, 0, R, 0, 0, p, 0],                                         
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, 0, p, 0, 0, 0, 0],                                             
                    [0, 0, 0, 0, 0, 0, 0, 0],]

    kingBoard = Board(BLACK, False)
    kingBoard.board = [[0, 0, 0, 0, 0, 0, 0, 0],  
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, 0, p, p, 0, 0, 0],                                           
                    [0, 0, 0, k, 0, 0, 0, 0],                                         
                    [0, 0, 0, 0, P, 0, 0, 0],                                           
                    [0, 0, 0, 0, 0, 0, 0, 0],                                             
                    [0, 0, 0, 0, 0, 0, 0, 0],]





    horizList = horizBoard.checkCross(4,3)
    testList = diagBoard.checkDiag(4,3)

    kingList = kingBoard.getKingMoves(4, 3)

    printMoveList(kingList)


    #printMoveList(testList)
    #printMoveList(horizList)
    

    kingBoard.printBoard()

