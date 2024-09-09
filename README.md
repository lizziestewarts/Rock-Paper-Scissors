# Rock Paper Scissors Game (in Python)


## Author
Elizabeth Stewart


## Plan
Decide on the basic features:
- **Two-player mode**: (against the computer).
- **Input validation**: (ensure the user only chooses rock, paper, or scissors).
- **GUI**: Use Tkinter for the graphical interface

### Project structure:
- **main.py**: Contains the game logic and GUI implementation.
- **tests/**: Folder for unit tests.
- **README.md**: This file provides documentation.


## How to Run the Game
1. Clone the repository:
    `git clone https://github.com/yourusername/Rock-Paper-Scissors.git`
    `cd Rock-Paper-Scissors`

2. Run the game: `python main.py`
   If using Python3, use: `python3 main.py`


## How to Run the Tests

### Prerequisites
- **Python 3.x**
- **Tkinter** (comes pre-installed with Python)
- **Pillow (PIL)** for image handling.
- **xvfb** (X virtual framebuffer) for headless GUI testing.

### Installation
1. Install the required Python packages:
    `pip install -r requirements.txt`

2. Install `xvfb` for headless testing:
    `sudo apt-get install -y xvfb`

### Running Tests
To run the tests:
1. For tests that do not require GUI:
    `pytest --ignore=tests/test_play.py`

2. For tests that include GUI components, run:
    `xvfb-run pytest tests/test_play.py`

This uses `xvfb-run` to create a virtual display, allowing GUI tests to run in environments without a display.