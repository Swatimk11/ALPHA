# test_analyzer.py

import unittest
from analyzer import count_lines_of_code

class TestLegacyCodeAnalyzer(unittest.TestCase):
    def test_count_lines_of_code(self):
        self.assertEqual(count_lines_of_code('sample_file.txt'), 67)

        # Test file not found scenario
        self.assertEqual(count_lines_of_code('non_existent_file.txt'), -1)

if _name_ == '_main_':
    unittest.main()
