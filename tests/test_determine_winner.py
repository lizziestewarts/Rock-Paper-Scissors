# tests/test_determine_winner.py

import unittest
from main import determine_winner

class TestDetermineWinner(unittest.TestCase):
    
    def test_user_wins(self):
        self.assertEqual(determine_winner('rock', 'scissors'), 'You win!')
    
    def test_computer_wins(self):
        self.assertEqual(determine_winner('scissors', 'rock'), 'Computer wins!')
    
    def test_draw(self):
        self.assertEqual(determine_winner('paper', 'paper'), "It's a tie!")

if __name__ == '__main__':
    unittest.main()
