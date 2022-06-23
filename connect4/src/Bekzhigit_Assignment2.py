import random
import os


NUM_ROWS = 6
NUM_COLS = 7
checkers = [' X ',' O ',' V ',' H ',' M ']
players = []
board = []
count=[]
PLAYERS_NUM = 2

#the constant variable which will be later used to check if the coordinate is empty or not
EMPTY = '   '


#a function which will print the board and the board labels every time it will be called 
def print_board():
    for cols in range(NUM_COLS):
        print('  '+chr(cols+65),end=' ')
        
    print("\n+"+"---+"*NUM_COLS)
    
    for row in range(NUM_ROWS):
        print('|',end='')
        for col in range(NUM_COLS):
            print(board[row][col]+'|',end='')
        print("\n+"+"---+"*NUM_COLS)

    
    
#Player 1 will play with the checker X,player 2 - O,player 3 - V, player 4 - H, player 5 - M    
for p in range(PLAYERS_NUM):
    players.append(checkers[p])
    #fill the list "count" with 0 and ensures that this list has the same number of elements as the number of the players;
    #in this list,later on, we will store the "counter" for each of the players which will help us check if the player won or not
    count.append(0)

#randomly select the first player
first_player=random.choice(players)

#change the order of the elements in the list "players", so that the randomly chosen player will start first
if first_player!=players[0]:
    players.remove(first_player)
    players.insert(0,first_player)


print("Players that will be playing this game are:",",".join(players),"\nThe player",first_player,"will start the game")
print("Please, take turns by placing your checker in a column of your choice, indicated by a letter(e.g. A)")

#create a board with given dimensions
for row in range(NUM_ROWS):
    row_list=[]
    for col in range(NUM_COLS):
        row_list.append('   ')
    board.append(row_list)

print_board()



coordinates_filled=0
counter = 0
win = False

