import numpy #prolly not needed
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
BLACK = 0



# need some helper functions:
# checkDiag() --used to help show how far I move diagonally
# checkCross() -- shows how far I can move horizontally 
# checkCheck() -- check if the king is in trouble check-- probably needs to be called after every move
# ^^ because of pins 

def printMoveList(moveList):
    for i in moveList:
        print(i.mString)

class Board:
    def __init__(self):
        #from move import Move
        self.nextTurn = WHITE  
        self.check = False 
        self.board = [[r, n, b, q, k, b, n, r],                                           
                    [p, p, p, p, p, p, p, p],                                           
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [P, P, P, P, P, P, P, P],                                             
                    [R, N, B, Q, K, B, N, R]]
                  
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
        print()
    def getPawnMoves(self, row, col):
        print()
    def getbishopMoves(self, row, col):
        print()
    def getKnightMoves(self, row, col):
        print()
    def getRookMoves(self, row, col):
        moveList = self.checkCross( row, col)
        return moveList
    def getQueenMoves(self, row, col):
        print()
    def getKingMoves(self, row, col):
        print()
    def checkDiag(self, row, col): #returns list of moves TODO needs fixing
        # need to check both diagonal
        # ultimately, both loops put moves into the returning list 
        # first diagonal--downward sloping
        moveList = []
        tRow = row
        tCol = col 
        
        while True: #top edge
            tRow -= 1
            tCol -= 1 
            if tCol < 0 or tCol > 7 or tRow < 0 or tRow > 7:
                break

            tSquare = self.board[tRow][tCol]

            if tSquare != 0:
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

            if tSquare != 0:
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

            if tSquare != 0:
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

            if tSquare != 0:
                break
            moveList.append(move.Move([[row, col],[tRow, tCol]]))
        
        return moveList
    def checkCross(self, row, col):
        moveList = []
        tRow = row
        tCol = col

        # need to check vertical and horizontal lines 

        while True: #vertical first -- vert top
            tRow -= 1
            if tRow < 0 or tRow > 7:
                break
            tSquare = self.board[tRow][tCol]
            if tSquare != 0:
                break
            moveList.append(move.Move([[row, col],[tRow, tCol]]))

        tRow = row
        tCol = col
        while True: #vertical first -- vert bottom
            tRow += 1
            if tRow < 0 or tRow > 7:
                break
            tSquare = self.board[tRow][tCol]
            if tSquare != 0:
                break
            moveList.append(move.Move([[row, col],[tRow, tCol]]))

        tRow = row
        tCol = col
        while True: #-- vert top
            tRow -= 1
            if tRow < 0 or tRow > 7:
                break
            tSquare = self.board[tRow][tCol]
            if tSquare != 0:
                break
            moveList.append(move.Move([[row, col],[tRow, tCol]]))

        tRow = row
        tCol = col
        while True: #-- horiz left
            tCol -= 1
            if tCol < 0 or tCol > 7: #TODO  optimize these checking methods to only check necessary bounds
                break
            tSquare = self.board[tRow][tCol]
            if tSquare != 0:
                break
            moveList.append(move.Move([[row, col],[tRow, tCol]]))

        
        tRow = row
        tCol = col
        while True: #-- horiz right
            tCol += 1
            if tCol < 0 or tCol > 7: #TODO  optimize these checking methods to only check necessary bounds
                break
            tSquare = self.board[tRow][tCol]
            if tSquare != 0:
                break
            moveList.append(move.Move([[row, col],[tRow, tCol]]))
        
        return moveList

    def checkCheck(self, row, col):
        print()





#TODO make some test boards 
#test code/ main
if __name__ == "__main__":
    newBoard = Board()
    newBoard1 = Board()
    newBoard2 = Board()
    newBoard3 = Board()
    newBoard4 = Board()
    newBoard5 = Board()

    newBoard.board = [[0, 0, 0, 0, 0, 0, 0, 0],  
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, 0, Q, 0, 0, 0, 0],                                           
                    [0, 0, 0, 0, 0, 0, 0, 0],                                           
                    [0, 0, 0, 0, 0, 0, 0, 0],                                             
                    [0, 0, 0, 0, 0, 0, 0, 0],]
    

    testList = newBoard.checkCross(4, 3)


    

    testList1 = newBoard.checkCross(4, 3)




    printMoveList(testList)

    print("for cross:")


    printMoveList(testList1)

    
    newBoard.printBoard()



    




        


