import unittest 
from faulty import Faulty
  
class SimpleTest(unittest.TestCase): 
  
    # Returns True or False.  
    
    def test_faulty(self):
        response = Faulty.func_faulty(2)
        with self.assertRaises(TypeError):
            Faulty.func_faulty('ankur')
