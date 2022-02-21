'''
Final Project: Plants v.s. Zombies But Python

Name: Sichao(Tommy) Bi
Andrew Id: sichaob
Due Date: 5P.M. EST, Friday, 13/08/2021

'''
from cmu_112_graphics import *
from tkinter import *
import random


#################################################
# Starting Screen Functions
#################################################

# Draw and load images onto the start screen
def startScreen_redrawAll(app, canvas):

    # The background image
    canvas.create_image(app.width / 2, app.height / 2, 
                        image = ImageTk.PhotoImage(app.menu))


# If the user presses any key go into menu mode 
def startScreen_keyPressed(app, event):

    # Go to the next mode: menu mode 
    app.mode = "menu"


#################################################
# Starting Screen Functions
#################################################



#################################################
# Menu Functions
#################################################


# Perform some actions When the player clicks on certain parts of the menu
def menu_mousePressed(app, event):

    # Extract x and y cords of where the player clicked 
    x, y = event.x, event.y

    # If player hit the "adventure mode" box, 
    if 500 <= x <= 885 and 75 <= y <= 205:
        # Go to the game mode!
        app.mode = "game"

    

# Perform some actions when the player presses some keys 
def menu_keyPressed(app, event):

    # Extract the key 
    key = event.key


    # Let the user enter their name and display it 
    if key == "n":

        # "getUserInput" method is learned from
        # https://cs.cmu.edu/~112/notes/notes-animations-part4.html#ioMethods
        name = app.getUserInput("Hi! What is your name?")

        if name == None:
            app.nameMessage = "Nothing Is Entered!"

        else: 
            app.nameMessage = name + "!"



# Call all of the drawing functions for the menu screen
def menu_redrawAll(app, canvas):

    # Menu background image
    canvas.create_image(app.width / 2, app.height / 2, 
                        image = ImageTk.PhotoImage(app.menu))

    # Adventure mode box
    canvas.create_rectangle(500, 75, 885, 205, outline = "red", width = 4)


    # Display user name
    canvas.create_text(200, 104, text = app.nameMessage, 
                       font = "Arial 17 bold", fill = "magenta")


#################################################
# Menu Functions
#################################################




#################################################
# Game Functions
#################################################


# Check if the given cords are in the drawn grid
def inLawn(app, x, y):

    # If the x, y cords are inside the grid, or on the lawn
    if (app.leftMargin <= x <= app.leftMargin + app.cols * app.cellWidth
        and app.topMargin <= y <= app.topMargin + app.rows * app.cellHeight):

        return True

    else: return False


# Get the row, col of a cell given its x, y cords
def getCell(app, x, y):

    # If the given cords are inside of the drawn grid
    if inLawn(app, x, y):

        # This part is learned from 
        # https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html
        row = int((y - app.topMargin) / app.cellHeight)
        col = int((x - app.leftMargin) / app.cellWidth)

        return row, col

    # If not inside of the grid make it gone
    else: return -1, -1


# Get row, col, for the SLOT grid given x, y cords
# Inspired by https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html
def getSlotCell(app, x, y):

    # If given x, y in the slot range
    if(app.leftMargin <= x <= app.leftMargin + 7 * app.cellWidth
        and 10 <= y <= app.topMargin - 10):

        row = 0 
        col = int((x - app.leftMargin) / app.cellWidth)

        return row, col

    else: return -1, -1


# Check if the clicked row, col are in the plantslot
def inSlotsGrid(app, x, y):

    _, col = getSlotCell(app, x, y)

    # If in the plants slot grid
    if 1 <= col <= 6:

        return True

    return False



# Keep track of where the mouse is being moved 
def game_mouseMoved(app, event):

    # If not game over
    if not app.gameOver:

        # Extract x, y cords 
        x, y = event.x, event.y 

        # If mouse is inside of the plant slot grid
        if inSlotsGrid(app, x, y):

            # Update the mouse cords 
            app.mouseX, app.mouseY = x, y
            #print("move")

        # And if we have selected a plant and moving inside of the lawn 
        # an indication of the plant chosen will move with the mouse 
        elif app.plantSelected and inLawn(app, x, y):

            app.mouseX, app.mouseY = x, y



