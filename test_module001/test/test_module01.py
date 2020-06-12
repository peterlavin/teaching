'''
Created on 7 Sep 2019

@author: peter
'''

import unittest, inspect


def add(x: int, y: int) -> int:
    print("We're in a custom func.: " + inspect.stack()[0][3])
    return x + y

class TestClass01(unittest.TestCase):


    

    def test_case01(self):
        print("\nRunning Test Method : " + inspect.stack()[0][3])
        my_str = "ASHWIN"
        my_int = 999
        self.assertTrue(isinstance(my_str, str))
        self.assertTrue(isinstance(my_int, int))
    
    def test_case02(self):
        print("\nRunning Test Method : " + inspect.stack()[0][3])
        my_pi = 3.14
        self.assertFalse(isinstance(my_pi, int))
    
    def test_case03(self):
        print("\nRunning Test Method : " + inspect.stack()[0][3])
        self.assertEqual(add(2,3), 5)
        

        
if __name__ == '__main__':
    ''' This is the test runner... '''
    unittest.main(verbosity=2)
