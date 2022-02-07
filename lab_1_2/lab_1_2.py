from tkinter import *

window = Tk()
window.title('Example') 
window.geometry('600x400+100+200') 

import tkinter.messagebox as box

def showdata(event):
	box.showinfo('Введенные данные', ent1.get())
	
lbl1 = Label(window, text='The first example') 
lbl1.grid(row = 0, column = 0)
ent1 = Entry()
ent1.grid(row = 0, column = 1)
btn1 = Button(window, text = 'Ввести данные', command=exit) 
btn1.grid(row = 1, column = 1) 
btn1.bind('<Button-1>',showdata)
window.mainloop()