# Perform some actions When the player clicks on certain parts of the game/lawn
def game_mousePressed(app, event):

    # If not game over
    if not app.gameOver:

        # Extract x and y cords of where the player clicked 
        x, y = event.x, event.y

        # If player clicks inside of the slots grid 
        if inSlotsGrid(app, x, y): 

            # Get the slot col, need to know the col number to see which plant it is
            row, col = getSlotCell(app, x, y)


            # Update selection info AND total sun info
            if col == 1: 
                app.selectedPlant = plant(app, "Sunflower", 0, 0, app.singlesfImg)
                app.plantSelected = not app.plantSelected
                app.totalSun += 10

            elif col == 2: 
                app.selectedPlant = plant(app, "Peashooter", 0, 0, app.singlepsImg)
                app.plantSelected = not app.plantSelected
                app.totalSun -= 10

            elif col == 3: 
                app.selectedPlant = plant(app, "CabbagePult", 0, 0, app.singlecabPImg)
                app.plantSelected = not app.plantSelected
                app.totalSun -= 10

            else: 
                app.selectedPlant = ""
                app.plantSelected = not app.plantSelected


        # Calclate the row and column number
        row, col = getCell(app, x, y)

        # If current row, col in plantsgrid and is not out of bounds
        if (0 <= row < app.rows and 0 <= col < app.cols and app.plantSelected):

            # Update the plants grid
            app.plantsGrid[col] = app.plantsGrid.get(col, list())

            if isinstance(app.selectedPlant, plant):
                app.selectedPlant.row, app.selectedPlant.col = row, col

            app.plantsGrid[col].append(app.selectedPlant)

            # Unselect the app.plantSelected
            app.plantSelected = False

            # Update bullet list
            if app.selectedPlant.bulletType == "pea":

                app.selectedPlant.peaBullet(app)

            elif app.selectedPlant.bulletType == "cabbage":

                app.selectedPlant.cabbageProjectile(app)




# Perfrom certain actions when certain keys are pressed on the game screen
def game_keyPressed(app, event):

    # Get the key
    key = event.key

    # If game not over
    if not app.gameOver:
        # Get a random map -- sort of a test but can stay
        if key == "n":

            app.lawn = app.loadImage(
                app.lawnChoices[random.randint(0, 2)]).resize((app.width, app.height))


        # Let the user enter some "cheats"
        elif key == "b":

            # "getUserInput" method is learned from
            # https://cs.cmu.edu/~112/notes/notes-animations-part4.html#ioMethods
            name = app.getUserInput("Enter 'kill' to kill all existing zombies!\nOr click cancel.")
            

            if name == None:
                app.message = "Nothing Is Entered!"

            elif name == "kill":

                # Clear all zombies on the lawn
                app.zomList = dict()
                app.showMessage("Boom! all zoms are 'dead' now!")
                app.message = f"Command: {name}"

            else: app.message = "Command Not Recognized!"

        # Let the user clear ALL zombies and plants on the lawn
        elif key == "r":

            app.zomList = dict()
            app.plantsGrid = dict()
            app.bullets = []

        # Go back to the menu
        elif key == "m":
            app.mode = "menu"


    # If game is over, go back to menu
    elif key == "Enter":

        # Reset basic game features 
        app.mode = "menu"
        app.zomList = dict()
        app.plantsGrid = dict()
        app.bullets = []
        app.totalSun = 100
        app.gameOver = False


# Draw the plant slots, sun counter, and plants preview
def game_drawSlots(app, canvas):

    # There will be, in total, 7 slots -- TBD
    for col in range(7):

        # Calculate the x, y cords of each cell
        x1 = app.leftMargin + col * app.cellWidth
        y1 = 10
        x2 = x1 + app.cellWidth
        y2 = app.topMargin - 10 

        # Draw the cell 
        canvas.create_rectangle(x1, y1, x2, y2, 
                                outline = "violet", width = 4)

    # Display the sun amount, and plants preview
    canvas.create_image(app.leftMargin + app.cellWidth / 2, app.cellHeight / 2,
                        image = ImageTk.PhotoImage(app.sun))
    canvas.create_text(app.leftMargin + app.cellWidth / 2,
                       app.cellHeight / 2 + 30, 
                       text = f"Sun: {app.totalSun}", font = "Arial 14 bold",
                       fill = "red")

    # Sunflower
    canvas.create_image(app.leftMargin + app.cellWidth + app.cellWidth / 2, 
                        app.cellHeight / 2,
                        image = ImageTk.PhotoImage(app.singlesfImg))
    canvas.create_text(app.leftMargin + app.cellWidth + app.cellWidth / 2, 
                       app.cellHeight / 2 + 30, 
                       text = "Give 10 sun", font = "Arial 13 bold",
                       fill = "red")
    
    # Peashooter
    canvas.create_image(app.leftMargin + 2 * app.cellWidth + app.cellWidth / 2, 
                        app.cellHeight / 2,
                        image = ImageTk.PhotoImage(app.singlepsImg))
    canvas.create_text(app.leftMargin + 2 * app.cellWidth + app.cellWidth / 2, 
                       app.cellHeight / 2 + 30, 
                       text = "Sun: 10", font = "Arial 11 bold",
                       fill = "red")


    # CabbagePult
    canvas.create_image(app.leftMargin + 3 * app.cellWidth + app.cellWidth / 2, 
                        app.cellHeight / 2,
                        image = ImageTk.PhotoImage(app.singlecabPImg))
    canvas.create_text(app.leftMargin + 3 * app.cellWidth + app.cellWidth / 2, 
                       app.cellHeight / 2 + 30, 
                       text = "Sun: 10", font = "Arial 11 bold",
                       fill = "red")


