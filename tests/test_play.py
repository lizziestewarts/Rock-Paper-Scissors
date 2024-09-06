import unittest
import tkinter as tk
from main import play

class TestPlayFunction(unittest.TestCase):
    def test_play_function_updates_result_label(self):
        #set up the main window for testing GUI
        window = tk.Tk()
        window.geometry("600x400")
        result_label = tk.Label(window, text="Make your choice!")
        result_label.grid(row=1, column=0, columnspan=3, sticky="nsew")

        #patch the play function to test GUI updates
        play('rock')
        
        #verify if result_label is updated correctly (since computer_choice is random, the check is general)
        self.assertIn(result_label.cget("text"), [
            "You chose rock, computer chose rock. It's a tie!",
            "You chose rock, computer chose paper. Computer wins!",
            "You chose rock, computer chose scissors. You win!"
        ])
        
        window.destroy()  #close the window after test

if __name__ == "__main__":
    unittest.main()