#players will keep entering the column until either one of them wins or the game results in a draw
while win==False:

    #this for loop will ensure that the turns are being alternated
    for p in range(PLAYERS_NUM):

        check = False

        #checks for all the types of invalid input
        #if the player provides an invalid input, the player will be asked to provide another input until the input is valid(the turn is not lost)
        while check==False:
            print("Player", players[p],end=" ")
            z = input(",please choose the column: ")
            
            if z.isalpha==False or len(z)!=1:
                print("Invalid input.Please, try again.")
                continue
            elif ord(z)-65>=NUM_COLS or ord(z)-65<0:
                print("Invalid input.Please, try again.")
                continue
            
            #if the input is valid, the program will exit this loop and the remaining part of the code will be executed   
            else:
                c=ord(z)
                check=True
                

 
           
        #since we sholud place the checkers in the lowest available space within the column,we will start from the bottom of the board and will move up
        for r in range(NUM_ROWS - 1, -1, -1):

            #this part of the code will be executed when the player places the checker in the lowest row
            if(board[r][c-65] == EMPTY):
                board[r][c-65] = players[p]

                #coordinates_filled will keep count of the number of coordinates that are filled with checkers
                coordinates_filled+=1
                
                #this loop checks if there are 4 same checkers to the right of the chosen coordinate 
                for col in range(c-65,c-65+4):
                    
                    #ensures that we will stay within the board dimensions while checking those 4 coordinates
                    if col<NUM_COLS and col>-1:
                        if board[r][col]==players[p]:
                            counter+=1

                            #if there are 4 same checkers located in the direction specified above, the player who placed those checkers will win
                            if counter==4:
                                win=True
                                break
                    else:
                        break

                        
                #we should update the counter's value to 0 every time we finish checking in certain direction
                counter=0
                
                #checks if there are 4 same checkers to the left of the chosen coordinate
                for col in range(c-65,c-65-4,-1):
                    if col<NUM_COLS and col>-1:
                        if board[r][col]==players[p]:
                            counter+=1
                            if counter==4:
                                win=True
                                break
                    else:
                        break
                        
                counter=0

                #checks if there are 4 same checkers located diagonally left from the chosen coordinate(in downward direction)
                for k in range(0,4):
                    if c-65-k<NUM_COLS and c-65-k>-1 and r+k<NUM_ROWS and r+k>-1:
                        if board[r+k][c-65-k]==players[p]:
                            counter+=1
                            if counter==4:
                                win=True
                                break
                    else:
                        break
                    
                    
                counter=0

                #checks if there are 4 same checkers located diagonally left from the chosen coordinate(in upward direction)
                for k in range(0,4):
                    if c-65-k<NUM_COLS and c-65-k>-1 and r-k<NUM_ROWS and r-k>-1:
                        if board[r-k][c-65-k]==players[p]:
                            counter+=1
                            if counter==4:
                                win=True
                                break
                    else:
                        break
                    
                    
                counter=0

                #checks if there are 4 same checkers located diagonally right from the chosen coordinate(in downward direction)
                for k in range(0,4):
                    if c-65+k<NUM_COLS and c-65+k>-1 and r+k<NUM_ROWS and r+k>-1:
                        if board[r+k][c-65+k]==players[p]:
                            counter+=1
                            if counter==4:
                                win=True
                                break
                    else:
                        break
                    
            
                counter=0

                #checks if there are 4 same checkers located diagonally right from the chosen coordinate(in upward direction)
                for k in range(0,4):
                    if c-65+k<NUM_COLS and c-65+k>-1 and r-k<NUM_ROWS and r-k>-1:
                        if board[r-k][c-65+k]==players[p]:
                            counter+=1
                            if counter==4:
                                win=True
                                break
                    else:
                        break

            
                counter=0

              
                break

            

            #this part of the code will be executed when the player places the checker in the column which already has at least one checker
            elif(board[r][c-65] != EMPTY):

                #if the player places the checker in the column which is already completely filled, the player will lose his/her turn
                if(r-1==-1):
                    print("\nThis column is already completely filled with checkers.Thus the turn is invalid and you lose your turn.\n")
                    break

               #if the row, which is located above "the already occupied" coordinate, is empty, we will place the checker there 
                elif(board[r-1][c-65] == EMPTY):
                    board[r-1][c-65] = players[p]
                    coordinates_filled+=1

                    #the similar logic is used here as in the above part of the code
                    #checks if there are 4 same checkers located vertically down
                    for row in range(r-1,r+3):
                        if row<NUM_ROWS:
                            if board[row][c-65]==players[p]:
                                counter+=1
                                if counter==4:
                                    win=True
                                    break
                        else:
                            break
                    
                    counter=0
                    
                    #checks if there are 4 same checkers to the right of the chosen coordinate
                    for col in range(c-65,c-65+4):
                        if col<NUM_ROWS and col>-1:
                            if board[r-1][col]==players[p]:
                                counter+=1
                                if counter==4:
                                    win=True
                                    break
                        else:
                            break
                        
                    counter=0

                    #checks if there are 4 same checkers to the left of the chosen coordinate
                    for col in range(c-65,c-65-4,-1):
                        if col<NUM_ROWS and col>-1:
                            if board[r-1][col]==players[p]:
                                counter+=1
                                if counter==4:
                                    win=True
                                    break
                        else:
                            break
                        
                    counter=0

                    
                    #checks if there are 4 same checkers located diagonally left from the chosen coordinate(in downward direction)
                    for k in range(0,4):
                        if c-65-k<NUM_COLS and c-65-k>-1 and r-1+k<NUM_ROWS and r-1+k>-1:
                            if board[r-1+k][c-65-k]==players[p]:
                                counter+=1
                                if counter==4:
                                    win=True
                                    break
                        else:
                            break


                    counter=0

                    #checks if there are 4 same checkers located diagonally left from the chosen coordinate(checks in upward direction)
                    for k in range(0,4):
                        if c-65-k<NUM_COLS and c-65-k>-1 and r-1-k<NUM_ROWS and r-1-k>-1:
                            if board[r-1-k][c-65-k]==players[p]:
                                counter+=1
                                if counter==4:
                                    win=True
                                    break
                        else:
                            break


                    counter=0

                    #checks if there are 4 same checkers located diagonally right from the chosen coordinate(checks in downward direction)
                    for k in range(0,4):
                        if c-65+k<NUM_COLS and c-65+k>-1 and r-1+k<NUM_ROWS and r-1+k>-1:
                            if board[r-1+k][c-65+k]==players[p]:
                                counter+=1
                                if counter==4:
                                    win=True
                                    break
                        else:
                            break


                    counter=0

                    #checks if there are 4 same checkers located diagonally right from the chosen coordinate(checks in upward direction)
                    for k in range(0,4):
                        if c-65+k<NUM_COLS and c-65+k>-1 and r-1-k<NUM_ROWS and r-1-k>-1:
                            if board[r-1-k][c-65+k]==players[p]:
                                counter+=1
                                if counter==4:
                                    win=True
                                    break
                        else:
                            break

                    counter=0
                    
                    break
                else:
                    continue
            
            
       
        #if the board gets filled before either player achieves 4 checkers in a row, the game will be a draw and it will end
        if coordinates_filled==NUM_ROWS*NUM_COLS:
            print_board()
            print("The board is already completely filled with checkers and no one has won yet. Therefore the game is a draw.")
            win=True
            break


        #after every turn, the board is checked for a possible win
        #if one player successfully places 4 checkers horizontally, vertically or diagonally, that player wins and the game will end
        elif win==True:
            print_board()
            print("Player",players[p],"won! Congratulations!")
            break
        

        #after every turn,the board will be printed
        os.system('clear')
        print_board()

       
