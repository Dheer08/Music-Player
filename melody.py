#you cannot use both pack layout and grid layout manager directly without frames in the same file
#you can use Grid layout manager to do buttons layout  by basing in rows and columns
from tkinter import *
import tkinter.messagebox
from pygame import mixer
import os
from tkinter import filedialog

root=Tk()	#creating a first window

menubar=Menu(root)
root.config(menu=menubar) 

def browse_file():
	global filename
	filename=filedialog.askopenfilename()
	print(filename)

subMenu =Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="Open",command=browse_file)
subMenu.add_command(label="Exit",command=root.destroy)
def about_us():
	tkinter.messagebox.showinfo('our title','this is music player Created by Dheer by using Tkinter\nIf u want to follow me click here')

subMenu =Menu(menubar)
menubar.add_cascade(label="Help",menu=subMenu)
subMenu.add_command(label="About us",command=about_us)

mixer.init() #initializing is necessary for mixer
root.geometry('300x360')
root.title("Melody")
root.iconbitmap(r'melody.ico')

text=Label(root,text="let's make some noise!")
text.pack(pady=10)

playPhoto= PhotoImage(file='play-button.png')
stopPhoto=PhotoImage(file='stop.png')
pausePhoto=PhotoImage(file='pause.png')
rewindPhoto=PhotoImage(file='Rewind.png')
#labelphoto=Label(root,image=photo)
#labelphoto.pack()

def play_music():
	
	try:
		paused #checks whether the pause variable is initilaized or not
	except NameError: # if not initilized then executes except condition
		try:
			mixer.music.load(filename)
			mixer.music.play()
			statusbar['text']="Playing music"+ '-'+os.path.basename(filename)

		except:
			tkinter.messagebox.showerror('File not found','Melody could not find the file.')
	else: # if initilize then it goes to else condition
		mixer.music.unpause()
def stop_music():
	mixer.music.stop()
	statusbar['text']="music is stopped"
def set_vol(val):
	volume =int(val)/100
	mixer.music.set_volume(volume)
#set volume of mixer only takes volume from 0 to 0.999
def pause_music():
	global paused
	paused=TRUE
	statusbar['text']="Music paused"
	mixer.music.pause()	
def rewind_music():
	pass

middleframe=Frame(root,relief=SUNKEN,borderwidth=0)
middleframe.pack(padx=10,pady=10)

play =Button(middleframe,image=playPhoto,command=play_music)
play.pack(side=LEFT,padx=10);
stop=Button(middleframe,image=stopPhoto,command=stop_music)
stop.pack(side=LEFT,padx=10);
pause=Button(middleframe,image=pausePhoto,command=pause_music)
pause.pack(side=RIGHT,padx=10);
rewind=Button(middleframe,image=rewindPhoto,command=rewind_music)
rewind.pack(side=RIGHT,padx=10);
scale=Scale(root,from_=0,to=100,orient=HORIZONTAL,command=set_vol)
scale.set(40)
mixer.music.set_volume(40)
scale.pack(pady=10)

statusbar=Label(root,text="Welcome to melody",relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)

root.mainloop() #engaging in a loop to be created again(to persist)










