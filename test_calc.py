import unittest
import calc


class testCalc(unittest.Testcase):
    def test_sum(self):
        result= calc.sum(num_1=5, num_2=10)
        self.assertequal(result,15)
  
    def test_divide(self):
        result= calc.divide(num_1=10,num_2=2)
        self.assertequal(result,5)
    
    def test_multiply(self):
        result= calc.multiply(num_1=5,num_2=2)
        self.assertequal(result,10)
        