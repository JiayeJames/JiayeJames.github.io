# from cmu_112_graphics import *

# def appStarted(app): 
#     app.messages = ['appStarted']

# def appStopped(app):
#     app.messages.append('appStopped')
#     print('appStopped!')

# def keyPressed(app, event):
#     app.messages.append('keyPressed: ' + event.key)

# def keyReleased(app, event):
#     app.messages.append('keyReleased: ' + event.key)

# def mousePressed(app, event):
#     app.messages.append(f'mousePressed at {(event.x, event.y)}')

# def mouseReleased(app, event):
#     app.messages.append(f'mouseReleased at {(event.x, event.y)}')

# def mouseMoved(app, event):
#     app.messages.append(f'mouseMoved at {(event.x, event.y)}')

# def mouseDragged(app, event):
#     app.messages.append(f'mouseDragged at {(event.x, event.y)}')


# def redrawAll(app, canvas):
#     font = 'Arial 20 bold'
#     canvas.create_text(app.width/2,  30, text='Events Demo', font=font)
#     n = min(10, len(app.messages))
#     i0 = len(app.messages)-n
#     for i in range(i0, len(app.messages)):
#         canvas.create_text(app.width/2, 100+50*(i-i0),
#                            text=f'#{i}: {app.messages[i]}',
#                            font=font)

# runApp(width=600, height=600)



# This demos app.getUserInput(prompt) and app.showMessage(message)

# from cmu_112_graphics import *
# from tkinter import*

# def appStarted(app):

#     url1 = "http://www.cs.cmu.edu/~112/notes/sample-spritestrip.png"
#     app.img1 = app.loadImage(url1)
#     app.img2 = app.scaleImage(app.img1, 1/10)
#     app.message = "Enter 'b' to input some commands!"

# def keyPressed(app, event):

#     key = event.key

#     if key == "b":

#         name = app.getUserInput("Enter 'kill' to kill all existing zombies!\nOr click cancel.")

#         if name == None:
#             app.message = "Nothing is entered!"

#         else:
#             app.showMessage("Boom! all zoms are 'dead' now!")
#             app.message = f"Command: {name}"



# def redrawAll(app, canvas):

#     canvas.create_text(app.width / 2, app.height / 2,
#                        text = app.message, font = 'Arial 24 bold')

#     canvas.create_image(app.width / 2 - 100, app.height / 2 + 100, 
#                         image = ImageTk.PhotoImage(app.img2))

# runApp(width = 600, height = 400)


# This demos using getpixel and putpixel

# from cmu_112_graphics import *

# def appStarted(app):
#     url = 'https://tinyurl.com/great-pitch-gif'
#     app.image1 = app.loadImage(url)

#     # now let's make a copy that only uses the red part of each rgb pixel:
#     app.image1 = app.image1.convert('RGB')
#     app.image2 = Image.new(mode='RGB', size=app.image1.size)
#     for x in range(app.image2.width):
#         for y in range(app.image2.height):
#             r,g,b = app.image1.getpixel((x,y))
#             app.image2.putpixel((x,y),(r,0,0))

# def redrawAll(app, canvas):
#     canvas.create_image(200, 300, image=ImageTk.PhotoImage(app.image1))
#     canvas.create_image(500, 300, image=ImageTk.PhotoImage(app.image2))

# runApp(width=700, height=600)

# This demos creating a new blank image and using PIL ImageDraw

# from cmu_112_graphics import *

# def appStarted(app):
#     imageWidth, imageHeight = app.width//3, app.height//2
#     bgColor = (0, 255, 255) # cyan
#     app.image1 = Image.new('RGB', (imageWidth, imageHeight), bgColor)
#     # Now that we created the image, let's use ImageDraw to draw in it
#     # See https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
#     draw = ImageDraw.Draw(app.image1)
#     draw.line((0, 0, imageWidth, imageHeight), width=10, fill=(255, 0, 0))
#     draw.line((0, imageHeight, imageWidth, 0), width=10, fill=(0, 0, 255))
#     # And now we will create a scaled copy to show this is a normal image
#     app.image2 = app.scaleImage(app.image1, 2/3)

# def redrawAll(app, canvas):
#     canvas.create_image(200, 300, image=ImageTk.PhotoImage(app.image1))
#     canvas.create_image(500, 300, image=ImageTk.PhotoImage(app.image2))

# runApp(width=700, height=600)

# This demos getSnapshot and saveSnapshot

# This demos using modes (aka screens).

# from cmu_112_graphics import *
# import random

# ##########################################
# # Splash Screen Mode
# ##########################################

# def splashScreenMode_redrawAll(app, canvas):
#     font = 'Arial 26 bold'
#     canvas.create_text(app.width/2, 150, text='This demos a ModalApp!', font=font)
#     canvas.create_text(app.width/2, 200, text='This is a modal splash screen!', font=font)
#     canvas.create_text(app.width/2, 250, text='Press any key for the game!', font=font)

# def splashScreenMode_keyPressed(app, event):
#     app.mode = 'gameMode'

# ##########################################
# # Game Mode
# ##########################################

