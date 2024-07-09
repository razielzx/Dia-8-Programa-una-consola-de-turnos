import unittest
import change_text


class TryUnitTest(unittest.TestCase):
    
    def test_capitalize(self):
        phrase = "good day"
        result = change_text.caitalize_all(phrase)
        self.assertEqual(result, "GOOD DAY")
        
        

if __name__=="__main__":
    unittest.main()