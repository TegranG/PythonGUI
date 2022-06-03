#pong code below
from inspect import FullArgSpec
from tkinter import *
import random
import time

def pongstart():
    # Define ball properties and functions
    class Ball:
        def __init__(self, canvas, color, size, paddle):
            self.canvas = canvas
            self.paddle = paddle #paddle user controls
            self.id = canvas.create_oval(6, 6, size, size, fill= 'white')
            self.canvas.move(self.id, 0, 0)
            self.xspeed = random.randrange(-6,6) #some randomness
            self.yspeed = -1
            self.hit_bottom = False
            self.score = 0

        def draw(self):
            self.canvas.move(self.id, self.xspeed, self.yspeed)
            pos = self.canvas.coords(self.id)
            if pos[1] <= 0:
                self.yspeed = 10
            if pos[3] >= tk.winfo_screenheight(): #hits the side of the montior, set the speed to 0
                self.hit_bottom = True
            if pos[0] <= 0:
                self.xspeed = 10
            if pos[2] >= tk.winfo_screenwidth(): # if its lower than the size of the monitor
                self.xspeed = -10
            if self.hit_paddle(pos) == True:
                self.yspeed = -10 * self.score #speed up by the value of score
                self.score += 1
                self.xspeed = self.xspeed*2 + self.score
                

        def hit_paddle(self, pos):
            paddle_pos = self.canvas.coords(self.paddle.id)
            if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]: #paddle hits to, reflet ball
                if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                    return True
            return False

    # Define paddle properties and functions
    class Paddle: #human paddle
        def __init__(self, canvas, color):
            self.canvas = canvas
            self.id = canvas.create_rectangle(0,0, 200, 10, fill='white')
            self.canvas.move(self.id, tk.winfo_screenwidth()/2, tk.winfo_screenheight() / 1.2)#paddle y location and x locaiton, it starts in the middle and lowers to a certain y on the monitor
            self.xspeed = 0
            self.canvas.bind_all('<KeyPress-Left>', self.move_left)
            self.canvas.bind_all('<KeyPress-Right>', self.move_right)
        def draw(self):
            self.canvas.move(self.id, self.xspeed, 0)
            pos = self.canvas.coords(self.id)
            if pos[0] <= tk.winfo_screenwidth():
                self.xspeed = 0 #paddle hits side, set to 0
            if pos[2] >= tk.winfo_screenheight():
                self.xspeed = 0 #no reason for this

        def move_left(self, evt):
            self.xspeed = -20
        def move_right(self, evt):
            self.xspeed = 20

    # Create window and canvas to draw on
    tk = Tk()
    tk.state("zoomed")#zoom it into prespective
    tk.title("Drunk Pong")
    tk.attributes('-fullscreen', True)#fullscreen
    canvas = Canvas(tk, width= tk.winfo_screenwidth(), height= tk.winfo_screenheight(), bd=0, bg='black')#set the canvas to be the size of the screen and set it to black because it looks cool 😎
    canvas.pack()
    label = canvas.create_text(5, 5,fill = 'white',anchor=NW, text="Score: 0")#anchor the text to the top left
    tk.update()
    paddle = Paddle(canvas, 'blue')
    ball = Ball(canvas, 'red', 25, paddle) #size of bol

    # Animation loop
    while ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
        canvas.itemconfig(label, text="Score: "+str(ball.score), font =("ibm plex sans",35))
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)#wait a bit then close

    # Game Over
    tk.update()
    go_label = canvas.create_text(tk.winfo_screenheight(),tk.winfo_screenwidth(),text="GAME OVER",font=("ibm plex sans",40))
    time.sleep(1)
    tk.destroy()
pass