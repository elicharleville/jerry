#from __future__ import division
# moves will be composed of one string
# string is parsed to find out what it does

#check(): checks the move


#TODO consider adding coordsT
def moveToCoords(mString): # converts string to list coordinate 

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

def numToLetter(num):
    if num == 0:
        return 'a'
    elif num == 1:
        return 'b'
    elif num == 2:
        return 'c'
    elif num == 3:
        return 'd'
    elif num == 4:
        return 'e'
    elif num == 5:
        return 'f'
    elif num == 6:
        return 'g'
    elif num == 7:
        return 'h'

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
        


def strToCoords(cString): #helper method to swtich a string to coords 
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
    def __init__(self, move, promote=None):
        self.promotion = False
        if isinstance(move, str):
            self.mString = move
            self.coordSet = retBoardMove(self.mString)
        elif isinstance(move, list):
            self.coordSet = move
            self.mString = self.coordsToMove()
        if promote is None: self.promotion = False
        else: self.promotion = promote
        self.eValue = -9999.9 # TODO  can be cleaner 
        self.defeated = None # if a piece is taken, this is where its stored

    def printMove(self):  # prints the move
        print(self.mString)

    def promote(self):  # sets the promotion bool to true
        self.promotion = True

    def coordsToMove(self):
        #coord1 = coord[0]
        #coord2 = coord[1]
        #ex: [[4, 3], [2, 3]]
        char1 = numToLetter(self.coordSet[0][1])
        char2 = numToLetter(self.coordSet[1][1])

        num1 = self.coordSet[0][0]
        num2 = self.coordSet[1][0]

        num1 = 8 - num1
        num2 = 8 - num2

        mString = char1 + str(num1) + char2 + str(num2)

        if self.promotion == True:
            mString += " --> Q"
            return mString
        else:
            return mString

if __name__ == "__main__":

    coordSet = retBoardMove("b7d5")

    move = Move(coordSet, True)

    print(move.promotion)
    print(move.coordSet)
