import unittest
from main import determine_winner

class TestDetermineWinner(unittest.TestCase):
    def test_determine_winner(self):
        #test different outcomes
        self.assertEqual(determine_winner('rock', 'scissors'), "You win!")
        self.assertEqual(determine_winner('scissors', 'paper'), "You win!")
        self.assertEqual(determine_winner('paper', 'rock'), "You win!")
        self.assertEqual(determine_winner('rock', 'rock'), "It's a tie!")
        self.assertEqual(determine_winner('scissors', 'scissors'), "It's a tie!")
        self.assertEqual(determine_winner('paper', 'paper'), "It's a tie!")
        self.assertEqual(determine_winner('rock', 'paper'), "Computer wins!")
        self.assertEqual(determine_winner('scissors', 'rock'), "Computer wins!")
        self.assertEqual(determine_winner('paper', 'scissors'), "Computer wins!")

if __name__ == "__main__":
    unittest.main()
