# Magnetic_Cave
# About this Project
The objective of this project is to develop an AI player for the game 'Magnetic Cave' using the Minimax Algorithm as an adversarial search technique. The Player has 2 options either to play against the  AI opponent automatically, or  play with another human as a 2-Player Game.

# Project Description
Magnetic Cave is a 2-player adversary game where each player tries to build a “bridge” of 5 magnetic bricks within a
cave whose left and right walls are magnetic. For the sake of this project, the bricks of one player will be represented
by a ■ and the bricks of the other by a □. The version of Magnetic Cave that you will implement will be played on a
regular 8x8 chess board.
The rules of the game are simple:
- Initially,thecave(theboard)isempty.
- Player ■ and player □ move in an alternate fashion, starting with ■.So ■ starts, followed by □, then ■ again,
then □ again, ...
- Because there are two big magnets on each side of the cave,a player can only place a brick on an empty cell
of the cave provided that the brick is stacked directly on the left or right wall, or is stacked to the left or the
right of another brick (of any color).
- As soon as one player is able to align 5 consecutive bricks in a row, in a column or in a diagonal, then this
player wins the game.
- If no player is able to achieve a winning configuration and the board is full,then the game stops and there is a tie.

The following figures show possible configurations of the game
![sadsadasd](https://github.com/Rasheed-Al-Qobbaj/Magnetic_Cave/assets/70337488/8889932b-7fad-4153-96e0-98b14252f726)

# Setup 
* install python **>= 3.9** and git
* clone this repository, and move to it

    ```bash
    git clone https://github.com/Rasheed-Al-Qobbaj/Magnetic_Cave.git    
    cd Magnetic_Cave
    ```
* Additionally, make sure you have NumPy installed. NumPy is a Python library used for efficient numerical computations and is a requirement for this program.
  ```
  pip install numpy
  ```


* Open a terminal or command prompt and navigate to the directory where you have cloned or extracted the program files.
* Ensure that you are using a dark-themed terminal to ensure proper display of colors and visual elements in the game. 
* Run the Code, and enjoy the Game!
  ```
  python main.py
  ```


![Screenshot (249)](https://github.com/Rasheed-Al-Qobbaj/Magnetic_Cave/assets/70337488/1a41d37f-512f-45e5-9603-8f48a80f8527)


![Screenshot (251)](https://github.com/Rasheed-Al-Qobbaj/Magnetic_Cave/assets/70337488/cb651ce9-3f07-4400-83f0-0220146f7f81)

![Screenshot (252)](https://github.com/Rasheed-Al-Qobbaj/Magnetic_Cave/assets/70337488/d4e5e557-0e12-43a4-8e65-819e1cd1cb57)

# Documents
> [Project Description](AI_project.pdf)

> [Report](Faris_1200546_Rasheed_1202474.pdf)

# Authors
* [Faris Abufarha](https://github.com/faris771)
* [Rasheed AL Qubbaj](https://github.com/Rasheed-Al-Qobbaj)
    
