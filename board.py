#git pull https://github.com/elicharleville/jerry.git
#git push -u origin master
#from enum import Enum
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
    def __init__(self, nextTurn, check = None, board = None):
        #from move import Move
        self.nextTurn = nextTurn
        if check is None: self.check = False
        else: self.check = check 
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
        self.moveList = self.legalMoves(self.nextTurn, True) #TODO this can be cleaned up
        self.numMoves = len(self.moveList)
        
                  
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

    def legalMoves(self, nextTurn, init): #return list of moves
        moveList = []

        prevTurn = self.nextTurn # want to temporarily switch the state of the board object so that the getMove methods behave correctly
        self.nextTurn = nextTurn

        for row in range(0, 8):
            for col in range(0,8):
                tSquare = self.board[row][col] * self.nextTurn
                if tSquare > 0:
                    if tSquare == 1:
                        moveList += self.pawnMoves(row, col)
                    elif tSquare == 2:
                        moveList += self.bishopMoves(row, col)
                    elif tSquare == 3:
                        moveList += self.knightMoves(row, col)
                    elif tSquare == 4: 
                        moveList += self.rookMoves(row, col)
                    elif tSquare == 5: 
                        moveList += self.queenMoves(row, col)
                    elif tSquare == 6: #for kingMoves, need specific parameter
                        moveList += self.kingMoves(row, col, init)

        self.nextTurn = prevTurn # aaaand we switch back 
        return moveList
        
    def pawnMoves(self, row, col): #TODO Promotions
        #1. check if pawn is in starting positon based on what side its on
        #2. if so, give ability to move up two squares
        moveList = []
        if self.nextTurn == WHITE:

            # check if this is a promotion move
            if row == 1: promotion = True
            else: promotion = False

            
            if self.board[row - 1][col] == 0: 
                moveList.append(move.Move([[row, col],[row - 1, col]], promotion))
            if row == 6: # handle checking for double jumping for pawn--WHITE
                if self.board[row - 2][col] == 0: 
                    moveList.append(move.Move([[row, col],[row - 2, col]]))

            # checking if black pieces are in immediate diag
            if col > 0:
                if self.board[row - 1][col - 1] < 0:
                    moveList.append(move.Move([[row, col],[row - 1, col -1]], promotion))
            if col < 7:
                if self.board[row - 1][col + 1] < 0:
                    moveList.append(move.Move([[row, col],[row - 1, col + 1]], promotion))

            
        else: #BLACK TODO add sideConst method to this

            # check if this is a promotion move
            if row == 6: promotion = True
            else: promotion = False

            if self.board[row + 1][col] == 0: 
                moveList.append(move.Move([[row, col],[row + 1, col]]))
            if row == 1: 
                if self.board[row + 2][col] == 0:
                    moveList.append(move.Move([[row, col],[row + 2, col]]))

            # checking if white pieces are in imediate diag
            if col > 0:
                if self.board[row + 1][col - 1] > 0:
                    moveList.append(move.Move([[row, col],[row + 1, col - 1]], promotion))
            if col < 7:
                if self.board[row + 1][col + 1] > 0:
                    moveList.append(move.Move([[row, col],[row + 1, col + 1]], promotion))
        return moveList
  
    def bishopMoves(self, row, col):
        moveList = self.checkDiag(row,col)
        return moveList

    def knightMoves(self, row, col): 
        #check all eight possible squares
        moveList = []

        if self.nextTurn == WHITE: 
            sideConst = 1 
        else:
            sideConst = -1 

        #going clockwise starting with top right . . .

        rowAdd = [-2, -1, 1, 2, 2, 1, -1, -2]
        colAdd = [1, 2, 2, 1, -1, -2, -2, -1]

        for i in range (0,8):
            inB = inBound(row + rowAdd[i], col + colAdd[i]) 
            if inB: 
                tSquare = self.board[row + rowAdd[i]][col + colAdd[i]] * sideConst
                if tSquare <= 0:
                    moveList.append(move.Move([[row, col],[row + rowAdd[i], col + colAdd[i]]]))

        return moveList
        
    def rookMoves(self, row, col):
        moveList = self.checkCross(row, col)
        return moveList
       
    def kingMoves(self, row, col, init):

        # if otherKing is false, then normal, else do not run check check
        moveList = []
        rowAdd = [-1, 0, 1, 0, -1, -1, +1, -1]
        colAdd = [0, -1, 0, 1, 1, 1, -1, 1]

        for i in range(0, 8):
            inB = inBound(row + rowAdd[i], col + colAdd[i])
            check = False
            if inB:
                if init:
                    check = self.checkCheck(row + rowAdd[i], col+colAdd[i]) #need to check if this move puts me in check 
                tSquare = self.board[row + rowAdd[i]][col + colAdd[i]] * self.nextTurn
                if tSquare <= 0 and not check:
                    moveList.append(move.Move([[row, col],[row + rowAdd[i], col + colAdd[i]]])) 
        return moveList


    def queenMoves(self, row, col):
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


        if self.nextTurn == WHITE: 
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
                    moveList.append(move.Move([[row, col],[tRow, tCol]])) 
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
                    moveList.append(move.Move([[row, col],[tRow, tCol]]))  
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
                    moveList.append(move.Move([[row, col],[tRow, tCol]])) 
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
       #  check = False  

        oppList = self.legalMoves(self.nextTurn * -1, False)
        
        tSquare = self.board[row][col] * self.nextTurn
        if tSquare > 0:
            return True #not technically in check but it is not a legal move
        
        for move in oppList:
            if move.coordSet[1] == [row, col]:
                return True
    
    def pieceCount(self, piece = None):
        countArray = [0] * 7 #0th index will be 0 for neatness's sake
        for row in range(0,8):
            for col in range(0,8):
                tSquare = self.board[row][col] * self.nextTurn #whatever side has the next turn gets its pieces counted 
                if tSquare == P:
                    countArray[P] += 1
                elif tSquare == B:
                    countArray[B] += 1 
                elif tSquare == N:
                    countArray[N] += 1 
                elif tSquare == R:
                    countArray[R] += 1 
                elif tSquare == Q:
                    countArray[Q] += 1 
                elif tSquare == K:
                    countArray[K] += 1 
        if piece is None:
            return countArray
        else:
            return countArray[piece]
            
    def moveCount(self):
        return len(self.moveList)
        

                        
            


#test code/ main
if __name__ == "__main__":
    newBoard = Board(WHITE, False)
    newBoard.printBoard()
    #kingsList = newBoard.kingMoves(2,5)
    #printMoveList(kingsList)

    
    
    countList = newBoard.pieceCount()
    print(countList)
    printMoveList(newBoard.moveList)
    print(len(newBoard.moveList))
    #print(newBoard.checkCheck(2,5))

