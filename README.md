# Simulation
It is a library which consists of a simulation of quantum probability calculations. Which consists of the probability of the marbles being on one side or the other after a certain time (click), also the probability in a multiple slit calculation, the experiments of multiple probabilistic classic slits, with more than two slits and multiple multiple slits

# How does it work?
It is a Python library, to use it you have to download the .py file called 'Canicas.py' on your PC, it is based on functions which resolve the points mentioned above. Some need parameters, others just need to change the value of the variables you need. Returns matrices, vectors or values as the case may be.
# Examples
```python
def canicas1(m1,v1,clicks): #receive the boolean matrix, the probability vector and the clicks.

    res = multi(m1,m1) #call the function that does the multiplication between the matrix and the vector
    clicks -= 1
    while clicks > 0: #does the multiplication so many clicks have been entered
        res = multi(res,m1)
        clicks -= 1
    
    return multi(res,v1) #returns the probability vector after so many clicks
```
# Test
If you need to test your results, you must download the .py file called 'Test.py'. The files 'Canicas.py' and 'Test.py' must be in the same folder so that it can be executed correctly. Example of how it should be done:
```python

import unittest
import canicas
class TestmyFunctions(unittest.TestCase):
    def testcani(self):
        a = [[0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 1],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 1, 0]] #the boolean matrix that will operate.
        b = [[6],[2],[1],[5],[3],[10]] #the vector that will operate.
        c = 2                        #the clicks you want
        esperado = [[0],[0],[1],[5],[9],[12]] #the result you expect to get
        res = canicas.canicas1(a,b,c) # the result that the function gives
        self.assertEqual(esperado,res)
if __name__ == '__main__':
    unittest.main() 
               
    #############################
    
    In the Python console you should see:
    ..............................
    Ran 1 tests in (your time)s

    OK
    ..............................
    else, should correct the error
```        
