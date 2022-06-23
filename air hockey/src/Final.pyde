add_library('minim')

path = os.getcwd()
player = Minim(this)

RES_W = 1000
RES_H = 500

disk_speed_x = 1.75
disk_speed_y = 1.75
disk_w = 45
disk_h = 45

disk_xc = RES_W/2
disk_yc = RES_H/2
BORDER=20

score_player1 = 0
score_player2 = 0

game_over = False
game_start = True
switch_round = False

round_number = 1
winning_player = 0
num_wins_player1 = 0
num_wins_player2 = 0

        
paddle_left_x = 40
paddle_right_x = RES_W - 40
paddle_left_y = RES_H/2
paddle_right_y = RES_H/2
paddle_width = 25
paddle_height = 100
paddle_vel = 5

  
#creating a class and initializing all the attributes                  
class DiskAndPaddle():
    def __init__(self, disk_xc, disk_yc, disk_w, disk_h, disk_speed_x, disk_speed_y, paddle_left_x, paddle_left_y, paddle_right_x, paddle_right_y, paddle_width, paddle_height):
        #x coordinate of the disk
        self.disk_xc = disk_xc
        
        #y coordinate of the disk
        self.disk_yc = disk_yc
        
        #self.disk_w and self.disk_h are the width and the height of the disk, in other words, the diameter of the disk
        self.disk_w = disk_w
        self.disk_h = disk_h
        
        self.px = paddle_left_x
        self.pxr = paddle_right_x
        self.py = paddle_left_y
        self.pyr = paddle_right_y
        self.pw = paddle_width
        self.ph = paddle_height
        self.ps = paddle_vel
        self.disk_speed_x = disk_speed_x
        self.disk_speed_y = disk_speed_y
        self.key_handler = {"w": False, "s": False, UP: False, DOWN: False}
        # adding sound effects 
        self.collision_sound = player.loadFile(path + "/sounds/collision.mp3")
        self.win_sound = player.loadFile(path + "/sounds/win.mp3")
        
# code for displaying the disk    
    def Disk_display(self):
        fill(255,255,255)
        ellipse(self.disk_xc, self.disk_yc, self.disk_w, self.disk_h)

# code for displaying two paddles          
    def Paddle_display(self):
        rectMode(CENTER) # Modifies the location from which rectangles are drawn to the Center
        fill(0,0,243)
        rect(self.px, self.py, self.pw, self.ph)
        fill(214,0,0)
        rect(self.pxr, self.pyr, self.pw, self.ph) 
           
#code for restricting paddle boundaries so that they don't go out of the table borders
    def Paddle_boundaries(self):
        if self.py + self.ph/2 > RES_H:# restricting lower boundary
            self.py = self.py - self.ps
            
        elif self.py - self.ph/2 < 0:# restricting upper boundary
            self.py = self.py + self.ps
            
        if self.pyr + self.ph/2 > RES_H: # restricting lower boundary
            self.pyr = self.pyr - self.ps    
        
        elif self.pyr - self.ph/2 < 0: # restricting upper boundary
            self.pyr = self.pyr + self.ps
            
    
#Paddle movement through W, S and UP, DOWN keyboards

    def Paddle_movement(self):
        
        #if "w" is pressed, left paddle will move up
        if self.key_handler["w"]:
            self.py = self.py - self.ps
        
        #if "s" is pressed, left paddle will move down
        if self.key_handler["s"]:
            self.py = self.py + self.ps
            
        #if "UP" is pressed, right paddle will move up
        if self.key_handler[UP]:
            self.pyr = self.pyr - self.ps
       
       #if "DOWN" is pressed, right paddle will move down
        if self.key_handler[DOWN]:
            self.pyr = self.pyr + self.ps
      

    #Code for managing Disk movement               
    def Disk_movement(self):  
        self.disk_xc = self.disk_xc + self.disk_speed_x
        self.disk_yc = self.disk_yc + self.disk_speed_y

    #Code for managing Disk bouncing when it touches boundaries 
    def Disk_bouncing(self):
        global score_player2
        global score_player1 
         
        #Code for bouncing off if disk hits the boundaries
        #this if statement will be executed if the disk touches right-side boundaries of the table
        if self.disk_xc + self.disk_w/2 > RES_W:
            
            #the disk should bounce off only when it hits the area outside the opponent's goal
            if RES_H/2 + 100  < self.disk_yc  or self.disk_yc < RES_H/2 - 100:
                self.disk_speed_x = - self.disk_speed_x
                
            #updating the score of player 1 if he/she hits the opponent's goal                    
            else:
                score_player1 += 1
                self.win_sound.rewind()
                self.win_sound.play()
                print(self.disk_xc,self.disk_yc)
                
                #the game will continue and the disk will be reinitialized
                continueGame()
                
         #this if statement will be executed if the disk touches left-side boundaries of the table       
        elif self.disk_xc - self.disk_w/2 < 0:
            
            if RES_H/2 + 100 < self.disk_yc  or self.disk_yc < RES_H/2 - 100:
                self.disk_speed_x = - self.disk_speed_x
                
            # updating the score of player 2 if he/she hits the opponent's goal        
            else:        
                score_player2 += 1
                self.win_sound.rewind()
                self.win_sound.play()
                print(self.disk_xc,self.disk_yc)
                continueGame()                
                               
        #this if statement will be executed if the disk touches upper or lower boundaries of the table
        if self.disk_yc + self.disk_h/2 > RES_H or self.disk_yc - self.disk_h/2 < 0:
            if RES_H/2 + 100 < self.disk_yc  or self.disk_yc < RES_H/2 - 100 :
                self.disk_speed_y = - self.disk_speed_y
     
        self.disk_xc = self.disk_xc + self.disk_speed_x
        self.disk_yc = self.disk_yc + self.disk_speed_y                     
                
        
        global winning_player
        global round_number
        global switch_round
        global num_wins_player1
        global num_wins_player2
        
        
        #if the player1 scores 15, it means he/she wins this round
        if score_player1 == 5:
            winning_player = 1
            num_wins_player1 += 1
            round_number += 1
            switch_round = True

        #if the player2 scores 15, it means he/she wins this round   
        elif score_player2 == 5:
            winning_player = 2
            num_wins_player2 += 1
            round_number += 1
            switch_round = True
            
                        
