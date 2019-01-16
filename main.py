from game import Game
from sys import argv
from sys import exit
import board

'''
- This file is responsible for strictly handling I/O
- Parses command line arguments, and will be an interface to change options about the chess computer 
- Interprets any errors spit out by the underlying code being called

-Usage:
    - main.py <depth> <white side> <black side>
    - put "computer" or human in white and black side options
'''


P, B, N, R, Q, K = 1, 2, 3, 4, 5, 6
p, b, n, r, q, k = -1, -2, -3, -4, -5, -6
WHITE = 1
BLACK = -1

def printUsage():
    print("Usage: main.py <depth> <white side> <black side>")
    print("Example: main.py 2 human computer")


if __name__ == "__main__":
    if len(argv) != 4:
        printUsage()
        exit()
    elif argv[2] not in ("human", "computer"):
        printUsage()
        exit()
    elif argv[3] not in ("human", "computer"):
        printUsage()
        exit()
    elif int(argv[1]) < 1:
        printUsage()
        exit()
    usage = False
    depth = int(argv[1])
    whiteSideStr = argv[2]
    blackSiderStr = argv[3]





    if whiteSideStr == "human" or blackSiderStr == "human":
        if whiteSideStr == "human":
            board = board.Board(WHITE)
            game = Game(board)
            game.runHuman(depth, "white")
        else:
            board = board.Board(BLACK)
            game = Game(board)
            game.runHuman(depth, "black")
    
    if whiteSideStr == "computer" and blackSiderStr == "computer":
        board = board.Board(WHITE)
        game = Game(board)
        game.runComp

    



    
    
    

    


