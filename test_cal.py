import unittest
import calc2


class palash_test_case(unittest.TestCase):
   
    def test_add(self):
        result =calc2.add(10,5)
        self.assertEqual(result,15)
        

    def test_subtract(self):
        result =calc2.subtract(10,5)
        self.assertEqual(result,5)
           
    def test_multiply(self):
        result =calc2.multiply(10,5)
        self.assertEqual(result,50)
        
   
    def test_divide(self):
        result =calc2.divide(10,5)
        self.assertEqual(result,2)
        
    
    
if __name__ == '__main__':
 unittest.main()