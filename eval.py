#Responisble for evaluating a board
import board   
import move

#methods needed for evaluation function:
# number of legal moves
# Doubled pawns
# isolated pawns 
# blocked pawns 
# number of legal moves 
# number of each piece on the board 


#definitions 
P, B, N, R, Q, K = 1, 2, 3, 4, 5, 6
p, b, n, r, q, k = -1, -2, -3, -4, -5, -6

WHITE = 1
BLACK = -1

class Eval:
    def __init__(self, eBoard):
        self.Evalue = None # Evalue is the value of the current position
        self.board = eBoard

    def evaluate(self):
        print()
        


if __name__ == "__main__":
    mainBoard = board.Board(WHITE)
    newEval = Eval(mainBoard)




