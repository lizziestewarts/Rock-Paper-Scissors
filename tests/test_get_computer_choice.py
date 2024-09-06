import unittest
from unittest.mock import patch
from main import get_computer_choice

class TestGetComputerChoice(unittest.TestCase):
    @patch('random.choice', return_value='rock')
    def test_get_computer_choice(self, mock_random_choice):
        #test the computer's choice is correctly chosen
        self.assertEqual(get_computer_choice(), 'rock')
        mock_random_choice.assert_called_once_with(["rock", "paper", "scissors"])

if __name__ == "__main__":
    unittest.main()
