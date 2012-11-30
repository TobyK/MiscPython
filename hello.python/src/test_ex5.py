'''
Created on 16/11/2012

@author: Toby
'''
import unittest
import ex_5

class Test(unittest.TestCase):


    def test_do_plus(self):
        ex_5.do_plus(3,8)
        
        self.assertEqual(0, ex_5.do_plus(0, 0), "do_plus() returns wrong result")
        self.assertEqual(11, ex_5.do_plus(3,8), "do_plus() returns wrong result")
        self.assertEqual(11, ex_5.do_plus(8,3), "do_plus() returns wrong result")        
        pass

    def test_do_plus_strings(self):
        self.assertEqual("Hi There", ex_5.do_plus("Hi", "There"), "do__plus() returns wrong result")

    def test_do_plus_mixed(self):
        self.assertEqual("hi5", ex_5.do_plus("hi", 5), "Could not add a text to an int")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()