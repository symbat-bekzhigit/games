import random
import os


SHIP_SIZE = 4
DIMENSION = 10
CHECKER = ' X '
DASH = ' # '
board = []

#///////////////////
#create a board with given dimensions(this board will be shown to the reader)
for row in range(DIMENSION):
    row_list=[]
    for col in range(DIMENSION):
        row_list.append('   ')
    board.append(row_list)
    
#create a copy of the above board which will store the location of the ship(this board will be hidden from the reader)
board_2 = [i.copy() for i in board]

#print the board and the board labels
for cols in range(DIMENSION):
    #in order to change 0,1,2,...,9 order to A,B,C,...,H, 65 is added to the cols, then the final decimal is converted to its corresponding ASCII value
    print('   '+chr(cols+65),end='')

print("\n +"+"---+"*DIMENSION)

for row in range(DIMENSION):
    print(str(row)+'|',end='')
    for col in range(DIMENSION):
        print(board[row][col]+'|',end='')
    print("\n +"+"---+"*DIMENSION)

'''create a random integer to define the direction in which the board extends
0 - board extends horizontally right, 1 - horizontally left, 2 - vertically up, 3 - vertically down'''
first_cell_orient = random.randint(0,3)

#placing the ship in the random position and setting column and row restrictions for the case when the ship extends horizontally right
if first_cell_orient == 0:
    first_cell_col = random.randint(65,71)
    first_cell_row = random.randint(0,9)
    
    '''the below code can be used to print the coordinates and direction of the cell where the ship is randomly placed:
    print(chr(first_cell_col)+str(first_cell_row),str(first_cell_orient))'''
    
    for col in range(SHIP_SIZE):
        board_2[first_cell_row][first_cell_col-65+col] = CHECKER
        
#placing the ship in the random position and setting column and row restrictions for the case when the ship extends horizontally left
elif first_cell_orient == 1:
    first_cell_col = random.randint(68,74)
    first_cell_row = random.randint(0,9)

    for col in range(SHIP_SIZE):
        board_2[first_cell_row][first_cell_col-65-col] = CHECKER

#placing the ship in the random position and setting column and row restrictions for the case when the ship extends vertically up       
elif first_cell_orient == 2:
    first_cell_col = random.randint(65,74)
    first_cell_row = random.randint(3,9)
    
    for row in range(SHIP_SIZE):
        board_2[first_cell_row-row][first_cell_col-65] = CHECKER

#placing the ship in the random position and setting column and row restrictions for the case when the ship extends horizontally down
elif first_cell_orient == 3:
    first_cell_col = random.randint(65,74)
    first_cell_row = random.randint(0,6)
    
    for row in range(SHIP_SIZE):
        board_2[first_cell_row+row][first_cell_col-65] = CHECKER


count_hit = 0
count_guess = 0


#user has 100 chances to find the location of the ship(100 because there are overall 10*10 cells)
while count_guess != 100:
    guess = input("Please,enter your guess in the following format(column+row, e.g.A2): ")
    os.system("clear")

    #checking for invalid input such as AB,1A,A 6,32,A;5 etc.
    if (guess[0].isalpha())==False or (guess[1:].isdigit())==False:
       print("Invalid data.Please,try again")
       continue

    #splitting column and row of the input, and converting it to integer
    guess_col = ord(guess[0])-65
    guess_row = int(guess[1:])

    #checking that the inputted coordinate is within the dimensions of the board
    if 9<guess_col or guess_col<0 :
        print("Column is out of range.Please,try again")
        continue
    elif 9<guess_row or guess_row<0 :
        print("Row is out of range.Please,try again")
        continue

    else:
      
        #if the player choses one of the cells where the ship is located this code will be executed
        if(board_2[guess_row][guess_col] == CHECKER):
            
            #checking for the repetitive guesses of the same cell
            if(board[guess_row][guess_col] == CHECKER):
                print("You have already chosen this coordinate. Please,try again")
                continue

            #placing 'x' if the guess was right   
            else:
                board[guess_row][guess_col] = CHECKER

                #keeping count of how many times a player hits the right cell
                count_hit = count_hit + 1
                
                #counting the number of guesses that the player makes in order to calculate the final score
                count_guess = count_guess + 1

        #if the player fails to chose one of the cells where the ship is located this code will be executed
        else:
            
            #checking for the repetitive guesses of the same cell
            if(board[guess_row][guess_col] == DASH):
                print("You have already chosen this coordinate. Please,try again")
                continue

            #placing '#' if the guess was wrong   
            else:
                board[guess_row][guess_col] = DASH

                #even though the guess was wrong, this attempt will be counted towards the total number of guesses
                count_guess = count_guess + 1

        #the screen is cleared before printing the updated board
        os.system("clear")

        #printing the updated board
        for cols in range(DIMENSION):
            print('   '+chr(cols+65),end='')

        print("\n +"+"---+"*DIMENSION)

        for row in range(DIMENSION):
            print(str(row)+'|',end='')
            for col in range(DIMENSION):
                print(board[row][col]+'|',end='')
            print("\n +"+"---+"*DIMENSION)

    #after each turn the program checks if the game is won
    #if the player finds all 4 cells of the ship the game will be terminated and the final score will be printed     
    if count_hit == 4:
        print("Game is over!\nYour score is:",count_guess)
        break





