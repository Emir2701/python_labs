# Увеличить яркость картинки

from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import messagebox as box
from tkinter import filedialog as fd


def update_image():
	filetypes = (('image files', '*.PNG'),)

	filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
	image = Image.open(filename)
	draw = ImageDraw.Draw(image)
	width = image.size[0]
	height = image.size[1]
	pix = image.load()

	count_channels = 3;
	for x in range(width):
		for y in range(height):
			channels = list(pix[x, y])
			print("{}, {}: {}".format(x, y, pix[x, y]))
			for z in range(count_channels):
				
				channal = channels[z]
				#print(channal)
				channal += 20
				#print(channal)

				if channal > 255:
					channal = 255
				channels[z] = channal

			channels = tuple(channels)
			draw.point((x, y), channels)
			print("{}, {}: {}".format(x, y, pix[x, y]))

	

	image.save(filename, "PNG")

	box.showinfo("Отчёт", "Яркость успешно увеличена")

# Создание окна
#--------------------------------------------------------------------------
win = tk.Tk()
win.resizable(width=False, height=False)
win.title('Lab_3_2')
#--------------------------------------------------------------------------




# Интерфейс
#--------------------------------------------------------------------------
label_input = tk.Label(win, text='Выберете файл:')
label_input.grid(row=0, column=0, padx=5, pady=5)

update_button = tk.Button(win, text="Увеличить яркость", command=update_image)
update_button.grid(row=4, column=0, stick='wens', padx=5, pady=5)


#--------------------------------------------------------------------------

# запуск обработчика обытий
win.mainloop()	
