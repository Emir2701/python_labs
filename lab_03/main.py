from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import messagebox as box
from tkinter import filedialog as fd

def ordkoi_bin(char):
	num_int = char.encode("koi8-r")
	num_bin = bin(num_int[0])[2:]
	num_bin = (8 - len(num_bin))*"0" + num_bin
	return num_bin

def massage_to_bin(massage):
	bin_massage = ""
	for char in massage:
		num_bin = ordkoi_bin(char)
		bin_massage += num_bin
	return bin_massage

def charkoi_bin(num_bin):
	num_int = int(num_bin, 2)
	num_byte = num_int.to_bytes(1, byteorder="big")
	char = num_byte.decode("koi8-r")
	return char

def change_last_bit(width, height, pix, bin_massage, draw):

	count_channels = len(pix[0, 0])
	index = 0
	for x in range(width):
		for y in range(height):
			for z in range(count_channels):
				
				if index == len(bin_massage):
					return pix

				bit = int(bin_massage[index])
				channel = pix[x, y][z]

				if (bit == 0b0):
					channel &=  ~0b1
				else:
					channel |=  0b1

				channels = list(pix[x, y])
				channels[z] = channel
				channels = tuple(channels)

				draw.point((x, y), channels)
				index += 1


def decode_image(width, height, pix):
	string = ""
	byte = ""
	count_channels = len(pix[0, 0])
	count_bits = 0
	for x in range(width):
		for y in range(height):
			for z in range(count_channels):

				if (count_bits == 8):
					
					char = charkoi_bin(byte)
					# print(char)
					if (char == "@"):
						return string

					string += char
					count_bits = 0
					byte = ""
				
				channel = pix[x, y][z]

				bit = channel & 0b1
				
				byte += str(bit)
				count_bits += 1



def info():
    box.showinfo('Описание программы',
                 "Программа шифрует сообщения в png изображения и расшифровывает их")

def encode_massage():
	filetypes = (('image files', '*.PNG'),)

	filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
	image = Image.open(filename)
	draw = ImageDraw.Draw(image)
	width = image.size[0]
	height = image.size[1]
	pix = image.load()

	massage = entry_input.get()
	end_point = "@"
	massage = massage + end_point
	bin_massage = massage_to_bin(massage)
	pix = change_last_bit(width, height, pix, bin_massage, draw)

	
     
	box.showinfo("Отчёт", "Сообщение успешно зашифровано, выберете путь для сохранения зашифрованной картики")


	folder = fd.askdirectory()
	name = "/" + entry_input_name.get()
	if name[-4:] != ".png":
		name += ".png"
	image.save(folder + name, "PNG")

	box.showinfo("Отчёт", "Картинка успешно сохранилась")

def decode_massage():
	filetypes = (('image files', '*.PNG'),)
	
	
	box.showinfo("Отчёт", "Выберете .png картику для расшифровки")
	filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
	name = filename.split("/")[-1]
	image = Image.open(filename)
	draw = ImageDraw.Draw(image)
	width = image.size[0]
	height = image.size[1]
	pix = image.load()

	string = decode_image(width, height, pix)
	box.showinfo("Отчёт", "Сообщение успешно расшифровано")
	#print(string)	
	entry_output.delete(0, tk.END)
	entry_output.insert(0, string)



# Создание окна
#--------------------------------------------------------------------------
win = tk.Tk()
win.resizable(width=False, height=False)
win.title('Lab_3_2')
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
label_input = tk.Label(win, text='Ввод сообщения:')
label_input.grid(row=0, column=0, padx=5, pady=5)

entry_input = tk.Entry(win)
entry_input.grid(row=1, column=0, padx=5, pady=5)

label_input = tk.Label(win, text='Ввод названия закодированной картинки:')
label_input.grid(row=2, column=0, padx=5, pady=5)

entry_input_name = tk.Entry(win)
entry_input_name.grid(row=3, column=0, padx=5, pady=5)

label_output = tk.Label(win, text='Вывод сообщения:')
label_output.grid(row=0, column=1, padx=5, pady=5)

entry_output = tk.Entry(win)
entry_output.grid(row=1, column=1, padx=5, pady=5)

encode_button = tk.Button(win, text="Зашифровать сообщение", command=encode_massage)
encode_button.grid(row=4, column=0, stick='wens', padx=5, pady=5)

decode_button = tk.Button(win, text="Расшифровать сообщение", command=decode_massage)
decode_button.grid(row=4, column=1, stick='wens', padx=5, pady=5)
#--------------------------------------------------------------------------

# запуск обработчика обытий
win.mainloop()	


	