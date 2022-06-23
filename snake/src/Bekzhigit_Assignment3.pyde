import os
import random

TILE_WIDTH=30
TILE_HEIGHT=30
RESOLUTION=600

#radius of the element of the snake is by default 15
RADIUS=TILE_WIDTH/2

path = os.getcwd()

#this class is responsible for the elements of the snake's tail
class Element():
    #r - row, c - column, img - later will be used to randomly draw a fruit
    def __init__(self,r,c,img=2):
        self.r=r
        self.c=c     
        self.x=self.c*TILE_WIDTH
        self.y=self.r*TILE_HEIGHT
        self.img=img  
            
    def display(self):
        if self.img==0:
            fill(173, 48, 32)
        elif self.img==1:
            fill(251, 226, 76)
        else:
            fill(80,153,32)
        strokeWeight(0)
        #an element of the snke's tail will be a circle with radius 15
        ellipse(self.x + RADIUS, self.y + RADIUS,TILE_WIDTH,TILE_HEIGHT)
 
#this class is responsible for the snake's head            
class Head(Element):
    def __init__(self,r,c):
        #this class inherits the attributes & methods of the class Element
        Element.__init__(self,r,c,img=2)
        #loading the images of the snake's head
        self.head_right=loadImage(path+"/images/head_right.png")
        self.head_up=loadImage(path+"/images/head_up.png")
        
        #the attributes x1,x2,y1,y2 are used to crop the images of head
        self.x1=self.c*TILE_WIDTH
        self.x2=(self.c+1)*TILE_WIDTH
        self.y1=self.r*TILE_HEIGHT
        self.y2=(self.r+1)*TILE_HEIGHT

        
    def display_right(self,x1,y1,x2,y2):
        image(self.head_right,self.x, self.y,TILE_WIDTH,TILE_HEIGHT,x1,y1,x2,y2)
        
    def display_up(self,x1,y1,x2,y2):
        image(self.head_up,self.x, self.y,TILE_WIDTH,TILE_HEIGHT,x1,y1,x2,y2)
 
        
