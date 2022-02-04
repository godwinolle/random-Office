from tokenize import String
import unittest;

from theOffice import optionFour, optionOne, optionThree, optionTwo

class TestTheOffice(unittest.TestCase):
    def testOption1(self):
        self.assertTrue(type(optionOne), String)

    def testOption2(self):
        self.assertTrue(type(optionTwo), String)
    
    def testOption3(self):
        self.assertTrue(type(optionThree), String)
    
    def testOption4(self):
        self.assertTrue(type(optionFour), String)


if __name__ == '__main__':
    unittest.main()