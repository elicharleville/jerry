import numpy #prolly not needed
from enum import Enum
from pprint import pprint

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

class Board:
    def __init__(self):
        #from move import Move
        self.nextTurn = WHITE  
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
        print()
    def getQueenMoves(self, row, col):
        print()
    def getKingMoves(self, row, col):
        print()

#test code/ main
if __name__ == "__main__":
    newBoard = Board()
    

    
    newBoard.printBoard()



    




        