# Draw cells according to the lawn pattern 
# Note that on the lawn each cell is different from each other in terms of sizes
# So there exists slight precision errors 
def game_drawCellsOnLawn(app, canvas):

    # Loop through all rows and columns of the lawn 
    for row in range(app.rows):
        for col in range(app.cols):

            # Calculate the x, y cords of each cell
            x1 = app.leftMargin + col * app.cellWidth
            y1 = app.topMargin + row * app.cellHeight
            x2 = x1 + app.cellWidth
            y2 = y1 + app.cellHeight

            # Draw the cell 
            canvas.create_rectangle(x1, y1, x2, y2, 
                                    outline = "brown", width = 4)



###################

# Drawing functions

# Get the x, y cords from the given row, col cords
# Copied from https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html
def getCellBounds(app, row, col):

    x0 = app.leftMargin + app.cellWidth * col
    x1 = app.leftMargin + app.cellWidth * (col+1)
    y0 = app.topMargin + app.cellHeight * row
    y1 = app.topMargin + app.cellHeight * (row+1)
    return (x0, y0, x1, y1)


# Draw the plants on the lawn 
def game_drawPlants(app, canvas):

    # Go through the dict
    for key in app.plantsGrid:
        for p in app.plantsGrid[key]:
            
            # Find a plant and draw it 
            if isinstance(p, plant):
                p.draw(app, canvas)


    # Draw the bullets on the lawn
    for bullet in app.bullets:
        x, y = bullet
        canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill = "green")



# Draw projectiles for cabbagePult
def game_drawProjectile(app, canvas):

    canvas.create_oval(app.ballX - app.ballR, app.ballY - app.ballR, 
                        app.ballX + app.ballR, app.ballY + app.ballR,
                        fill = "green")


#######################



# Check if game is over 
def game_checkGameOver(app):

    # All zombies
    for key in app.zomList:
        for z in app.zomList[key]:
            
            # If any zombie crosses the left side of the lawn, game is over
            if z.x <= 0: app.gameOver = True



# The game screen's timerFired
def game_timerFired(app):


    # Check if game is over 
    game_checkGameOver(app)
    

    # Not game over 
    if not app.gameOver:

        # Zombies' generation and movement 
        # Generate zombies every 1.25 seconds 
        app.timer += app.timerDelay

        if app.timer == 1250:

            roll = random.randint(1, 10)  # A random int [1, 10]

            # Fast zombie
            if roll == 5:
                tempZom = zombie(app, "fast", 150, 110, 0, "red")
            
            # Tanky zombie
            elif roll == 3 or roll == 6:
                tempZom = zombie(app, "tanky", 400, 30, 0, "black")

            # Smart zombie
            elif roll == 4 or roll == 8: 
                tempZom = zombie(app, "smart", 200, 45, 0, "yellow")

            # Normal zombie
            else: tempZom = zombie(app, "normal", 200, 45, 0, "gray")

            # Make sure that two zombies don't generate back to back on the same row
            while(tempZom.row == app.lastRow):

                # Fast zombie
                if roll % 5 == 0:
                    tempZom = zombie(app, "fast", 150, 110, 0, "red")
                
                # Tanky zombie
                elif roll % 3 == 0:
                    tempZom = zombie(app, "tanky", 400, 30, 0, "black")

                # Smart zombie
                elif roll % 4 == 0: 
                    tempZom = zombie(app, "smart", 200, 45, 0, "yellow")

                # Normal zombie
                else: tempZom = zombie(app, "normal", 200, 45, 0, "gray")


            # Just to keep track of which row the last zombie was generated on 
            app.lastRow = tempZom.row

            # Add the new zombie to the zombie dict 
            app.zomList[tempZom.row] = app.zomList.get(tempZom.row, list())
            app.zomList[tempZom.row].append(tempZom)

            # All zombies move to the left by their speed
            for key in app.zomList: 
                for z in app.zomList[key]:

                    if z.name == "smart":

                        z.x -= z.speed
                        z.y += random.randint(-100, 300)


                    else:
                        z.x -= z.speed

            # Reset the timer
            app.timer = 0


        # Projectile parameter changes 
        app.yAcceleration -= 0.1
        app.ballX += app.vX
        app.ballY += app.vY

    
        # Plants' shooting mechanism 
        for i in range(len(app.bullets)): 

            # Add the bullet to bullets list
            x, y = app.bullets[i]
            newX = x + app.bulletSpeed
            app.bullets[i] = (newX, y)

            # Check if any zombie is hit
            for key in app.zomList:
                for z in app.zomList[key]:
                    z.checkHit(app, newX, y, 100)

    


