from tkinter import *

window = Tk()
window.title('Example') 
window.geometry('600x400+100+200')

import tkinter.messagebox as box 

def showtext(event):
	box.showinfo('Text info', txt.get(1.0,END)) 
	txt.delete(2.0,2.3)

txt = Text(width=25, height=5, fg='black', wrap=WORD) # default 80*24
txt.insert(2.0, 'It is a good day')
txt.pack() 
txt.bind('<Return>',showtext) 
window.mainloop()