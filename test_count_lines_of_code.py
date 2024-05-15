import unittest
from analyzer import count_lines_of_code

class TestLegacyCodeAnalyzer(unittest.TestCase):
    def test_count_lines_of_code(self):
        actual_lines = count_lines_of_code('sample_file.txt')
        print("Actual number of lines:", actual_lines)  # Add this line for debugging
        self.assertEqual(actual_lines, 300)

if _name_ == '_main_':
    unittest.main()
