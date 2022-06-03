from gettext import gettext
from multiprocessing.connection import wait
from operator import truediv
from time import sleep
import tkinter as tk
import os
from tkinter.messagebox import showinfo
from turtle import circle, color, width
from tkinter import Tk,Label
from tkinter import *
#from snakegame import startsnake
from ponggame import pongstart #import the file that runs the game, it needs to be in the same directory as the guiapp
from hangmangame import gamerun #import the file that runs the game, it needs to be in the same directory as the guiapp
root = tk.Tk() #root that has the start button
root1 = tk.Tk() #root contains the ui to open the games
root1.iconify() #hide it
#find wtf are we
filedir = os.getcwd()
print(filedir)
#printmsg def
def printmsg():
    showinfo(title = "Hi", message = 'hello gamers')
pass

pass    
def start():  #start the app and close the start screen
    root.destroy()
    root1.state("zoomed")
    autosetting(root1)
    fullscreen(root1)
pass
#root properties below
root.title("test")
def autosetting(window1):
    window1.anchor()
    window1.resizable(False,False)
    rooth = 600 #desired hieght
    rootw = 400 #desired width
    #center window1 code
    screenheight = window1.winfo_screenheight() #height of screen
    screenwidth = window1.winfo_screenwidth() #width of screen
    screenwidthcenter = int(screenwidth/2 - rooth/2) #get the center of screen, line 12-13
    print(screenwidth)
    screenhieghtcenter = int(screenheight/2 - rooth/2)
    print(screenheight)
    window1.geometry(f'{rootw}x{rooth}+{screenwidthcenter}+{screenhieghtcenter}') #use the integers and convert them to sting using  'f' to be used in the screen geometry
pass
def fullscreen(window1): #fullscreen a window of the users choice
    window1.attributes('-fullscreen',True)
pass
xcenter = root1.winfo_screenwidth() /2 #get the center of the monitor x
ycenter = root1.winfo_screenheight() /2 #get the center of the monitor y 
xcenterstr = str(xcenter) #convert it to a string
ycenterstr = str(ycenter) #convert it to a string
xtot = root1.winfo_screenwidth()
ytot = root1.winfo_screenheight()
print("middle of x in your monitor is " + xcenterstr)
print("middle of y in your monitor is " + ycenterstr)
def getText(): #get text from the namebox that gets string from a users name
    print(namebox.get()) 
    username = namebox.get()
    text1.pack(ipadx = 5, ipady = 5)  
    text1.update() 
    text1.place(x = xcenter - text1.winfo_width()/2, y = ycenter + 10)
    print(text1.winfo_width())
    text1.config(text = 'hello ' + username)
    button4.pack(ipadx= 5, ipady = 5)
    button4.place(x = xcenter - 39/2, y = 0) #get the center of the screen and subtract with the size of the button to get the absolute center 
pass

def closert1():
    button6.pack() #pack means to display the tk funciton, so we display button6
    text1.destroy()
    namebox.destroy() 
    button3.destroy()
    button4.destroy()
    button5.pack()
    button5.config(bg = "white")
    button5.update()
    print(root1.winfo_height())
    button5.place(x = 0, y = ycenter/4) #get a 1/4 of the montior size
    button5.config(height = 50, width = 50) #change the size of the button
pass
screenx = root1.winfo_screenheight() #screen x height
autosetting(root) #center the window to the screen
#button to print hello world
#button6 = tk.Button(root1,text = "game", command = startsnake )
root1.config(bg = "#FFAA3F")
button2 = tk.Button(root1,text = 'X',bg = 'red',command = root1.destroy) #close the screen, x button
button2.pack(ipadx=20,ipady= 20, expand= True)
root1.update()
button2.place(x = root1.winfo_screenwidth() - 59, y = 0) #moves the button to the cornor
button2.config(height = 2, width = 7)#increases the size of button
root1.update()
print(button2.winfo_width()) #print the width of the button by pixel
button5 = tk.Button(root1,text = "pong", command = pongstart) #run the script "ponggame.py"
button1 = tk.Button(root,text = 'Start!',command = start) #start button on the 1st root
button1.pack(ipadx=5,ipady=5,expand=True)
button3 = tk.Button(root1,text = 'Confirm Your Name',command = getText) #grab text from textbox for name
button3.pack(ipadx = 5, ipady= 3, expand = True)
button3.place(x = xcenter - 122/2, y = ycenter + 40) #move it to the center and lower it by 40 pixels
button3.config(height = 2, width = 16)
#root1.update()
#print(button3.winfo_width())
namein = tk.StringVar() #the string varible that is used to store the input of namebox
namebox = tk.Entry(root1,textvariable = namein)
namebox.pack()#show namebox, export namebox to the screen
namebox.focus()
namebox.place(x = xcenter - 124/2, y = ycenter -4)
#root1.update()
#print(namebox.winfo_width())
button4 = tk.Button(root1, text = 'Next!', command = closert1)
button6 = tk.Button(root1,text = 'wordguesser', command = gamerun) #run hangman game from script 'hangmangame.py'
text1 = tk.Label(root1,text = "Hello ") 
text1.pack_forget()
text2 = tk.Label(root1,text = 'Word Guesser')
text2.pack_forget()

#run the root
#root1.update()
#print(button4.winfo_width())
root.mainloop() #make sure this is at the bottom so the code doesnt spawntaniously combust