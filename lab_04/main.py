# ИУ7-23Б Шимшир Эмирджан

# На плоскости задано множество прямых. 
# Найти три прямые, образующие треугольник минимальной площади.
# Дать графическое изображение результатов.

import tkinter as tk
from tkinter import messagebox

# Класс треугольников
class Triangle:
	triangles = []
	def __init__(self, line1, line2, line3, point1, point2, point3):
		self.line1 = line1
		self.line2 = line2
		self.line3 = line3
		self.point1 = point1
		self.point2 = point2
		self.point3 = point3
		self.triangles.append(self)

	def print_triangle(self, color):
		self.line1.change_color(color)
		self.line2.change_color(color)
		self.line3.change_color(color)

	def del_triangle(self):
		self.point1.del_point()
		self.point2.del_point()
		self.point3.del_point()

	def square(self):
		x1 = self.point1.x
		y1 = self.point1.y
		x2 = self.point2.x
		y2 = self.point2.y
		x3 = self.point3.x
		y3 = self.point3.y

		a = ((x2 - x1) ** 2 + (y2 - y1) ** 2)**0.5
		b = ((x3 - x1) ** 2 + (y3 - y1) ** 2)**0.5
		c = ((x2 - x3) ** 2 + (y2 - y3) ** 2)**0.5
		p = (a + b + c) / 2
		return (p * (p - a) * (p - b) * (p - c))**0.5

	@classmethod
	def del_zero_square(cls):
		i = 0
		while i < cls.len_arr():
			if cls.triangles[i].square() == 0:
				cls.triangles[i].del_triangle()
				cls.triangles.pop(i)
			i += 1

	@classmethod
	def clear(cls):
		for triangle in cls.triangles:
			triangle.print_triangle("white")
			
		cls.triangles.clear()

	@classmethod
	def len_arr(cls):
		return len(cls.triangles)

	def __str__(self):
		return f"square: {self.square()}"

# Класс прямых
class Line:
	lines = []
	def __init__(self, point_1, point_2, color):
		self.point_1 = point_1
		self.point_2 = point_2
		self.color = color
		self.id = self.create()
		self.lines.append(self)

	def len(self):
		return ((self.point_1.x - self.point_2.x)**2 + (self.point_1.y - self.point_2.y)**2)**0.5

	def change_color(self, color):
		canvas.delete(self.id)
		self.color = color
		self.id = self.create()

	def create(self):
		return canvas.create_line(self.point_1.x, self.point_1.y, 
								self.point_2.x, self.point_2.y,
								fill=self.color)
	@classmethod
	def len_arr(cls):
		return len(cls.lines)

	def __str__(self):
		return f"point_1: {self.point_1}\npoint_2: {self.point_2}\nline_id: {self.id}\n"

# Класс точек
class Point:
	points = []
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.color = color
		self.id = self.create()
		self.points.append(self)

	def change_color(self, color):
		canvas.delete(self.id)
		self.color = color
		self.id = self.create()

	def create(self):
		return canvas.create_oval(self.x - POINT_SIZE, self.y - POINT_SIZE,
								self.x + POINT_SIZE, self.y + POINT_SIZE,
								fill=self.color, outline='')
	@classmethod
	def clear_with_canvas(cls):
		for point in cls.points:
			canvas.delete(point.id)

		cls.points.clear()

	def del_point(self):
		canvas.delete(self.id)

	@classmethod
	def clear(cls):
		cls.points.clear()

	@classmethod
	def len_arr(cls):
		return len(cls.points)

	def __str__(self):
		return f"x: {self.x}, y: {self.y}, point_id: {self.id}\n"


def line_intersection(line1, line2, mode):
	xdiff = (line1.point_1.x - line1.point_2.x, line2.point_1.x - line2.point_2.x)
	ydiff = (line1.point_1.y - line1.point_2.y, line2.point_1.y - line2.point_2.y) 

	def det(a, b):
		return a[0] * b[1] - a[1] * b[0]

	div = det(xdiff, ydiff)
	if div == 0:
	   return False

	d = (det((line1.point_1.x, line1.point_1.y), (line1.point_2.x, line1.point_2.y)), 
		det((line2.point_1.x, line2.point_1.y), (line2.point_2.x, line2.point_2.y)))
	x = det(d, xdiff) / div
	y = det(d, ydiff) / div

	def is_in_lines(x, y, line1, line2):
		line_1_part_1 = ((line1.point_1.x - x)**2 + (line1.point_1.y - y)**2)**0.5
		line_1_part_2 = ((line1.point_2.x - x)**2 + (line1.point_2.y - y)**2)**0.5

		line_2_part_1 = ((line2.point_1.x - x)**2 + (line2.point_1.y - y)**2)**0.5
		line_2_part_2 = ((line2.point_2.x - x)**2 + (line2.point_2.y - y)**2)**0.5
		EPS = 1e-3

		if abs(line_1_part_1 + line_1_part_2 - line1.len()) < EPS and abs(line_2_part_1 + line_2_part_2 - line2.len()) < EPS:
			return True
		return False

	if is_in_lines(x, y, line1, line2):
		if mode == "bin":
			return True
		return Point(x, y, "red")
		
	return False



