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
        play('rock', result_label)
        
        #check if the result label text was updated correctly
        self.assertIn("You chose rock", result_label.cget("text"))
        self.assertIn("computer chose", result_label.cget("text"))


if __name__ == "__main__":
    unittest.main()
