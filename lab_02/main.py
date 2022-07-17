# ИУ7-23Б Шимшир Эмирджан В-5
'''
Необходимо вычислить корни функции на отрезке [a; b] заданным методом. 
Для вычисления отрезок [a; b] делится на элементарные отрезки с шагом h. 
На каждом элементарном отрезке у функции не более одного корня. 
Для каждого элементарного отрезка, на котором есть корень, 
итерационно вычисляется приближенное значение корня с заданной точностью eps. 
Для обнаружения медленного процесса сходимости или расходимости метода
количество итераций ограничивается числом Nmax.
'''

#_______________________________________________________________________
from math import *
import tkinter as tk
from tkinter import ttk

import matplotlib
matplotlib.use("TkAgg")

import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import messagebox as box
#_______________________________________________________________________

# функция
def f(x):
	return eval(entry_f.get())

# разбить на отрезки
def find_intervals(a, b, h):
	x_0 = a
	x_1 = x_0 + h
	arr = []

	if f(a) == 0:
		arr.append((a, a + h))
	if f(b) == 0:
		arr.append((b - h, b))
	while (x_0 < b):

		if f(x_1) == 0:
			arr.append((x_0, x_1))
		elif f(x_0) * f(x_1) < 0:
			arr.append((x_0, x_1))
		x_0 += h
		x_1 += h
	return arr

# уточнение корней
def secant_method(a, b, eps, n_max, j):
	x_0 = a
	x_1 = b
	section = "[{:<9.4}; {:>9.4}]".format(a, b)
	error = (j + 1, section, "Error", "Error", "Error", 1)
	for i in range(n_max):
		x_2 = x_0 - (x_1 - x_0) * f(x_0) / (f(x_1) - f(x_0))
		x_0 - x_1
		x_1 = x_2
		if not (a <= x_2 <= b):
			error = (j + 1, section, "Error", "Error", "Error", 2)
		if abs(f(x_2)) < eps:
			break
	else:
		return error

	return (j + 1, section, format(x_2, "<9.4"), format(f(x_2),"<.0e"), i + 1, 0)

# запуск
def start():
	a = float(entry_a.get())
	b = float(entry_b.get())
	h = float(entry_h.get())
	n_max = int(entry_n_max.get())
	eps = float(entry_eps.get())

	arr = find_intervals(a, b, h)
	table_arr = []
	for i in range(len(arr)):
		table_arr.append(secant_method(arr[i][0], arr[i][1], eps, n_max, i))

	table = ttk.Treeview(win)
	table.grid(row=3, column=0, columnspan=6)
	heads = ["№ root", "interval", "x'", "f(x')", "N", "code"]
	table["columns"] = heads

	for header in heads:
		table.heading(header, text=header, anchor='center')
	for row in table_arr:
		table.insert("", tk.END, values=row)

	plot(a, b)

# график
def plot(a, b):

	fig = Figure(figsize=(5,5))
	a_f = fig.add_subplot()
	X = np.linspace(a, b, int((b-a)*1000))

	Y = [f(i) for i in X]
	Y = np.array(Y)
	Y_diff_1 = np.diff(Y)
	y_diff_2 = np.diff(Y_diff_1)
	
	
	
	mask = np.abs(Y) < 1e-3
	mask_1 = np.abs(Y_diff_1) < 1e-5
	mask_2 = np.abs(y_diff_2) < 1e-8
	
	a_f.plot(X, Y)

	a_f.scatter(X[:-1][mask_1], Y[:-1][mask_1], color='green', s=40, marker='o', label="extremes")
	a_f.scatter(X[:-2][mask_2], Y[:-2][mask_2], color='red', s=40, marker='o', label="inflection points")
	a_f.scatter(X[mask], Y[mask], color='orange', s=20, marker='o', label="zeros")

	a_f.legend()
	a_f.grid()
	a_f.set_ylabel(str(entry_f.get()))
	a_f.set_xlabel("x")
	canvas = FigureCanvasTkAgg(fig, win)
	canvas.draw()
	canvas.get_tk_widget().grid(row=6, column=0, rowspan=3, columnspan = 6, stick='we', padx=20, pady=20)
		

def code_msg():
    box.showinfo('Error codes',
                 "0 - root's found: OK\n"
                 "1 - too many iterations\n"
                 "2 - out of the interval\n")
 

# Создание окна
win = tk.Tk()

win.geometry('1400x830')
# Блокировка измениения размера
win.resizable(width=False, height=False)
# заголовок
win.title('Lab_2_2')

mainmenu = tk.Menu(win)
win.config(menu=mainmenu)
  
# Меню перевода
pmenu = tk.Menu(mainmenu)
pmenu.add_command(label='Error codes', command=code_msg) 
mainmenu.add_cascade(label='Info', menu = pmenu)


# создание надписи ВВОД
lb_f = tk.Label(win, text='f(x):')
lb_f.grid(row=0, column=0)

# Создание поля ввода
entry_f = tk.Entry(win)
entry_f.grid(row=1, column=0)

# создание надписи ВВОД
lb_a = tk.Label(win, text='a:')
lb_a.grid(row=0, column=1)

# Создание поля ввода
entry_a = tk.Entry(win)
entry_a.grid(row=1, column=1)

# создание надписи ВВОД
lb_b = tk.Label(win, text='b:')
lb_b.grid(row=0, column=2)

# Создание поля ввода
entry_b = tk.Entry(win)
entry_b.grid(row=1, column=2)

# создание надписи ВВОД
lb_h = tk.Label(win, text='h:')
lb_h.grid(row=0, column=3)

# Создание поля ввода
entry_h = tk.Entry(win)
entry_h.grid(row=1, column=3)

# создание надписи ВВОД
lb_n_max = tk.Label(win, text='n_max:')
lb_n_max.grid(row=0, column=4)

# Создание поля ввода
entry_n_max = tk.Entry(win)
entry_n_max.grid(row=1, column=4)

# создание надписи ВВОД
lb_eps = tk.Label(win, text='eps:')
lb_eps.grid(row=0, column=5)

# Создание поля ввода
entry_eps = tk.Entry(win)
entry_eps.grid(row=1, column=5)

enter_button = tk.Button(text='start', command=start)
enter_button.grid(row=2, column=0, columnspan=6, stick='we')

table = ttk.Treeview(win)
table.grid(row=3, column=0, columnspan=6)
heads = ["№ root", "interval", "x'", "f(x')", "N", "code"]
table["columns"] = heads

for header in heads:
	table.heading(header, text=header, anchor='center')
table_arr = [("", "", "", "", "", "")]
for row in table_arr:
	table.insert("", tk.END, values=row)

# запуск обработчика обытий
win.mainloop()	

	

