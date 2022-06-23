# Battleship game

This is a simple simulation of a battleship game where the player's goal is to locate the whole boat's location by randomly choosing the coordinates from the 8x8 board.

**Game specifities**

When the game is launched, the board will be drawn and location of the boat will be chosen randomly. Since the boat will extend for the length 4 cells, the location of the boat will be based on the initial cell and the orientation that the boat will take with respect to that cell(left/right/up/down). 
Both the inital cell and orientation will be chosen randomly.

The player will keep guessing the cells until finding the location of all 4 cells of the boat.

The player's entry should be in the format column+row (i.e. A2). If the player enters location of the cell in the incorrect format, he/she will be asked to enter it again and the game will continue.

If the location that the player chooses doesn't have a boat, a hash (#) will be drawn on that cell, otherwise - a checker (X).

An auxiliary board that stores the boat and an original boat that the player sees are used to compare the player's input with the location of the boat.

Once the player locates all the 4 cells of the boat, the game will be finished and the final score (which corresponds to the total number of guesses that the player made) will be printed.

***
![](bin/data/1.png)
![](bin/data/2.png)