def count_triangle(line1, line2, line3):
	point1 = line_intersection(line1, line2, "-")
	point2 = line_intersection(line2, line3, "-")
	point3 = line_intersection(line3, line1, "-")

	return point1, point2, point3

def result():
	Point.clear_with_canvas()
	Triangle.clear()

	print(f"Point: {Point.len_arr()}")
	print(f"Line: {Line.len_arr()}")
	print(f"Triangle: {Triangle.len_arr()}")
	
	if Line.len_arr() < 3:
		error_message("Ошибка ввода: на плоскости меньше трех прямых")
		return 1

	for i in range(len(Line.lines)):
		candidates = []
		for j in range(i + 1, len(Line.lines)):
			if line_intersection(Line.lines[i], Line.lines[j], "bin"):
				candidates.append(Line.lines[j])
				
		if len(candidates) < 2:
			continue
		for k in range(len(candidates)):
			for p in range(k + 1, len(candidates)):
				if line_intersection(candidates[k], candidates[p], "bin"):
					
					triang_points = count_triangle(Line.lines[i], candidates[k], candidates[p])
					Triangle(Line.lines[i], candidates[k], candidates[p], *triang_points)
	
	Triangle.del_zero_square()
		
	if len(Triangle.triangles) == 0:
		error_message("Ошибка ввода: нет треуголников")
		return 1

	min_triang = Triangle.triangles[0]
	min_square = Triangle.triangles[0].square()
	for i in range(1, len(Triangle.triangles)):
		if min_square > Triangle.triangles[i].square():
			min_triang = Triangle.triangles[i]
			min_square = Triangle.triangles[i].square()
	min_triang.print_triangle("blue")
	
	print("min_triang:", min_triang)
	for i in range(len(Triangle.triangles)):
		print(f"{i + 1}: {Triangle.triangles[i]}")
	Point.clear()


def clear_canvas():
	canvas.delete('all')
	Point.points.clear()
	Line.lines.clear()
	Triangle.triangles.clear()

def add_object(x, y):
	Point(x, y, "white")
	if Point.len_arr() == 2:
		if (Point.points[0].x == Point.points[1].x) and (Point.points[0].y == Point.points[1].y):
			error_message("Ошибка ввода: точки совпадают")
			Point.clear_with_canvas()
		Line(Point.points[0], Point.points[1], "white")
		Point.clear()

def add_point():
	try:
		x = int(entry_input_x.get())
		y = int(entry_input_y.get())
	except ValueError:
		error_message('Ошибка ввода: введите число')

	if not (0 <= x <= WIDTH and 0 <= y <= HEIGHT):
		error_message('Ошибка ввода: canvas 500x500')
		return

	add_object(x, y)

def click(event):
	add_object(event.x, event.y)


def info():
	text = '''На плоскости задано множество прямых. 
Найти три прямые, образующие треугольник минимальной площади.
Дать графическое изображение результатов.'''

	messagebox.showinfo('Описание программы', text)

def error_message(text):
	messagebox.showinfo('Ошибка', text)

# Создание окна
#--------------------------------------------------------------------------
win = tk.Tk()
win.resizable(width=False, height=False)
win.title('Lab_4_2')
#--------------------------------------------------------------------------


# Основное меню
#--------------------------------------------------------------------------
mmenu = tk.Menu(win)
win.config(menu=mmenu)
pmenu = tk.Menu(mmenu)
pmenu.add_command(label='Информация', command=info) 
mmenu.add_cascade(label='Меню', menu = pmenu)
#--------------------------------------------------------------------------


# Интерфейс
#--------------------------------------------------------------------------
label_input_x = tk.Label(win, text='x:')
label_input_x.grid(row=0, column=0, padx=5, pady=5)

entry_input_x = tk.Entry(win)
entry_input_x.grid(row=0, column=1, padx=5, pady=5)

label_input_y = tk.Label(win, text='y:')
label_input_y.grid(row=1, column=0, padx=5, pady=5)

entry_input_y = tk.Entry(win)
entry_input_y.grid(row=1, column=1, padx=5, pady=5)

button_add_point = tk.Button(win, text="Добавить точку", command=add_point)
button_add_point.grid(row=0, column=2, stick='wens', padx=5, pady=5)

button_clear_canvas = tk.Button(win, text="Очистить холст", command=clear_canvas)
button_clear_canvas.grid(row=1, column=2, stick='wens', padx=5, pady=5)

button_result = tk.Button(win, text="Результат", command=result, bg="red")
button_result.grid(row=0, column=3, rowspan=1, stick='wens', padx=5, pady=5)

label_canvas= tk.Label(win, text='Canvas 500x500:')
label_canvas.grid(row=1, column=3, padx=5, pady=5)

WIDTH = 500
HEIGHT = 500
canvas = tk.Canvas(win, width=WIDTH, height=HEIGHT, bg="green")
canvas.grid(row=2, column=0, columnspan=4, stick='wens', padx=5, pady=5)


POINT_SIZE = 2

canvas.bind("<Button-1>", click)
#--------------------------------------------------------------------------

# запуск обработчика обытий
win.mainloop()	


