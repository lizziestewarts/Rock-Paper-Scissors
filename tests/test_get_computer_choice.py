# tests/test_get_computer_choice.py

import unittest
from main import get_computer_choice

class TestGetComputerChoice(unittest.TestCase):
    
    def test_computer_choice(self):
        choices = ['rock', 'paper', 'scissors']
        computer_choice = get_computer_choice()
        self.assertIn(computer_choice, choices)

if __name__ == '__main__':
    unittest.main()
