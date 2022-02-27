import tkinter as tk

def summ():

	n_1 = entry_in_1.get()
	n_2 = entry_in_2.get()
	print(n_1, n_2)

	if int(n_1) >= 0 and int(n_2) >= 0:
		res = summ_2_plus(n_1, n_2)
		entry_out.delete(0, tk.END)
		entry_out.insert(0, res)
	elif int(n_1) < 0 and int(n_2) < 0:
		n_1 = n_1[1:]
		n_2 = n_2[1:]
		res = summ_2_plus(n_1, n_2)
		entry_out.delete(0, tk.END)
		entry_out.insert(0, '-' + res)
		summ_2_minus(n_1, n_2)
	elif int(n_1) < 0:
		n_1 = list(map(int, n_1[1:]))
		n_2 = list(map(int, n_2))

		res = sum_1_minus(n_2, n_1)
		entry_out.delete(0, tk.END)
		entry_out.insert(0, '-' + res)

	else:
		n_1 = list(map(int, n_1))
		n_2 = list(map(int, n_2[1:]))

		res = sum_1_minus(n_1, n_2)
		res = sum_1_minus(n_2, n_1)
		entry_out.delete(0, tk.END)
		entry_out.insert(0, '-' + res)
	
def summ_2_plus(n_1, n_2):
	n_1 = list(map(int, n_1))
	n_2 = list(map(int, n_2))

	n_1 = n_1[::-1]
	n_2 = n_2[::-1]

	size = max(len(n_1), len(n_2))

	n_1 += [0] * (size - len(n_1))
	n_2 += [0] * (size - len(n_2))
	print(n_1, n_2)

	# сложить 2 числа
	overflow = 0
	res = []
	for obj in zip(n_1, n_2):
	    value = obj[0] + obj[1] + overflow
	    overflow = value // 3
	    res.append(value % 3)

	# если флаг переполнения установлен - добавить бит в начало нового числа
	if overflow == 1:
		res.append(1)

    # перевернуть число назад
	res = res[::-1]
	return ''.join(map(str, res))

def sum_1_minus(n_p, n_m):
	

	n_p = n_p[::-1]
	n_m = n_m[::-1]

	size = max(len(n_p), len(n_m))

	n_p += [0] * (size - len(n_p))
	n_m += [0] * (size - len(n_m))
	print(n_p, n_m)

	# сложить 2 числа
	overflow = 0
	res = []
	for obj in zip(n_p, n_m):
		if overflow == 1:
			obj[0] -= 1

	value = obj[0] - obj[1]
	if value < 0:
		value = 2 - obj[1]
		overflow = 1
	else:
		overflow = 0
	res.append(value)

	# если флаг переполнения установлен - добавить бит в начало нового числа
	if overflow == 1:
		res.append(1)

    # перевернуть число назад
	res = res[::-1]
	return ''.join(map(str, res))
	



# Создание окна
win = tk.Tk()

# создание надписи ВВОД
lb_in = tk.Label(win, text='Ввод:')
lb_in.grid(row=0, column=0)

# создание надписи ВЫВОД
lb_out = tk.Label(win, text='Вывод:')
lb_out.grid(row=1, column=0)

# Создание поля ввода
entry_in_1 = tk.Entry(win)
entry_in_1.grid(row=0, column=1)

# Создание поля ввода
entry_in_2 = tk.Entry(win)
entry_in_2.grid(row=0, column=2)

# Создание поля вывода
entry_out = tk.Entry(win)
entry_out.grid(row=1, column=1, columnspan=3)

enter_button = tk.Button(text='enter', command=summ)
enter_button.grid(row=2, column=1, columnspan=3)


# запуск обработчика обытий
win.mainloop()	
