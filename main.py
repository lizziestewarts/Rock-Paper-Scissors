"""
Rock-Paper-Scissors Game

This is a simple command-line implementation of the classic Rock-Paper-Scissors game.
Players can compete against the computer by selecting 'rock', 'paper', or 'scissors'.
The game determines the winner based on standard rules and displays the result.

Author: Elizabeth Stewart
Date started: 3/9/24
Last updated: 3/9/24
"""

import random  #import random for generating random choices for the computer

def get_user_choice():
    """
    Get user's choice of rock, paper, or scissors.
    Returns:
        str: user's choice (needs to be 'rock', 'paper', or )
    """
    user_input = input("Enter rock, paper, scissors: ").lower() #convert input to lowercase to handle case sensitivity
    if user_input in ["rock", "paper", "scissors"]:
        return user_input #valid input
    else:
        print("Invalid input. Try again.")
        return get_user_choice() #recursive call until valid input

def get_computer_choice():
    """
    Randomly select the computer's choice from rock, paper, or scissors.
    Returns:
        str: the computer's choice
    """
    return random.choice(["rock", "paper", "scissors"]) #use random.choice 

def play_game():
    """
    Main game loop
    """
    user_choice = get_user_choice() #get user's choice
    computer_choice = get_computer_choice() #get computer's choice

if __name__ == "__main__":
    play_game() #run game if this file is executed directly