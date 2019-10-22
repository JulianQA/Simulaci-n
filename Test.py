import unittest
import canicas
class TestmyFunctions(unittest.TestCase):
    def testcani(self):
        a = [[0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 1],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 1, 0]]
        b = [[6],[2],[1],[5],[3],[10]]
        c = 2 
        esperado = [[0],[0],[1],[5],[9],[12]]
        res = canicas.canicas1(a,b,c)
        self.assertEqual(esperado,res)
    def test2(self):
        a = [[0,0,0,0,0,0,0,0],
            [1/2,0,0,0,0,0,0,0],
            [1/2,0,0,0,0,0,0,0],
            [0,1/3,0,1,0,0,0,0],
            [0,1/3,0,0,1,0,0,0],
            [0,1/3,1/3,0,0,1,0,0],
            [0,0,1/3,0,0,0,1,0],
            [0,0,1/3,0,0,0,0,1]]
        b = [[1],[0],[0],[0],[0],[0],[0],[0]]
        c = 2
        esperado = [[0.0], [0.0], [0.0],
                    [0.16666666666666666],
                    [0.16666666666666666],
                    [0.3333333333333333],
                    [0.16666666666666666],
                    [0.16666666666666666]]
        res = canicas.canicas1(a,b,c)
        self.assertEqual(esperado,res)
    def test3(self):
        a = [[(3,1),(2,1)]]
        b = [[(1,2)],[(1,1)]]
        c = 1
        esperado = [[(2, 10)]]
        res = canicas.canicasimag(a,b,c)
        self.assertEqual(esperado,res)
      
if __name__ == '__main__':
    unittest.main()
        
        
