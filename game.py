import board
import move
import evaluate
import time
import collections 

'''
-This class will primarily be responsible for tracking the board state of a game as its played.
-It will also contain the minmax function for picking the best move

-makeMove()
    - changes board state
    - should spit out  errors

-MMDriver()- Driver that handles the picking of a move from a boardState
-Max() - should return a move
-Min() - should return a move
-Run function()
    -Runs everything about a game. 
    -1. move made
    -2. Response move 
    -3. if Check is in place on board state:
        - check for mate

-objs: 
    - Board 
    - Arrays for storing potential board states? 
'''
# definitions

#moveTuple = collections.namedtuple('moveTuple', ['moveValue', 'move'])

P, B, N, R, Q, K = 1, 2, 3, 4, 5, 6
p, b, n, r, q, k = -1, -2, -3, -4, -5, -6
WHITE = 1
BLACK = -1

class Game:
    def __init__(self, board):
        self.board = board # need to keep track of next move
        self.moveStack = []
    
    def gameState(self):
        self.board.printBoard()

    def negaMax(self, depth, color, move):
        if depth == 0:
            move.eValue = color * evaluate.evaluate(self.board)
            print(color * evaluate.evaluate(self.board))
            return move # TODO still need to return move obj.
        bestMove = move
        moveList = self.board.legalMoves(color, True)
        for move in moveList: 
            self.makeMove(move)

            print()
            print("depth: " + str(depth))
            print("move: " + str(move.mString))
            self.gameState()
            print() 
            #bestMove = max(bestMove, -self.negaMax(depth - 1, -color, move).eValue)

            testMove = self.negaMax(depth - 1, -color, move)
            testMove.eValue *= -1
            if testMove.eValue > bestMove.eValue:
                bestMove = testMove

            #print(color)
            #print(move.mString)
            #print(bestMove)
            self.undo()
        return bestMove

    def run(self): #TODO 
        print()

    def makeMove(self, move): # takes in move object 
        piece = self.board.board[move.coordSet[0][0]][move.coordSet[0][1]] 
        self.board.board[move.coordSet[0][0]][move.coordSet[0][1]] = 0 # set orig place to empty
        move.defeated = self.board.board[move.coordSet[1][0]][move.coordSet[1][1]]
        self.board.board[move.coordSet[1][0]][move.coordSet[1][1]] = piece 
        self.moveStack.append(move) 
        #TODO  Make move needs to change board.nextTurn 
    
    def undo(self):
        move = self.moveStack.pop() #problem: have to remember what was there in the first place 
        piece = self.board.board[move.coordSet[1][0]][move.coordSet[1][1]] 
        self.board.board[move.coordSet[0][0]][move.coordSet[0][1]] = piece 
        self.board.board[move.coordSet[1][0]][move.coordSet[1][1]] = move.defeated 

if __name__ == "__main__":    
    board = board.Board(WHITE)
    move = move.Move("g1f3")
    newGame = Game(board)
    newGame.makeMove(move)
    #testing undo
    #newGame.undo()
    start = time.time()

    
    moveScore = newGame.negaMax(2, WHITE, move)


    end = time.time()

    print()
    #print("move Score: ")
    print(moveScore.mString)
    #print(end - start)
    

    newGame.gameState()