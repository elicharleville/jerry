from __future__ import division
# moves will be composed of one string
# string is parsed to find out what it does

#check(): checks the move
def moveToCoords(mString):

    #coordSet = [[-99,-99],[-99,-99]]
    #test = float(len(mString/2))
    coord1, coord2 = mString[:int(len(mString)/2)],  mString[int(len(mString)/2):]

    nSet1 = strToCoords(coord1)
    nSet2 = strToCoords(coord2)
    #nSet1 = nSet1.append(nSet2)
    coordSet = [[99,99],[99,99]]
    coordSet[0] = nSet1
    coordSet[1] = nSet2



    return coordSet

def boardAdjust(coordSet):

    #switch the coordinates
    # then mirror the y coordinates 


    coordSet[0][0], coordSet[0][1] = coordSet[0][1], coordSet[0][0]
    coordSet[1][0], coordSet[1][1] = coordSet[1][1], coordSet[1][0]
    #print(coordSet)

    if coordSet[0][0] < 4:
        coordSet[0][0] = coordSet[0][0] + (7 - 2 * (coordSet[0][0]))
    elif coordSet[0][0] >= 4:        
        coordSet[0][0] = coordSet[0][0] + (7 - 2 * (coordSet[0][0])) 

    if coordSet[1][0] < 4:
        coordSet[1][0] = coordSet[1][0] + (7 - 2 * (coordSet[1][0]))
    elif coordSet[1][0] >= 4: 
        coordSet[1][0] = coordSet[1][0] + (7 - 2 * (coordSet[1][0])) 

    #print(coordSet)

    return coordSet
        


def strToCoords(cString): #helper method to 
    colC = cString[0]
    rowC = cString[1] #row and col chars inited

    coordSet = [-99, -99]
    error = False

    if colC == 'a':
        coordSet[0] = 0
    elif colC == 'b':
        coordSet[0] = 1
    elif colC == 'c':
        coordSet[0] = 2
    elif colC == 'd':
        coordSet[0] = 3
    elif colC == 'e':
        coordSet[0] = 4
    elif colC == 'f':
        coordSet[0] = 5
    elif colC == 'g':
        coordSet[0] = 6
    elif colC == 'h':
        coordSet[0] = 7
    else:
        error = True
    coordSet[1] = int(rowC)
    coordSet[1] = coordSet[1] - 1

    if coordSet[1] < 0 or coordSet[1] > 7: 
        error = True
    
    if error:
        print("Invalid CoordString")
    else:
        return coordSet
    
    # going to to return 

def retBoardMove(mString): # just combines the above code 
    coordSet = moveToCoords(mString)
    coordSet = boardAdjust(coordSet)
    return coordSet

    

class Move:
    #import board
    def __init__(self, mString):
        self.mString = mString
        self.coordSet = retBoardMove(self.mString)

    #TODO  allow object to be constructed from coordinate set


    def printMove(self): # prints the move
        print(self.mString)




    

if __name__ == "__main__":
    #move = Move("e2e4")
    #move.printMove()

    coordSet = retBoardMove("b7d5")
    print(coordSet)


    







