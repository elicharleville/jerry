#Responisble for evaluating a board
import board   
import move

#methods needed for evaluation function:
# Doubled pawns
# isolated pawns  
# blocked pawns 
# number of legal moves #
# number of each piece on the board # 


#definitions 
P, B, N, R, Q, K = 1, 2, 3, 4, 5, 6
p, b, n, r, q, k = -1, -2, -3, -4, -5, -6


'''
f(p) = 200(K-K')
       + 9(Q-Q')
       + 5(R-R')
       + 3(B-B' + N-N')
       + 1(P-P')
       - 0.5(D-D' + S-S' + I-I')
       + 0.1(M-M') + ...

KQRBNP = number of kings, queens, rooks, bishops, knights and pawns
D,S,I = doubled, blocked and isolated pawns
M = Mobility (the number of legal moves)


^^^ What i'm going for
'''

WHITE = 1
BLACK = -1

class Eval:
    def __init__(self, eBoard): # Evalue is the value of the current position TODO change this 
        self.board = eBoard
        self.eValue = self.evaluate()

    def evaluate(self):
        wMoveList  = self.board.legalMoves(WHITE, True)
        bMoveList = self.board.legalMoves(BLACK, True)

        wMoveCount = len(wMoveList)
        bMoveCount = len(bMoveList)

        pieceList = self.board.pieceCount()
        dblPawns = self.board.doubledPawns() #TODO need to have these returned values for both sides. 
        blockPawns = self.board.blockedPawns()
        isoPawns  =self.board.isoPawns()

        wKings = pieceList[K]
        bKings = pieceList[K+6]
        wQueens = pieceList[Q]
        bQueens = pieceList[Q+6]
        wRooks = pieceList[R]
        bRooks = pieceList[R+6]
        wBishops = pieceList[B]
        bBishops = pieceList[B+6]
        wKnights = pieceList[N]
        bKnights = pieceList[N+6]
        wPawns = pieceList[P]
        bPawns = pieceList[P+6]


        print("White kings: " + str(wKings))

        eValue = 200 * (wKings - bKings) \
                + 9 * (wQueens - bQueens) \
                + 5 * (wRooks - bRooks) \
                + 3 * ((wBishops- bBishops) + (wKnights - bKnights)) \
                + 1 * (wPawns - bPawns) \
                - 0.5 * ((dblPawns[0] - dblPawns[1]) + (blockPawns[0] - blockPawns[1]) + (isoPawns[0] - isoPawns[1])) \
                + 0.1 * (wMoveCount - bMoveCount)
    
    

        print(200 * (wKings - bKings))
        print(9 * (wQueens - bQueens))
        print(5 * (wRooks - bRooks) )
        print(3 * ((wBishops- bBishops) + (wKnights - bKnights)))
        print(1 * (wPawns - bPawns))
        print(0.5 * ((dblPawns[0] - dblPawns[1]) + (blockPawns[0] - blockPawns[1]) + (isoPawns[0] - isoPawns[1])))
        print( 0.1 * (wMoveCount - bMoveCount))


        return eValue

        


if __name__ == "__main__":
    dPawnArr = [[0, 0, 0, 0, 0, 0, 0, 0],                                           
                [0, 0, 0, 0, 0, 0, 0, 0],                                           
                [0, 0, 0, 0, 0, 0, 0, 0],                                           
                [0, 0, 0, 0, 0, p, 0, 0],                                           
                [0, p, 0, p, 0, p, 0, 0],                                           
                [0, p, 0, p, 0, 0, 0, 0],                                           
                [0, 0, 0, 0, 0, 0, 0, 0],                                             
                [0, 0, 0, 0, 0, 0, 0, 0]]


    mainBoard = board.Board(WHITE, False, dPawnArr)
    newEval = Eval(mainBoard)
    print(newEval.eValue)




