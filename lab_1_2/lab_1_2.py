# ИУ7-23Б Шимшир Эмирджан В-2

# Программа переводит числа из 10-й СС в 3-ю и обратно


import tkinter as tk
from tkinter import messagebox

# функции перевода
# _______________________________________________________________________

# Перевод в десятичную из 3
def from_3_to_10():
	try:
		# Взятие поля ввода
		entry_in['state'] = tk.NORMAL
		num = entry_in.get()
		entry_in['state'] = tk.DISABLED

		# Проверка на 3 СС
		flag = False
		for i in '3456789':
			if i in num:
				flag = True

		# Обработка крайних точек
		if  num[-1] == '.' or flag:
			messagebox.showinfo("Ошибка", "Число введено некорректно")
			clear_all()
		else:
			# Целое или дробное
			if '.' in str(num):
				int_part, float_part = str(num).split('.')

				summ = 0

				# Перевод целой части
				int_part = int_part[::-1]
				for i in range(len(int_part)):
					summ += int(int_part[i]) * 3 ** i

				# Перевод дробной части
				for i in range(len(float_part)):
					summ += int(float_part[i]) * 3 ** (- i - 1)
			else:
				summ = 0

				# Перевод целой части
				num = str(num)[::-1]
				for i in range(len(num)):
					summ += int(num[i]) * 3 ** i


			summ = round(summ, 6)

			# Вывод
			entry_out['state'] = tk.NORMAL
			entry_out.delete(0, tk.END)
			entry_out.insert(0, str(summ))
			entry_out['state'] = tk.DISABLED

	except ValueError:
		messagebox.showinfo("Ошибка", "Число введено некорректно")
		clear_all()




# Перевод из десятичной в 3
def from_10_to_3():
	try:
		# Взятие поля ввода
		entry_in['state'] = tk.NORMAL
		num = entry_in.get()
		entry_in['state'] = tk.DISABLED

		# Обработка крайних точек
		if num[-1] == '.':
			messagebox.showinfo("Ошибка", "Число введено некорректно")
			clear_all()
		else:
			# Целое или дробное
			if '.' in str(num) and num[0]=='.':
				ch = '0.' + str(from_10_float(num[1:]))
				ch = round(float(ch), 6)
			elif '.' in str(num) and num[0]!='.':
				int_part, float_part = str(num).split('.')
				ch = from_10_int(int_part) + '.' + from_10_float(float_part)
				ch = round(float(ch), 6)
			else:
				ch = from_10_int(num)

			# Вывод
			entry_out['state'] = tk.NORMAL
			entry_out.delete(0, tk.END)
			entry_out.insert(0, str(ch))
			entry_out['state'] = tk.DISABLED

	except ValueError:
		messagebox.showinfo("Ошибка", "Число введено некорректно")
		clear_all()

# Перевод целой части
def from_10_int(num):
	ch_10 = int(num)
	new_ch = ''
	while ch_10 > 0:
		new_ch += str(ch_10 % 3)
		ch_10 //= 3

	return new_ch[::-1]

# Перевод дробной части
def from_10_float(num):
	ch_10 = float('0.' + num)
	new_ch = ''
	for i in range(8):
		new_ch += str(int(ch_10 * 3))
		ch_10 = ch_10 * 3 - int(ch_10 * 3)
		if ch_10 == 0:
			break

	return new_ch

# _______________________________________________________________________

# очистить ввод
def clear_in():
	clear(entry_in)

# очистить вывод
def clear_out():
	clear(entry_out)

# очистить все
def clear_all():
	clear(entry_in)
	clear(entry_out)

# Вывод информации
def info():
	messagebox.showinfo("Информация", "ИУ7-23Б\n\nШимшир Эмирджан\n\n\
Программа переводит числа из 10-й в 3-ю СС и обратно")

# Добавить символ в ввод
def add_digit_or_dot(digit):
	entry_in['state'] = tk.NORMAL
	value = entry_in.get()
	if value[0]=='0' and len(value) == 1:
		value = value[1:]
	entry_in.delete(0, tk.END)
	entry_in.insert(0, value + digit)
	entry_in['state'] = tk.DISABLED

