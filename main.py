"""
Rock-Paper-Scissors Game

This is a simple tkinter GUI implementation of the classic Rock-Paper-Scissors game.
Players can compete against the computer by selecting 'rock', 'paper', or 'scissors'.
The game determines the winner based on standard rules and displays the result.

Author: Elizabeth Stewart
Date started: 3/9/24
Last updated: 9/9/24
"""

import tkinter as tk
from PIL import Image, ImageTk
import random  #import random for generating random choices for the computer

def get_computer_choice():
    """
    Randomly select the computer's choice from rock, paper, or scissors.
    Returns:
        str: the computer's choice
    """
    return random.choice(["rock", "paper", "scissors"]) #use random.choice 

def determine_winner(user_choice, computer_choice):
    """
    Determine the winner of the game based on user and computer choices.
    Args:
        user_choice (str): The user's choice ('rock', 'paper', or 'scissors').
        computer_choice (str): The computer's choice ('rock', 'paper', or 'scissors').
    Returns:
        str: message indicating result
    """
    if user_choice == computer_choice:
        return "It's a tie!" #both choice are the same, result is tie
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "scissors" and computer_choice == "paper") or \
        (user_choice == "paper" and computer_choice == "rock"):
        return "You win!" #user's choice beats computer's choice, result is win
    else:
        return "Computer wins!" #computer's choice beats user's choice, result is loss
    

def play(user_choice, result_label):
    """
    Handle game play and update GUI
    """
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"You chose {user_choice}, computer chose {computer_choice}. {result}")


#ensures that the GUI is only created when main.py is run directly, not when imported for testing
if __name__ == "__main__":
    #initialize the Tkinter window only if this script is run directly
    window = tk.Tk()
    window.title("Rock-Paper-Scissors Game")
    window.geometry("600x400")
    window.columnconfigure([0, 1, 2], weight=1)  #make all three columns expand equally
    window.rowconfigure([0, 1], weight=1)  #make the rows expand

    #load images
    rock_img = ImageTk.PhotoImage(Image.open("images/rock.png").resize((100, 100)))
    paper_img = ImageTk.PhotoImage(Image.open("images/paper.png").resize((100, 100)))
    scissors_img = ImageTk.PhotoImage(Image.open("images/scissors.png").resize((100, 100)))

    #create buttons for user choices with images
    rock_button = tk.Button(window, image=rock_img, command=lambda: play('rock', result_label))
    paper_button = tk.Button(window, image=paper_img, command=lambda: play('paper', result_label))
    scissors_button = tk.Button(window, image=scissors_img, command=lambda: play('scissors', result_label))

    #position buttons on the window
    rock_button.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    paper_button.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    scissors_button.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

    #label to display the result
    result_label = tk.Label(window, text="Make your choice!", font=('Arial', 14))
    result_label.grid(row=1, column=0, columnspan=3, sticky="nsew")

    #start GUI loop
    window.mainloop()