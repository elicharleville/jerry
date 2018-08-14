import unittest
import move

class TestBoardAdjust(unittest.TestCase):
    def testBoardAdjust(self):
        testMove1 = "b2d5"
        testCoord1 = move.retBoardMove(testMove1)
        sureCoord1 = [[6,1],[3,3]]

        testMove2 = "c1c7"
        testCoord2 = move.retBoardMove(testMove2)
        sureCoord2 = [[7,2],[1,2]]

        testMove3 = "a6a4"
        testCoord3 = move.retBoardMove(testMove3)
        sureCoord3 = [[2,0],[4,0]]

        testMove4 = "g6e2"
        testCoord4 = move.retBoardMove(testMove4)
        sureCoord4 = [[2,6],[6,4]]



        self.assertEqual(testCoord1, sureCoord1)
        self.assertEqual(testCoord2, sureCoord2)
        self.assertEqual(testCoord3, sureCoord3)
        self.assertEqual(testCoord4, sureCoord4)


if __name__ == '__main__':
    unittest.main()
    

