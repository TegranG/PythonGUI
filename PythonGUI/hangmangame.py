from asyncio import wait_for
from cgitb import text
from timeit import repeat
import tkinter as tk
import random
def gamerun(): #make it to a libary to be called my pygui
	#list of preset words for singleplayer
	preset1 = ["g","r","i","t"]
	preset2 = ["m","o","r","b","i","u","s"]
	preset3 = ["i","s","o","y","a","n","a","t","e"]
	preset4 = ['s','p','y','x','f','a','m','i','l','y']
	preset5 = ['p','r','i','k','e','t']
	preset6 = ['s','c','r','u','m','p','t','i','o','u','s']
	preset7 = ['z','y','g','o','t','e']
	preset8 = ['f','o','r','i','c','a','t','e']
	gamewin = tk.Tk() #chose between multi or single player
	twoscreen = tk.Tk()# multiplayer's screen 
	singlescreen = tk.Tk() #single player screen
	singlescreen.iconify() #hide the screen to be used later
	twoscreen.iconify() #hide the screen to be used later
	screenx = gamewin.winfo_screenwidth()
	def closeone(): #close the singleplayer window when button is clicked
		singlescreen.destroy()
	pass
	def closetwo(): #close the multiplayer window when button is clicked
		twoscreen.destroy()
	pass
	def singleclicked(): #start single player game/window
		gamewin.destroy() #destroy the game mode choosing screen
		global randomword #make varible global
		singlescreen.deiconify() #maximize
		singlescreen.attributes('-fullscreen', True)
		text1 = tk.Label(singlescreen, text = 'Guess the Word, a computer has alraedy randomnized it for you, all you need to do is guess. Good Luck!')
		randomword = random.randint(1,8) #pick a number from 1 to 8 
		print(randomword)
		text1.pack()
		#what ever the randomnumber is use that corresponding word
		#ex). if the number is 4, chose word 4, 'spyxfamily'
		if randomword == 1:
			randomword = preset1
		elif randomword == 2:
			randomword = preset2
		elif randomword == 3:
			randomword = preset3
		elif randomword == 4:
			randomword = preset4
		elif randomword == 5:
			randomword = preset5
		elif randomword == 6:
			randomword = preset6
		elif randomword == 7:
			randomword = preset7
		else:
			randomword = preset8
		pass
		i = 0# my own for loop like a java script for loop works
		global randomwordlen
		
		randomwordlen = len(randomword)
		global wordguess2
		wordguess2 = list()
		
		while i < randomwordlen:
			wordguess2.append("_")
			i += 1
	pass
	def singlestart(): #start the single player game algorithim
		tries2 = 10
		userin = nameboxsingle.get() #users input
		print(userin)
		#infinate tries
		while tries2 > 0:
			for score1 in range(randomwordlen): #filter through the list to see if the character the user choosed is in the random word
				if userin == randomword[score1]: #if the user's choice of letter is = to any letter in the word
					print("worked")
					wordguess2.insert(score1,randomword[score1])
					wordguess2.pop(score1 +1)#python list suck
					print(wordguess2) #your list
					singleplayertext.config(text = wordguess2)
				pass
			if wordguess2 == randomword: #if the users list that contains all the input of letters = the word, if the user guessed the right word
				print("you won")
				closebut2 = tk.Button(singlescreen,text = "Close", command = closeone)
				closebut2.pack()
				closebut2.anchor(tk.CENTER)
			pass
			break

	def twoplayer(): #start coup mode
		gamewin.destroy()
		twoscreen.attributes('-fullscreen', True)
		twoscreen.state("zoomed")
		text2 = tk.Label(twoscreen,text = 'Player 1 input a word into the textbox')
		text2.pack() 
	pass

	def getword(): #getword from textbox that player 1 inputs, the word that the next person needs to guess
		wordneeded = namebox.get()
		if wordneeded.islower() == False: #makes sure the word to be in lowercase or else it becomes an unfair advantage
			text2 = tk.Label(twoscreen,text = "dont type in upercase, it needs to all be lowercase")
			text2.pack()
			text2.update()
			text2.place(x = twoscreen.winfo_screenwidth()/2 - text2.winfo_width()/2, y = 100)
		else: #if its all lower case began the game!
			global wordguess
			wordguess = namebox.get()
			startgamemulti.pack()
			startgamemulti.update()
			startgamemulti.place(x = screenx/2 - startgamemulti.winfo_width()/2, y = 150)
			
			text3.pack()
			text3.update()
			text3.place(x = twoscreen.winfo_screenwidth()/2 - text3.winfo_width()/2, y = 120)
		pass
	pass
	def gamestartmultiplayer(): #start running the games algorithm
		guessbox.pack()
		guessbox.update()
		guessbox.place(x = screenx/2 - guessbox.winfo_width()/2, y = 180) #center the player 2's character input
		print("began game")
		guessbutton = tk.Button(twoscreen,text = "guess letter?",command = gamebegin)
		guessbutton.pack()
		guessbutton.update()
		guessbutton.place(x = screenx/2 - guessbutton.winfo_width()/2, y = 220)
		global wordlistlen#global these varibles to line 133
		global wordlist
		wordlist = list(wordguess)
		wordlistlen = len(wordlist)
		print(wordlistlen)
		print(wordlist)
		global rightguess
		global rightguesslen
		rightguess = list() #set right guess to a list of user inputs
		rightguesslen = len(rightguess)
		i = 0
		while i < wordlistlen:#make the list empty
			rightguess.append("_")
			i += 1
	pass
	wordin = tk.Label(twoscreen)
	wordin.place(x = screenx/2, y = 1000)
	def gamebegin(): #ok now the game begins!
		text3.config(text = "The word is below, along with the empty spots")
		namebox.destroy()
		guesschar = guessbox.get()
		tries = 10
		while tries > 0: #already explained all of this
			falied = 0
			for score in range(wordlistlen):
				if guesschar == wordlist[score]:
					print("worked")
					rightguess.insert(score,wordlist[score])
					rightguess.pop(score +1)
					print(wordin.winfo_rooty()) 
					text3.place(x = twoscreen.winfo_screenwidth()/2 - text3.winfo_width()/2, y = 120)
					print(wordin.winfo_rootx())
				pass
			if rightguess == wordlist:
				print("you won")
				text3.config(text = "Congrats you won, the word was " + wordguess)
				closebut = tk.Button(twoscreen,text = "Close", command = closetwo)
				closebut.pack()
				closebut.anchor(tk.CENTER)
				
			pass
			break
		wordin.pack()
		wordin.config(text = rightguess)
	pass
	#all of the tkinter elements!
	text3 = tk.Label(twoscreen, text = "Player 2, input one letter at a time to guess the word, click start to begin! Good Luck!")
	guesscharstr = tk.StringVar()
	guessbox = tk.Entry(twoscreen,textvariable = guesscharstr)
	gamewin.attributes('-fullscreen', True)
	singlebutton = tk.Button(gamewin,text = 'SinglePlayer',command = singleclicked)
	singlebutton.pack()
	singlebutton.anchor(tk.NW)
	multiplayer = tk.Button(gamewin, text = 'Multiplayer', command = twoplayer)
	multiplayer.pack()
	namein = tk.StringVar()
	namebox = tk.Entry(twoscreen,textvariable = namein,show = "*")
	namebox.pack()
	print(screenx)
	namebox.update()
	namex = namebox.winfo_width()/2
	print(namex)
	namebox.place(x = screenx/2 - 113/2, y = 35) #check why it doesnt work
	multiplayer.anchor(tk.NE)
	confirmword = tk.Button(twoscreen, text = 'confirm your word!',command = getword)
	confirmword.pack()
	startgamemulti = tk.Button(twoscreen,text = "Start Game!", command = gamestartmultiplayer)
	nameinsingle = tk.StringVar()
	nameboxsingle = tk.Entry(singlescreen,textvariable= nameinsingle)
	namebox.update()
	nameboxsingle.place(x = screenx/2 - namex/2, y = 20)
	nameboxsingle.pack()
	button5 = tk.Button(singlescreen, text = 'Start!', command = singlestart)
	button5.place(x = screenx/2 - button5.winfo_width()/2, y = 40)
	button5.pack()
	while True:#constantly check to update the values of the text
		confirmword.update()
		break
	print(confirmword.winfo_width())
	confirmword.place(x = screenx/2 - confirmword.winfo_width()/2, y = 65)
	singleplayertext = tk.Label(singlescreen)
	singleplayertext.pack()
	gamewin.mainloop()
pass