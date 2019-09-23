import unittest
import canicas
class TestmyFunctions(unittest.TestCase):
    def testcani(self):
        esperado = [[0], [0], [12], [5], [1], [9]]
        res = canicas.canicas1()
        self.assertEqual(esperado,res)
    def testmul(self):
        a = [[0,1/6,5/6],[1/3,1/2,1/6],[2/3,1/3,0]]
        b = [[1/3,2/3],[2/3,1/3]]
        esperado = [[[0.0, 0.0], [0.0, 0.0]],
                    [[0.06, 0.11], [0.11, 0.06]],
                    [[0.28, 0.56], [0.56, 0.28]],
                    [[0.11, 0.22], [0.22, 0.11]],
                    [[0.17, 0.33], [0.33, 0.17]],
                    [[0.06, 0.11], [0.11, 0.06]],
                    [[0.22, 0.44], [0.44, 0.22]],
                    [[0.11, 0.22], [0.22, 0.11]],
                    [[0.0, 0.0], [0.0 , 0.0]]]
        res = canicas.multiple(a,b)
        self.assertEqual(esperado,res)

        
if __name__ == '__main__':
    unittest.main()
    
