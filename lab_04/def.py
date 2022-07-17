# 1 точка, много окружнситей нужно найти ближайшую к точке окружность.

import tkinter as tk
from tkinter import messagebox

rounds = []
POINT_SIZE = 2

dot = list(map(int, (input("Введите координаты точки: ").split())))

n_rounds = int(input("Введите количество окружностей: "))

for i in range(n_rounds):
	center = list(map(int, (input("Введите координаты центра {} окружности: ".format(i + 1)).split())))
	radius = int(input("Введите радиус {} окружности: ".format(i + 1)))
	rounds.append([center, radius])


def create_point(point, color):
	return canvas.create_oval(point[0] - POINT_SIZE, point[1] - POINT_SIZE,
							point[0] + POINT_SIZE, point[1] + POINT_SIZE,
							fill=color, outline='')

def create_round(roond, color):
	return canvas.create_oval(roond[0][0] - roond[1], roond[0][1] - roond[1],
							roond[0][0] + roond[1], roond[0][1] + roond[1])


def result():
	enum_rounds = list(enumerate(rounds))
	min_dist = float("inf")
	for i, r in enum_rounds:
		len_a = ((r[0][0] - dot[0])**2 + (r[0][1] - dot[1])**2)**0.5
		if (len_a <= r[1]):
			dist = r[1] - len_a
		else:
			dist = len_a - r[1]

		if dist < min_dist:
			min_dist = dist
			res = r

	return canvas.create_oval(res[0][0] - res[1], res[0][1] - res[1],
							res[0][0] + res[1], res[0][1] + res[1],
							fill="black", outline='')


# Создание окна
#--------------------------------------------------------------------------
win = tk.Tk()
win.resizable(width=False, height=False)
win.title('Lab_4_2_def')
#--------------------------------------------------------------------------

WIDTH = 500
HEIGHT = 500
canvas = tk.Canvas(win, width=WIDTH, height=HEIGHT, bg="green")
canvas.grid(row=0, column=0, columnspan=4, stick='wens', padx=5, pady=5)

button_result = tk.Button(win, text="Результат", command=result, bg="red")
button_result.grid(row=1, column=0, columnspan=4, stick='wens', padx=5, pady=5)

create_point(dot, "white")

for r in rounds:
	create_round(r, "white")





# запуск обработчика обытий
win.mainloop()	
