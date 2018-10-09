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

# definitions

P, B, N, R, Q, K = 1, 2, 3, 4, 5, 6
p, b, n, r, q, k = -1, -2, -3, -4, -5, -6
WHITE = 1
BLACK = -1

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

class Game:
    def __init__(self, board):
        self.board = board # need to keep track of next move 
    
    def MMDriver(self):
        print()

    
    def run(self):
        print()

    def makeMove(self, move): # takes in move object 
        piece = self.board.board[move.coordSet[0][0]][move.coordSet[0][1]] 
        self.board.board[move.coordSet[0][0]][move.coordSet[0][1]] = 0 # set orig place to empty
        self.board.board[move.coordSet[1][0]][move.coordSet[1][1]] = piece 


if __name__ == "__main__":
    board = board.Board(WHITE)
    move = move.Move("g1f3")
    newGame = Game(board)
    newGame.makeMove(move)

    newGame.board.printBoard()