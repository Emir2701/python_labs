# Дьяченко Артём ИУ7-23Б
import tkinter as tk
import tkinter.messagebox as mb


# Перевод целой части
def from_10_int(num, ss):
    ch_10 = int(num)
    new_ch = ''
    while ch_10 > 0:
        new_ch += str(ch_10 % ss)
        ch_10 //= ss

    return new_ch[::-1]


# Перевод дробной части
def from_10_float(num, ss):
    ch_10 = float('0.' + num)
    new_ch = ''
    for i in range(8):
        new_ch += str(int(ch_10 * ss))
        ch_10 = ch_10 * ss - int(ch_10 * ss)
        if ch_10 == 0:
            break

    return new_ch


def from_10():
    val = num.get()
    try:
        val = float(val)
    except:
        msg = 'Это не вещественное десятичное число!'
        mb.showerror("Ошибка", msg)
        return

    flag = ''
    if val < 0:
        flag = '-'
        val *= -1
    int_part, float_part = str(val).split('.')
    ch = from_10_int(int_part, 6) + '.' + from_10_float(float_part, 6)
    res.delete(0, 'end')
    res.insert(0, flag+ch)


def check6(s):
    if len(s) == 0:
        return False
    try:
        val = float(s)
        cnt = 1
        for i in s:
            if i != '.' and int(i) >= 6:
                if i == '.' and cnt == 1:
                    continue
                return False
            cnt += 1
        return True
    except:
        return False


def from_6():
    val = num.get()
    flag = ''
    if len(val) and val[0] == '-':
        flag = '-'
        val = val[1::]

    if not check6(val):
        msg = 'Это не шестеричное число!'
        mb.showerror("Ошибка", msg)
        return


    sum6 = 0
    if '.' in str(val):
        int_part, float_part = str(val).split('.')

        # Перевод целой части
        int_part = int_part[::-1]
        for i in range(len(int_part)):
            sum6 += int(int_part[i]) * 6 ** i

        # Перевод дробной части
        for i in range(len(float_part)):
            sum6 += int(float_part[i]) * 6 ** (- i - 1)
    else:

        # Перевод целой части
        val = str(val)[::-1]
        for i in range(len(val)):
            sum6 += int(val[i]) * 6 ** i

    res.delete(0, 'end')
    res.insert(0, flag+str(sum6))


def erase_cin():
    num.delete(0, 'end')


def erase_cout():
    res.delete(0, 'end')


def erase_all():
    num.delete(0, 'end')
    res.delete(0, 'end')


def info():
    msg = 'Программа для перевода вещественных чисел из 10-й СС в 6-ю и обратно. Автор: Дьяченко Артём ИУ7-23Б.'
    mb.showinfo('Информация', msg)


def cin1():
    ind = len(num.get())
    num.insert(ind, '1')


def cin2():
    ind = len(num.get())
    num.insert(ind, '2')


def cin3():
    ind = len(num.get())
    num.insert(ind, '3')


def cin4():
    ind = len(num.get())
    num.insert(ind, '4')


def cin5():
    ind = len(num.get())
    num.insert(ind, '5')


def cin6():
    ind = len(num.get())
    num.insert(ind, '6')


def cin7():
    ind = len(num.get())
    num.insert(ind, '7')


def cin8():
    ind = len(num.get())
    num.insert(ind, '8')


def cin9():
    ind = len(num.get())
    num.insert(ind, '9')


def cin0():
    ind = len(num.get())
    num.insert(ind, '0')


def cinDot():
    ind = len(num.get())
    num.insert(ind, '.')


def cinMinus():
    ind = len(num.get())
    num.insert(ind, '-')


win = tk.Tk()
win.title('Лабораторная работа 1_2')  # заголовок окна
h = 300
w = 500
win.geometry(f"{w}x{h}")
win.resizable(False, False)

# Меню
mmenu = tk.Menu(win)
mmenu.add_command(label='Перевести из 10-й в 6-ю СС',
                  command=from_10)
mmenu.add_command(label='Перевести из 6-й в 10-ю СС',
                  command=from_6)
mmenu.add_command(label='Очистить поле ввода',
                  command=erase_cin)
mmenu.add_command(label='Очистить поле вывода',
                  command=erase_cout)
mmenu.add_command(label='Очистить поле ввода и вывода',
                  command=erase_all)
mmenu.add_command(label='Информация о программе и авторе',
                  command=info)
win.config(menu=mmenu)

# обозначение ввода
tk.Label(win, text='Введите число:').grid(row=0, column=0)
# ввод числа
num = tk.Entry(win)
num.grid(row=0, column=1)

# обозначение вывода
tk.Label(win, text='Результат:').grid(row=1, column=0)
# вывод результата
res = tk.Entry(win)
res.grid(row=1, column=1)

btn1 = tk.Button(win, text='1', command=cin1)
btn2 = tk.Button(win, text='2', command=cin2)
btn3 = tk.Button(win, text='3', command=cin3)
btn4 = tk.Button(win, text='4', command=cin4)
btn5 = tk.Button(win, text='5', command=cin5)
btn6 = tk.Button(win, text='6', command=cin6)
btn7 = tk.Button(win, text='7', command=cin7)
btn8 = tk.Button(win, text='8', command=cin8)
btn9 = tk.Button(win, text='9', command=cin9)
btn0 = tk.Button(win, text='0', command=cin0)
btnDot = tk.Button(win, text='.', command=cinDot)
btnMinus = tk.Button(win, text='-', command=cinMinus)

btn1.grid(row=2, column=0, stick='we')
btn2.grid(row=2, column=1, stick='we')
btn3.grid(row=2, column=2, stick='we')
btn4.grid(row=3, column=0, stick='we')
btn5.grid(row=3, column=1, stick='we')
btn6.grid(row=3, column=2, stick='we')
btn7.grid(row=4, column=0, stick='we')
btn8.grid(row=4, column=1, stick='we')
btn9.grid(row=4, column=2, stick='we')
btn0.grid(row=5, column=0, stick='we')
btnDot.grid(row=5, column=1, stick='we')
btnMinus.grid(row=5, column=2, stick='we')

win.grid_columnconfigure(0, minsize=120)
win.grid_columnconfigure(1, minsize=120)
win.grid_columnconfigure(2, minsize=120)
win.grid_rowconfigure(1, minsize=40)

win.mainloop()
