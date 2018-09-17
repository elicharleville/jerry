#Responisble for evaluating a board
import board   
import move



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
        


if __name__ == "__main__":
    mainBoard = board.Board(WHITE)
    newEval = Eval(mainBoard)