# def gameMode_redrawAll(app, canvas):
#     font = 'Arial 26 bold'
#     canvas.create_text(app.width/2, 20, text=f'Score: {app.score}', font=font)
#     canvas.create_text(app.width/2, 60, text='Click on the dot!', font=font)
#     canvas.create_text(app.width/2, 100, text='Press h for help screen!', font=font)
#     canvas.create_text(app.width/2, 140, text='Press v for an MVC Violation!', font=font)
#     canvas.create_oval(app.x-app.r, app.y-app.r, app.x+app.r, app.y+app.r,
#                        fill=app.color)
#     if app.makeAnMVCViolation:
#         app.ohNo = 'This is an MVC Violation!'

# def gameMode_timerFired(app):
#     moveDot(app)

# def gameMode_mousePressed(app, event):
#     d = ((app.x - event.x)**2 + (app.y - event.y)**2)**0.5
#     if (d <= app.r):
#         app.score += 1
#         randomizeDot(app)
#     elif (app.score > 0):
#         app.score -= 1

# def gameMode_keyPressed(app, event):
#     if (event.key == 'h'):
#         app.mode = 'helpMode'
#     elif (event.key == 'v'):
#         app.makeAnMVCViolation = True

# ##########################################
# # Help Mode
# ##########################################

# def helpMode_redrawAll(app, canvas):
#     font = 'Arial 26 bold'
#     canvas.create_text(app.width/2, 150, text='This is the help screen!', font=font)
#     canvas.create_text(app.width/2, 250, text='(Insert helpful message here)', font=font)
#     canvas.create_text(app.width/2, 350, text='Press any key to return to the game!', font=font)

# def helpMode_keyPressed(app, event):
#     app.mode = 'gameMode'

# ##########################################
# # Main App
# ##########################################

# def appStarted(app):
#     app.mode = 'splashScreenMode'
#     app.score = 0
#     app.timerDelay = 50
#     app.makeAnMVCViolation = False
#     randomizeDot(app)

# def randomizeDot(app):
#     app.x = random.randint(20, app.width-20)
#     app.y = random.randint(20, app.height-20)
#     app.r = random.randint(10, 20)
#     app.color = random.choice(['red', 'orange', 'yellow', 'green', 'blue'])
#     app.dx = random.choice([+1,-1])*random.randint(3,6)
#     app.dy = random.choice([+1,-1])*random.randint(3,6)

# def moveDot(app):
#     app.x += app.dx
#     if (app.x < 0) or (app.x > app.width): app.dx = -app.dx
#     app.y += app.dy
#     if (app.y < 0) or (app.y > app.height): app.dy = -app.dy

# runApp(width=600, height=500)


# This demos sprites using Pillow/PIL images
# See here for more details:
# https://pillow.readthedocs.io/en/stable/reference/Image.html

# This uses a spritestrip from this tutorial:
# https://www.codeandweb.com/texturepacker/tutorials/how-to-create-a-sprite-sheet

# from cmu_112_graphics import *

# def appStarted(app):
#     url = 'http://www.cs.cmu.edu/~112/notes/sample-spritestrip.png'
#     spritestrip = app.loadImage(url)
#     app.sprites = [ ]
#     for i in range(6):
#         sprite = spritestrip.crop((30+260*i, 30, 230+260*i, 250))
#         app.sprites.append(sprite)
#     app.spriteCounter = 0

# def timerFired(app):
#     app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)

# def redrawAll(app, canvas):
#     sprite = app.sprites[app.spriteCounter]
#     canvas.create_image(200, 200, image=ImageTk.PhotoImage(sprite))

# runApp(width=400, height=400)



from cmu_112_graphics import *

def appStarted(app):
    
    app.timeInAir = 5000   

    app.dx = 200              
    app.xAcceleration = 0  
    app.vX = app.dx / (app.timeInAir/1000)      

    app.dy = 100    # v0t + 1/2 a t**2 = 100, solve for v sub y 
    app.yAcceleration = 3 
    app.vY = (app.dy - 1/2 * app.yAcceleration * (app.timeInAir/1000)**2) / (app.timeInAir/1000)


    app.timerDelay = 1000

    app.ballX, app.ballY = 100, 100


def timerFired(app):

    app.yAcceleration -= 0.5

    app.ballX += app.vX
    app.ballY += app.vY

    print(app.vX, app.vY, app.ballX, app.ballY)


def redrawAll(app, canvas):

    if 100 <= app.ballX <= 300:
        canvas.create_oval(app.ballX - 10, app.ballY - 10, app.ballX + 10, app.ballY + 10, 
                       fill = "green")


runApp(width=400, height=400)




'''

dx is constant 
dy start off big and gets smaller, reach zero and continue going

dx = 15
dy = 40

per timerFired 
subtract d = 5



'''

# d = dict()

# d[1] = [1, 2, 3, 5]
# d[3] = [1, 2, 3, 5]
# d[2] = [1, 2, 3, 5]
# d[4] = [1, 2, 3, 5]

# for i in range(1, len(d) + 1):

#     if 3 in d[i]:
#         d[i].pop(3)