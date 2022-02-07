from tkinter import *

window = Tk()
window.title('Example') 
window.geometry('600x400+100+200') 

import tkinter.messagebox as box

def showdata():
	a = ent1.get()
	ent1.delete(0, len(a))
	ent1.insert(0, "!" + a + "!")

lbl1 = Label(window, text='The first example') 
lbl1.grid(row = 0, column = 0)
ent1 = Entry()
ent1.grid(row = 0, column = 1)
btn1 = Button(window, text = 'Ввести данные', command=showdata) 
btn1.grid(row = 1, column = 1)
window.mainloop()