# Call all of the drawing functions for the game screen
def game_redrawAll(app, canvas):

    if not app.gameOver:
        # Draw the background lawn first 
        canvas.create_image(app.width / 2, app.height / 2, 
                            image = ImageTk.PhotoImage(app.lawn))

        # Draw all of the cells on the lawn
        game_drawCellsOnLawn(app, canvas)

        # Draw all the plant slots, sun counter, and shovel
        game_drawSlots(app, canvas)

        # Text that asks the player's cheat -- to be made invisible
        canvas.create_text(app.width / 2, app.height / 2, 
                        text = app.message, font = 'Arial 24 bold')

        
        # TEMP DRAW for PLANTS
        game_drawPlants(app, canvas)

        # Draw zombies
        for key in app.zomList:
            for z in app.zomList[key]: 
                z.draw(canvas)


        # Draw the projectiles 
        game_drawProjectile(app, canvas)



    # If game over, draw a picture saying so
    else:
        # "The zombies ate your brain!"
        canvas.create_image(app.width / 2, app.height / 2,
                            image = ImageTk.PhotoImage(app.gameOverImg))

        # Message
        canvas.create_text(app.width / 2, app.height / 2 + 100, 
                           text = "Press 'Enter' to go back to menu", 
                           font = "Arial 20 bold", fill = "red")

#################################################
# Game Functions
#################################################




#################################################
# Plants 
#################################################

class plant(object):

    # Construcrtor
    def __init__(self, app, name, row, col, img):
        
        # Name
        self.name = name

        # Its image
        self.img = img


        # The row and column the plant is planted on
        self.row, self.col = row, col   


        # Bullet Type and damage
        if self.name == "Peashooter":
            self.damage = 75
            self.bulletType = "pea"   
            
        
        elif self.name == "CabbagePult":
            self.damage = 75
            self.bulletType = "cabbage"

        else:
            self.damage = 0
            self.bulletType = None

    
    # Bullet shooting
    def peaBullet(self, app):

        x1, y1, x2, y2 = getCellBounds(app, self.row, self.col)
        cellCenterX = (x1 + x2) / 2
        cellCenterY = (y1 + y2) / 2

        app.bullets.append((cellCenterX, cellCenterY))

    
    # Cabbage Projectile launching
    def cabbageProjectile(self, app):

        x1, y1, x2, y2 = getCellBounds(app, self.row, self.col)
        app.ballX = (x1 + x2) / 2
        app.ballY = (y1 + y2) / 2

        app.startX, app.startY = (x1 + x2) / 2, (y1 + y2) / 2

        for key in app.zomList:
            
            if len(app.zomList[key]) > 0:
                app.endX, app.endY = app.zomList[key][0].x, app.zomList[key][0].y




    
    # Draw the plant on a cell, given its row and column
    def draw(self, app, canvas):

        # All of the image processing, including the ones used below,
        # Are learned from https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html
        canvas.create_image(app.leftMargin + self.col * app.cellWidth + app.cellWidth / 2,
            app.topMargin + self.row * app.cellHeight + app.cellHeight / 2, 
            image = ImageTk.PhotoImage(self.img))




#################################################
# Plants
#################################################




#################################################
# Zombies 
#################################################