# function for displaying the scores of the players, along with the player name and round number     
    def Score_display(self):
        fill(255)
        textSize(20)
        textAlign(CENTER)
        text("Round:" + str(round_number), RES_W/2, 50)
        text("Player 1", 100, 50)
        text(score_player1, 100, 80)
        text("Player 2", RES_W - 100, 50) 
        text(score_player2, RES_W - 100, 80)    
        
    #Code for managing Disk bouncing when it touches paddles 
    def Disk_Paddle_Contact(self):
        
        #We manage the Disk and Paddle contact by looking into coordinates of Disk and Paddle and creating condition "if" which checks whether the disk contacted the paddle
        
        #check whether the disk contacted the left paddle
        if (self.disk_xc - self.disk_w/2 < self.px + self.pw/2) and (self.disk_yc + self.disk_h/2 > self.py - self.ph/2) and (self.disk_yc - self.disk_h/2 < self.py + self.ph/2):
            if self.disk_speed_x < 0:
                self.collision_sound.rewind()
                self.collision_sound.play()
                print(self.px,self.py)
                print("contacted left paddle")
                self.disk_speed_x = - self.disk_speed_x
                
        ##check whether the disk contacted the right paddle      
        elif (self.disk_xc + self.disk_w/2 > self.pxr - self.pw/2) and (self.disk_yc + self.disk_h/2 > self.pyr - self.ph/2) and (self.disk_yc - self.disk_h/2 < self.pyr + self.ph/2):
            if self.disk_speed_x > 0:
                self.collision_sound.rewind()
                self.collision_sound.play()
                print(self.pxr,self.pyr)
                print("contacted right paddle")
                self.disk_speed_x = - self.disk_speed_x

# Note in some rare cases minor bugs can occur because Processing does not update coordinates fast enough and real world physics cannot be recreated ideally                                                                                                

class Game:
    def __init__(self):
        self.disk = DiskAndPaddle(disk_xc, disk_yc, disk_w, disk_h, disk_speed_x, disk_speed_y, paddle_left_x, paddle_left_y, paddle_right_x, paddle_right_y, paddle_width, paddle_height)
        # code for adding background music
        self.bg_sound = player.loadFile(path + "/sounds/background.mp3")
        self.bg_sound.loop()
        
        global round_number
        
        if round_number == 2:
            self.bg_sound.pause()
        
        if round_number == 3:
            self.bg_sound.pause()    

# code for preventing overlapping of background sound
        if round_number == 4:
            player.stop()
                

    def display(self):
        global round_number
        background(0)
        
        #circle in the center
        ellipseMode(CENTER)
        fill(194, 194, 194)
        ellipse(RES_W/2,RES_H/2,RES_W/5,RES_W/5)
        ellipseMode(CENTER)
        fill(0)
        ellipse(RES_W/2,RES_H/2,RES_W/5-BORDER/2,RES_W/5-BORDER/2)
            
        #rectangle borders
        fill(194, 194, 194)
        rectMode(CENTER)
        rect(RES_W/2,RES_H/2,BORDER/4,RES_H*2)
        fill(194, 194, 194)
        rect(0,0,RES_W*2,BORDER)
        fill(194, 194, 194)
        rect(0,RES_H,RES_W*2,BORDER)
        fill(194, 194, 194)
        rect(RES_W,0,BORDER,RES_H*2)
        fill(194, 194, 194)
        rect(0,0,BORDER,RES_H*2)
        
        #goal of the blue paddle
        fill(194, 194, 194)
        ellipse(0,RES_H/2,200,200)
        fill(0)
        ellipse(0,RES_H/2,200-BORDER/2,200-BORDER/2) 
         
        #goal of the red paddle
        fill(194, 194, 194)
        ellipse(RES_W,RES_H/2,200,200)
        fill(0)
        ellipse(RES_W,RES_H/2,200-BORDER/2,200-BORDER/2)          
        
        self.disk.Disk_display()
        self.disk.Disk_bouncing()
        self.disk.Disk_movement()
        self.disk.Disk_Paddle_Contact()
        self.disk.Paddle_display()
        self.disk.Paddle_movement()
        self.disk.Paddle_boundaries()
        self.disk.Score_display()

        
