# tests/test_get_user_choice.py

import unittest
from unittest.mock import patch
from main import get_user_choice

class TestGetUserChoice(unittest.TestCase):

    @patch('builtins.input', return_value='rock')
    def test_valid_choice(self, mock_input):
        self.assertEqual(get_user_choice(), 'rock')
    
    @patch('builtins.input', side_effect=['invalid', 'rock'])
    def test_invalid_choice(self, mock_input):
        self.assertEqual(get_user_choice(), 'rock')

if __name__ == '__main__':
    unittest.main()

        