#this class is responsible for the movement/growth of the snake       
class Snake(Element):
    def __init__(self,r,c):
        Element.__init__(self,r,c)
        #create a list which will hold the head and elements of the snake
        self.body=[]
        self.body.append(Head(self.r,self.c))
        self.body.append(Element(self.r,self.c-1))
        self.body.append(Element(self.r,self.c-2))
        
        #dictionary for handling movement of the snake
        self.key_handler = {LEFT:False, RIGHT:False, UP:False, DOWN:False}
        
        #these attributes are responsible for changing the direction of the snake with respect to the KEY pressed
        self.direction = RIGHT
        self.change_to=RIGHT
        
        #this attricbute is responsible for checking if the game is over or not
        self.game_over=False
    
    #this function is responsible for changing the direction of the snake when corresponding KEYS are pressed
    #i'm creating two dirrerent attributes "change_to" and "direction" to prevent the snake from moving the opposite direction of the current movement         
    def change_direction(self):   
        if self.key_handler[LEFT]:
            self.change_to=LEFT
        if self.key_handler[RIGHT]:
            self.change_to=RIGHT
        if self.key_handler[UP]:
            self.change_to=UP
        if self.key_handler[DOWN]:
            self.change_to=DOWN  
            
        if self.change_to==LEFT and self.direction!=RIGHT:
            self.direction=LEFT
        if self.change_to==RIGHT and self.direction!=LEFT:
            self.direction=RIGHT
        if self.change_to==UP and self.direction!=DOWN:
            self.direction=UP
        if self.change_to==DOWN and self.direction!=UP:
            self.direction=DOWN
     
    #this function will be called if RIGHT key will be pressed     
    #to create the movement, the elements of the snake's body will be replacing the preceding element(starting from the back of the tail)   
    def move_right(self):
        for i in range(len(self.body)-1,0,-1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
            self.body[i].display()
        self.body[0].x+=30   
        self.body[0].display_right(0,0,TILE_WIDTH,TILE_HEIGHT)
     
    #this function will be called if UP key will be pressed        
    def move_up(self):
        for i in range(len(self.body)-1,0,-1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
            self.body[i].display()
        self.body[0].y-=30   
        self.body[0].display_up(0,0,TILE_WIDTH,TILE_HEIGHT) 
    
    #this function will be called if LEFT key will be pressed     
    def move_left(self):
        for i in range(len(self.body)-1,0,-1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
            self.body[i].display()
        self.body[0].x-=30   
        self.body[0].display_right(TILE_WIDTH,0,0,TILE_HEIGHT)
    
    #this function will be called if DOWN key will be pressed     
    def move_down(self):
        for i in range(len(self.body)-1,0,-1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
            self.body[i].display()
        self.body[0].y+=30   
        self.body[0].display_up(TILE_WIDTH,TILE_HEIGHT,0,0) 
     

    #this function will be called to stop the snake's movement when the game is over
    def stop(self):
        for i in range(0,len(self.body)):
            self.body[i].display()

     
     #this function is responsible for checking if the game is over or not   
    def check_game(self):
        
        #If the snake hits the boundaries of the board, the game is over.        
        if self.body[0].x<0 or self.body[0].x>=RESOLUTION or self.body[0].y<0 or self.body[0].y>=RESOLUTION:
            self.game_over=True
         
 
        #If the head of the snake collides with any element (tail) of the snake, the game is over.      
        for i in range(1,len(self.body)-1):
            if self.body[0].x==self.body[i].x and self.body[0].y==self.body[i].y:
                self.game_over=True
                break
         
         #If the screen is completely filled with snake elements, i.e. the length of the snake becomes 400 and no further movement is possible, the game ends    
        if len(self.body)==(RESOLUTION/TILE_WIDTH)*(RESOLUTION/TILE_HEIGHT):
            self.game_over=True
                                         
    #this function is responsible for displaying the moving snake                                                                             
    def display(self):
        self.check_game()
        self.change_direction()
        if self.game_over==False:
            if self.direction==RIGHT:
                self.move_right()
            if self.direction==UP:
                self.move_up()
            if self.direction==LEFT:
                self.move_left()
            if self.direction==DOWN:
                self.move_down()
        else:
            self.stop()
            #if the game is over, Game Over Screen will be displayed
            gameOverScreen()

#this class is responsible for initializing the attributes related to fruits and displaying the fruit            
class Fruit(Element):
    def __init__(self,r,c,img):
        Element.__init__(self,r,c)
        #creating the list which will hold the images of apple and banana
        self.fruit=[]
        self.apple=loadImage(path+"/images/apple.png")
        self.fruit.append(self.apple)
        self.banana=loadImage(path+"/images/banana.png")
        self.fruit.append(self.banana)
        self.img=img
    
    #this function is responsible for displaying the fruit
    def display(self):
        image(self.fruit[self.img],self.x,self.y,TILE_WIDTH,TILE_HEIGHT)
    
#this class is responsible for the main game                                        
class Game(Element):
    #it inherits attributes/methods from the Element class
    def __init__(self,r,c):
        Element.__init__(self,r,c)
        
        #instantiating the snake
        self.snake = Snake(self.r,self.c)
        
        #this attribute will be used when checking if the snake collided with the fruit or not
        self.collided=False
        
        #this attribute will be used to accumulate and display the score
        self.score=0
        
        #this attribute will be used to check if the game is over or not
        self.game_over=False
        self.k=0
           
        self.generate_fruit() 
    
      #this function is responsible for generating fruit in random position      
    def generate_fruit(self):
        
        self.c=random.randint(0,RESOLUTION/TILE_WIDTH-1)
        self.r=random.randint(0,RESOLUTION/TILE_HEIGHT-1)
        
        #this function is responsible for ensuring that the fruit's randomly drawn location does not overlap with the body/tail of the snake.
        for i in self.snake.body:
            if self.c*TILE_WIDTH==i.x and self.r*TILE_HEIGHT==i.y:
                self.c=random.randint(0,RESOLUTION/TILE_WIDTH-1)
                self.r=random.randint(0,RESOLUTION/TILE_HEIGHT-1)
                continue            
            else:
                continue
         #if the fruit doesn't overlop with the tail/body of the snake, a new object fruit will be instantiated                       
        self.fruit = Fruit(self.r,self.c,random.randint(0,1))   
     
      #this function is reponsible for checking if the snake "ate" the fruit 
    def collision(self): 
        #if the snake collides with the fruit(eats it) this part of the code will be executed
        if self.snake.body[0].x == self.fruit.x and self.snake.body[0].y == self.fruit.y:
            self.collided=True
            self.score+=1
            
            #if the snake eats apple, a new element in red color will be added to its tail
            if self.fruit.img==0:
                self.snake.body.append(Element(self.snake.r,self.snake.c-self.k,0))
                
             #if the snake eats banana, a new element in yellow color will be added to its tail    
            elif self.fruit.img==1:#banana
                self.snake.body.append(Element(self.snake.r,self.snake.c-self.k,1))
                
            #after the snake eats the fruit, a new fruit will be generated again in random position
            self.generate_fruit()
         
        #if the snake doesn't collide with the fruit(eats it), self.collided will be False  
        else:
            self.collided=False
     
    #this function is responsible for displaying the main game screen with the snake and the fruits       
    def display(self):    
        textAlign(LEFT)
        fill(0)
        textSize(15)
        #the score will be displayed in the upper right corner of the screen 
        text("Score:"+str(game.score),RESOLUTION-70,30) 
        self.snake.display()
        self.collision()
        if self.game_over==False:
            self.fruit.display()
   
#instantiating the game object                
game = Game((RESOLUTION/TILE_WIDTH)//2,(RESOLUTION/TILE_HEIGHT)//2)

def setup():
    size(RESOLUTION,RESOLUTION)
    background(205)
    
def draw():
    # this function is used to slow down the speed of the game
    if game.game_over==False:
        if frameCount%12 == 0: 
            background(205)
            game.display()
            
#this function is responsible for restarting the game                
def restart():
    global game
    game = Game((RESOLUTION/TILE_WIDTH)//2,(RESOLUTION/TILE_HEIGHT)//2)
 
#this function is responsible for displaying the game over screen with all the texts and the final score        
def gameOverScreen():
    game.game_over=True
    background(205)
    textAlign(CENTER)
    fill(0)
    textSize(15)
    text("Your score is:"+str(game.score),RESOLUTION/2,RESOLUTION/2+50)
    fill(255)
    textSize(30)
    text("Game Over",RESOLUTION/2,RESOLUTION/2)
    textSize(15)
    text("Click to Restart",RESOLUTION/2,RESOLUTION/2-50)
                
#if the mouse is clicked while in the "Game Over screen", the game will be restarted
def mouseClicked():
    if game.game_over==True:
        restart()
    
def keyPressed():  
    if keyCode == LEFT:
        game.snake.key_handler[LEFT] = True
    elif keyCode == RIGHT:
        game.snake.key_handler[RIGHT] = True
    elif keyCode == UP:
        game.snake.key_handler[UP] = True
    elif keyCode == DOWN:
        game.snake.key_handler[DOWN] = True
      
                
def keyReleased():
    if keyCode == LEFT:
        game.snake.key_handler[LEFT] = True
    else:
        game.snake.key_handler[LEFT] = False
    
    if keyCode == RIGHT:
        game.snake.key_handler[RIGHT] = True
    else:
        game.snake.key_handler[RIGHT] = False
    
    if keyCode == UP:
        game.snake.key_handler[UP] = True
    else:
        game.snake.key_handler[UP] = False
    
    if keyCode == DOWN:
        game.snake.key_handler[DOWN] = True
    else:
        game.snake.key_handler[DOWN] = False


    
