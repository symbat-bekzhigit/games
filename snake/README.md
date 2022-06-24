# Snake game

This is an online simulation of a two-player connection board game where the players take turns dropping their tokens into the 8x8 vertically suspended grid. The pieces fall straight down, occupying the lowest available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own tokens.

**Game specifities**

By default, there are 8 columns named with capital alphabet letters A-G. When the game is launched, the board will be drawn and the players will be randomly assigned checkers which are either X or O. The players will take turns chosing a column, in which case their checkers will be placed in the lowest available space within the column.

There is a error check for the various types of invalid input from the player side that will ensure that the column their entering matches the ones that are displayed on the board. The player's entry should be in the format "column name" i.e. A.

Players will keep entering the column until either one of them wins or the game results in a draw.

The player who successfully places 4 checkers horizontally, vertically or diagonally wins. The draw occurs when the board gets filled before either player achieves 4 checkers in a row.

The logic behind checking if the player won is that every time the player places his/her checker in the specific column, first we place the checker in the lowest available location in that column, and then check if there are 4 same checkers to the right, left, up, down, diagonally up and right, diagonally up and left, diagonally down and right, diagonally down and right of the chosen coordinate, inlcuding the coordinate where player just placed his/her checker.

Here's the link to the video recording of my game: https://youtu.be/mvKUmYcDO7c
