from tkinter import *

window = Tk()

# создание кнопки выхода
btn_end = Button(window, text = 'Выйти', command=exit) 

# менеджер геометрии
btn_end.pack(padx = 150, pady = 20)

def tog():
	if window.cget('bg') == 'green': 
		window.configure(bg = 'yellow') 
	else:
		window.configure(bg = 'green')

btn_tog = Button(window, text = 'Изменить', command=tog) 
btn_tog.pack(padx = 150, pady = 20)


window.mainloop()