# Очистка
def clear(entry):
	entry['state'] = tk.NORMAL
	entry.delete(0, tk.END)
	entry.insert(0, 0)
	entry['state'] = tk.DISABLED

# Удаление символа
def delete(entry):
	entry['state'] = tk.NORMAL
	value = entry.get()
	entry.delete(0, tk.END)
	if len(value[:-1]) == 0:
		entry.insert(0, 0)
	else:
		entry.insert(0, value[:-1])
	entry['state'] = tk.DISABLED

# Создание основных кнопок
def make_digit_button(digit):
	return tk.Button(text=digit, bd=5, font=('Arial', 13), command=lambda : add_digit_or_dot(digit))

# Создание кноки удаления символа
def make_del_button(operation):
	return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', \
		command=lambda: delete(entry_in))

# Создание кноки очистки ввода
def make_clear_button(operation):
	return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', \
		command=lambda :  clear(entry_in))

# Обработка кнопок
def press_key(event):
	if event.char.isdigit() or event.char=='.':
		add_digit_or_dot(event.char)
# MAIN
#___________________________________________________________________________________

# Цвет фона
GREY = '#b0cbd2'
# Создание окна
win = tk.Tk()
# размер окна
win.geometry('250x360')
# Блокировка измениения размера
win.resizable(width=False, height=False)
# задать цвет фона
win['bg'] = GREY
# заголовок
win.title('Lab_1_2')
# обработка клавиатуры
win.bind('<Key>', press_key)

# Основное меню
mmenu = tk.Menu(win)

# Меню перевода
pmenu = tk.Menu(mmenu)
pmenu.add_command(label='Из 10-й в 3-ю СС', command=from_10_to_3) 
pmenu.add_command(label='Из 3-й в 10-ю СС', command=from_3_to_10) 
mmenu.add_cascade(label='Перевод', menu = pmenu)

# Меню очистки
cmenu = tk.Menu(mmenu)
cmenu.add_command(label='Поле ввода', command=clear_in) 
cmenu.add_command(label='Поле вывода', command=clear_out) 
cmenu.add_command(label='Оба поля', command=clear_all)
mmenu.add_cascade(label='Очистка', menu=cmenu)

# Кнопка в меню с информацией
mmenu.add_command(label='Информация', command=info)

# создание надписи ВВОД
lb_in = tk.Label(win, text='Ввод:', bg=GREY)
lb_in.grid(row=0, column=0, stick='wens', padx=5, pady=5)

# создание надписи ВЫВОД
lb_out = tk.Label(win, text='Вывод:', bg=GREY)
lb_out.grid(row=1, column=0, stick='wens', padx=5, pady=5)

# Создание поля ввода
entry_in = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
entry_in.grid(row=0, column=1, columnspan=3, stick='we', padx=5)
entry_in.insert(0, 0)
entry_in['state'] = tk.DISABLED

# Создание поля вывода
entry_out = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
entry_out.grid(row=1, column=1, columnspan=3, stick='we', padx=5)
entry_out.insert(0, 0)
entry_out['state'] = tk.DISABLED

# Создание основных кнопок
make_digit_button('1').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button('2').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(row=4, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=4, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=5, column=0, stick='wens', padx=5, pady=5)
make_digit_button('.').grid(row=5, column=1, columnspan=2, stick='wens', padx=5, pady=5)

# Создание кноки удаления символа
make_del_button('del').grid(row=4, column=3, rowspan=2, stick='wens', padx=5, pady=5)
# Создание кноки очистки ввода
make_clear_button('C').grid(row=2, column=3, rowspan=2, stick='wens', padx=5, pady=5)

# выравнивание по столбцам
win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

# выравнивание по строкам
win.grid_rowconfigure(0, minsize=60)
win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)
win.grid_rowconfigure(5, minsize=60)

# привязка меню
win.config(menu=mmenu)
# запуск обработчика обытий
win.mainloop()	