# Distance formula
def dist(x, y, x1, y1):

    return ((x - x1)**2 + (y - y1)**2) ** 0.5


# Make an empty 2d List
# Copied from https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html#creating2dLists
def make2dList(rows, cols):
    return [ ([0] * cols) for row in range(rows) ]


######################

# SPFA's: find the best path for the zombie to go through the lawn
# Complex algorithm
# Learned from Office Hour and
# https://en.wikipedia.org/wiki/Shortest_Path_Faster_Algorithm


# An edge connecting two nodes 
class Edge(object):

    def __init__(self, v, w):

        self.v = v  # Sides it goes to 
        self.w = w  # Weight of this edge


def SPFA(app):

    # Setting up variables
    dList = make2dList(app.rows, app.cols)

    for row in dList:
        for col in dList:

            dList[row][col] = app.plantsGrid[row][col]



    visited = []  # Visited or not 


    adj = []   # For storing edges

    num = app.cols * app.rows 

    for i in range(1, num + 1):

        v, w = 0, 0

        adj[i].append((Edge(v, w)))



    start, end = 0, num

    # Initialize the lists
    for i in range(1, num + 1):

        dList[i] = 9999999
        visited[i] = False
    dList[1] = 0


    # Functions as a temp list to go through values  
    temp = []
    temp.append(1)
    visited[1] = True

    # While temp list not empty
    while(len(temp) > 0):

        # Get the first value out of it 
        number = temp.pop(0)

        # Make it visited
        visited[number] = False 

        # Go through the 2d list in that row 
        for i in range(len(adj[number])):
            
            # Get the sides it goes to and the value for each Edge
            v = adj[number][i].v
            w = adj[number][i].w

            if dList[number] + w < dList[v]:

                dList[v] = dList[number] + w

                if not visited[v]:

                    temp.append(v)
                    visited[v] = True


    return dList[end]

######################



class zombie(object):

    # Constructor
    def __init__(self, app, name, hp, speed, spriteIndex, color):

        self.name = name
        self.hp = hp
        self.speed = speed
        self.spriteIndex = spriteIndex 
        self.color = color
        
        # Its image
        self.img = app.zombieImg

        # The zombie's x, y cords and the row it is on 
        self.x = app.width + 5
        self.row = random.randint(0, 4)
        self.y = app.topMargin + self.row * app.cellHeight + app.cellHeight / 2


    # Check if a zombie is hit
    def checkHit(self, app, bulletX, bulletY, damage):

        # If it is hit, reduce the zombie's hp by damage
        if dist(self.x, self.y, bulletX, bulletY) <= 15:
            self.hp -= damage 

            # If the zombie dies put if off screen
            if self.hp <= 0: #self.x = -100
                
                app.zomList[self.row].remove(self)

            return True

        return False


    # Draw a zombie on the lawn
    def draw(self, canvas):

        canvas.create_image(self.x, self.y, 
                            image = ImageTk.PhotoImage(self.img))
        canvas.create_text(self.x + 5, self.y + 5, 
                            text = self.name, font = "Arial 13 bold", 
                            fill = self.color)



#################################################
# Zombies
#################################################



#################################################
# Main
#################################################

# Setting the model 
def appStarted(app):


    # Keep track which screen we're on
    app.mode = "startScreen"    

    # All of the url and images used 
    urlHelper(app)


    # The cell width and height of the lawn grid
    # Note that b/c each cell is slighly different than the other, 
    # we will use two magic numbers here
    app.cellWidth, app.cellHeight = 90, 105


    # Total number of rows and cols of the lawn(grid)
    app.rows, app.cols = 5, 9 

    # Top and left margins of the lawn
    app.topMargin, app.leftMargin = 105, 95



    # A dict that keep track of the plants planted on each row 
    app.plantsGrid = dict()

    # A list of bullet shot by the plants
    app.bullets = []


    # Bullet speed
    app.bulletSpeed = 40

    # A dict that keep track of the zombies on each row 
    app.zomList = dict()

    # The last row a zombie was genarated on 
    app.lastRow = 0 

    # The total amount of sun the player has
    app.totalSun = 100



    # Plant selection 
    app.mouseX, app.mouseY = 0, 0
    app.plantSelected = False
    app.selectedPlant = ""



    # Timerdelay interval
    app.timer = 0       # Keep track of time passes
    app.timerDelay = 250


    # Messages to be displayed 
    app.nameMessage = "Press 'n' to put your name here!"
    app.message = "Press 'b' to input some commands!"


    # Gameover 
    app.gameOver = False

    
   
    # Projectile part
    # Learned at Office Hour and from 
    # https://en.wikipedia.org/wiki/Kinematics
 
    app.timeInAir = 3000    # The time the projectile will stay in air

    app.ballX, app.ballY, app.ballR = 0, 0, 10
    app.startX, app.startY, app.endX, app.endY = 0, 0, 0, 0

    app.dx = app.endX - app.startX              # Total change of x cord
                                                # x acceleration - no acc.for x
    app.vX = app.dx / (app.timeInAir/1000)      # Velocity of x cord

    app.dy = app.endY - app.startY              # Total change of the y cord
    app.yAcceleration = 5                       # y acceleration
    app.vY = (app.dy - 1/2 * app.yAcceleration * (app.timeInAir/1000)**2) / (app.timeInAir/1000)
                            # Y cord velecity



    # User cannot resize the canvas
    app._root.resizable(False, False) 



