import board
import move
import evaluate

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



'''
What I'm going for: 
int maxi( int depth ) {
    if ( depth == 0 ) return evaluate();
    int max = -oo;
    for ( all moves) {
        score = mini( depth - 1 );
        if( score > max )
            max = score;
    }
    return max;
}

int mini( int depth ) {
    if ( depth == 0 ) return -evaluate();
    int min = +oo;
    for ( all moves) {
        score = maxi( depth - 1 );
        if( score < min )
            min = score;
    }
    return min;
}
'''
# definitions

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
    
    
    def negaMax(self, depth, color):
        if depth == 0:
            return color * evaluate.evaluate(self.board) # TODO still need to return move obj.
        bestMove = -9999
        moveList = self.board.legalMoves()
        for move in moveList: 
            self.makeMove(move)
            bestMove = max(bestMove, -self.negaMax(depth - 1, -color))
            self.undo()
        return bestMove 

    def run(self):
        print()

    def makeMove(self, move): # takes in move object 
        piece = self.board.board[move.coordSet[0][0]][move.coordSet[0][1]] 
        self.board.board[move.coordSet[0][0]][move.coordSet[0][1]] = 0 # set orig place to empty
        move.defeated = self.board.board[move.coordSet[1][0]][move.coordSet[1][1]]
        self.board.board[move.coordSet[1][0]][move.coordSet[1][1]] = piece 
        self.moveStack.append(move)
    
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
    newGame.undo()


    

    newGame.gameState()