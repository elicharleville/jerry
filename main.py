from game import Game
from sys import argv
from sys import exit
'''
- This file is responsible for strictly handling I/O
- Parses command line arguments, and will be an interface to change options about the chess computer 
- Interprets any errors spit out by the underlying code being called

-Usage:
    - main.py <depth> <white side> <black side>
    - put "computer" or human in white and black side options
'''

def printUsage():
    print("Usage: main.py <depth> <white side> <black side>")


if __name__ == "__main__":
    usage = False
    depth = int(argv[1])
    whiteSideStr = argv[2]
    blackSiderStr = argv[3]

    if len(argv) != 4:
        usage = True
    if whiteSideStr not in ("human", "computer"):
        usage = True
    if blackSiderStr not in ("human", "computer"):
        usage = True
    if not isinstance(depth, int):
        usage = True
    if depth < 1:
        usage = True

    if usage:
        printUsage()
        exit()

    
    

    


