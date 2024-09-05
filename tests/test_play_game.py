# tests/test_play_game.py

import unittest
from unittest.mock import patch
from main import play_game

class TestPlayGame(unittest.TestCase):
    
    @patch('main.get_user_choice', return_value='rock')
    @patch('main.get_computer_choice', return_value='scissors')
    def test_play_game(self, mock_user_choice, mock_computer_choice):
        #test the play_game function to ensure it correctly identifies the winner
        with patch('builtins.print') as mock_print:
            play_game()
            mock_print.assert_any_call('User wins!')

if __name__ == '__main__':
    unittest.main()