game = Game()    
        
def setup():
     size(RES_W,RES_H)
     background(0)
    
def draw(): 
    global game_over 
    global game_start 
    global round_number 
    global switch_round
        
    if game_start == True:
        gameStartDisplay()

    if game_start == False and switch_round == False and round_number != 4:
        game.display()
        
    if game_start == False and switch_round == True:
        if round_number == 4:
            game_over = True
            gameOverDisplay()
        else:
            SwitchBetweenRoundsDisplay()
        
        
#this function is used to update the disk to its initial location whenever someone scores a goal
def continueGame():
    global game
    game.disk = DiskAndPaddle(disk_xc, disk_yc, disk_w, disk_h, disk_speed_x, disk_speed_y, paddle_left_x, paddle_left_y, paddle_right_x, paddle_right_y, paddle_width, paddle_height)
    
    
#this function is used to start a new round
def newRound():
    global score_player1
    global score_player2
    global disk_speed_x
    global disk_speed_y
    
    score_player1 = 0
    score_player2 = 0
    
    #as the round increases, the speed of the disk also increases, thus increasing the complexity the game
    disk_speed_x += 0.75
    disk_speed_y += 0.75
    
    global game
    game = Game()
   
#this function is used for restarting the game 
def restartGame():
    global score_player1
    global score_player2
    global game_over
    global game_start
    global switch_round
    global round_number
    global winning_player
    global num_wins_player1
    global num_wins_player2
    global disk_speed_x
    global disk_speed_y
    
    score_player1 = 0
    score_player2 = 0
    game_over = False
    game_start = True
    switch_round = False
    round_number = 1
    winning_player = 0
    num_wins_player1 = 0
    num_wins_player2 = 0
    disk_speed_x = 2
    disk_speed_y = 2
    
    global game
    game = Game()
        
#this display will be displayed when the game starts
def gameStartDisplay():
    background(0)
    fill(255)
    textAlign(CENTER)
    textSize(30)
    text("Welcome to the Air Hockey game!", RES_W/2, RES_H/2)
    fill(255)
    textSize(15)
    text("Click anywhere to start", RES_W/2, RES_H/2 + 30)
          
#this display will be displayed when switching between rounds          
def SwitchBetweenRoundsDisplay():
    background(0)
    fill(255)
    global round_number
    global winning_player
    textAlign(CENTER)
    textSize(30)
    text("Player " + str(winning_player) + " has won this round!", RES_W/2, RES_H/2)
    textSize(15)
    text("Click anywhere to continue the game", RES_W/2, RES_H/2 + 30)
            
  
#this display will be displayed when the game is over         
def gameOverDisplay():
    global num_wins_player1
    global num_wins_player2
    global winning_player
    
    #code for identifying the ultimate winner of the game
    if num_wins_player1 > num_wins_player2:
        winning_player = 1
    else:
        winning_player = 2
        
    background(0)
    fill(255)
    textAlign(CENTER)
    textSize(40)
    text("Game is over!", RES_W/2, RES_H/2)
    textSize(25)
    text("Player " + str(winning_player) + " has won this game!", RES_W/2, RES_H/2 + 50)
    textSize(15)
    text("Click anywhere to restart the game", RES_W/2, RES_H/2 + 80)
    
    
def mouseClicked():
    global game_over 
    global game_start 
    global switch_round

    #when the mouse will be clicked while in a gameStartDisplay(), game_start will change to False, thus allowing us to display the actual game
    if game_start == True:
        game_start = False
        
    #when mouse will be clicked while in a switchRoundsDisplay(), switch_round will change to False and new round will be created
    if switch_round == True:
        switch_round = False
        newRound()
        
    #when mouse will be clicked while in a gameOverDisplay(), game_over will change to False and the game will be restarted
    if game_over == True:
        game_over = False
        restartGame()
            
        
def keyPressed():
    if key == "w" or key == "W":
        game.disk.key_handler["w"] = True
    elif key == "s" or key == "S":
        game.disk.key_handler["s"] = True
    elif keyCode == UP:
        game.disk.key_handler[UP] = True
    elif keyCode == DOWN:
        game.disk.key_handler[DOWN] = True    
                

def keyReleased():
    if key == "w" or key == "W":
        game.disk.key_handler["w"] = False
    elif key == "s" or key == "S":
        game.disk.key_handler["s"] = False
    elif keyCode == UP:
        game.disk.key_handler[UP] = False
    elif keyCode == DOWN:
        game.disk.key_handler[DOWN] = False    