# Store and load all of the needed urls and images
def urlHelper(app):

    # Start Screen Image from https://www.pinterest.com/pin/207587864052800140/
    #startUrl = "https://i.pinimg.com/originals/ff/2a/f4/ff2af4c06b41232e083d6e44a6f0c40e.png"
    #app.img1 = app.loadImage(startUrl).resize((app.width, app.height))

    # Menu Image from https://plantsvszombies.fandom.com/wiki/Adventure_Mode
    menuUrl = "D:\Others\PythonPrograms\PVZ2\StartScreen.png"
    app.menu = app.loadImage(menuUrl).resize((app.width, app.height))


    # Lawn Images from https://plantsvszombies.fandom.com/wiki/Areas#Plants_vs._Zombies
    lawn1 = "D:\Others\PythonPrograms\PVZ2\DayLawn.jpg"
    lawn2 = "D:\Others\PythonPrograms\PVZ2\FarFutureLawn.png"
    lawn3 = "D:\Others\PythonPrograms\PVZ2\LostCityNightLawn.png"
    app.lawnChoices = [lawn1, lawn2, lawn3]
    app.lawn = app.loadImage(app.lawnChoices[random.randint(0, 2)]).resize((app.width, app.height))


    # Plants images are taken from 
    # https://plantsvszombies.fandom.com/wiki/Category:Galleries

    # Sunflower 
    sunF = "D:\Others\PythonPrograms\PVZ2\Sunflower.png"
    app.sfImg = app.loadImage(sunF)

    singleSunF = "D:\Others\PythonPrograms\PVZ2\SingleSunflower.png"
    app.singlesfImg = app.loadImage(singleSunF).resize((90, 90))


    # Plants images are taken from 
    # https://plantsvszombies.fandom.com/wiki/Category:Galleries

    # NOTE: all image processing methods below are learned from 
    # https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html


    # Peashooter 
    peaS = "D:\Others\PythonPrograms\PVZ2\Peashooter.png"
    app.psImg = app.loadImage(peaS)

    singlePeaS = "D:\Others\PythonPrograms\PVZ2\SinglePeashooter.png"
    app.singlepsImg = app.loadImage(singlePeaS).resize((90, 90))


    # Plants images are taken from 
    # https://plantsvszombies.fandom.com/wiki/Category:Galleries
    # CabbagePult
    cabP = "D:\Others\PythonPrograms\PVZ2\CabbagePult.png"
    app.singlecabPImg = app.loadImage(cabP).resize((90, 90))


    # Sun
    # Image taken from https://plantsvszombies.fandom.com/wiki/Sun
    sunUrl = "D:\Others\PythonPrograms\PVZ2\Sun.png"
    app.sun = app.loadImage(sunUrl).resize((90, 90))


    # Game over screen
    # Image taken from https://www.pinterest.com/pin/527976756296840361/
    gameOverUrl = "D:\Others\PythonPrograms\PVZ2\GameOver.jpg"
    app.gameOverImg = app.loadImage(gameOverUrl).resize((app.width, app.height))


    # Zombie
    # Image taken from https://plantsvszombies.fandom.com/wiki/Browncoat_Zombie/Gallery#Plants_vs._Zombies
    zombieUrl = "D:\Others\PythonPrograms\PVZ2\Zombie.png"
    app.zombieImg = app.loadImage(zombieUrl).resize((70, 70))



runApp(width = 960, height = 640)
