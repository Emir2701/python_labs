# Перевод в десятичную из любой

def to_10(num, ss):
	if '.' in str(num):
		int_part, float_part = str(num).split('.')

		summ = 0

		# Перевод целой части
		int_part = int_part[::-1]
		for i in range(len(int_part)):
			summ += int(int_part[i]) * ss ** i

		# Перевод дробной части
		for i in range(len(float_part)):
			summ += int(float_part[i]) * ss ** (- i - 1)
	else:
		summ = 0

		# Перевод целой части
		num = str(num)[::-1]
		for i in range(len(num)):
			summ += int(num[i]) * ss ** i

	return summ

# _______________________________________________________
# Перевод из десятичной в любую

def from_10(num, ss):
	int_part, float_part = str(num).split('.')

	ch = from_10_int(int_part, ss) + '.' + from_10_float(float_part, ss)

	return ch

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

# _______________________________________________________
# Перевод из десятичной в 2-10

def from_10_to_2_10(num):
	num = str(num)

	d = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', 
	     '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001'}

	new_ch = ''

	for i in range(len(num)):
		if num[i] == '.':
			new_ch += '.'
			continue
		new_ch += d.get(num[i])

	return new_ch

# _______________________________________________________
# Перевод из 2-10 в десятичную

def from_2_10_to_10(num):
	num = str(num)
	new_ch = ''

	d = {'0000':'0', '0001':'1', '0010':'2', '0011':'3', '0100':'4', 
	     '0101':'5', '0110':'6', '0111':'7', '1000':'8', '1001':'9'}

	i = 0
	while i < len(num):
		if num[i] == '.':
			new_ch += '.'
			i += 1
			continue

		new_ch += d.get(num[i:i+4])
		i += 4

	return new_ch

# _______________________________________________________
# Из десятичной в троично-симметричную

def from_10_to_3(num):
	num = list(from_10(num, 3)[::-1] + '0')
	new_ch = ''
	for i in range(len(num)):
		if num[i] == '.':
			new_ch += '.'
		elif num[i] == '0':
			new_ch += '0'
		elif num[i] == '1':
			new_ch += '+'
		elif num[i] == '1':
			new_ch += '-'
			if num[i + 1] == '.':
				num[i + 2] = str(int(num[i + 2]) + 1)
			else:
				num[i + 1] = str(int(num[i + 1]) + 1)
		else:
			new_ch += '0'
			if num[i + 1] == '.':
				num[i + 2] = str(int(num[i + 2]) + 1)
			else:
				num[i + 1] = str(int(num[i + 1]) + 1)

	new_ch = new_ch[::-1]
	if new_ch[0] == '0' and new_ch[1] != '.':
		new_ch = new_ch[1:]

	return new_ch

# _______________________________________________________
# Из троично симметричной в десятичную

def from_3_to_10(num):
	int_part, float_part = str(num).split('.')
	new_ch = ''

	summ = 0

	int_part = int_part[::-1]
	for i in range(len(int_part)):
		if int_part[i] == '+':
			summ += 3 ** i
		elif int_part[i] == '-':
			summ -= 3 ** i

	for i in range(len(float_part)):
		if float_part[i] == '+':
			summ += 3 ** (- i - 1)
		elif float_part[i] == '-':
			summ -= 3 ** (- i - 1)

	return summ

# _______________________________________________________
# Из десятичной в Грея

def from_10_to_grey(num):
	num = int(num)
	ch = num ^ (num >> 1)
	ch = from_10_int(ch, 2)
	return ch

# _______________________________________________________
# Из Грея в десятичную

def from_grey_to_10(num):
	ch = num[0]
	count = 1 if num[0] == '1' else 0
	for i in range(1, len(num)):
		if count % 2 == 0:
			ch += num[i]
		else:
			if num[i] == '1':
				ch += '0'
			else:
				ch += '1'

	return to_10(ch, 2)


# _______________________________________________________
# Из Римской в десятичную

def from_rim(num):
	d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	num += 'I'
	summ = 0
	for i in range(len(num) - 1):
		print(d.get(num[i]))
		if d.get(num[i]) < d.get(num[i + 1]):
			summ -= d.get(num[i])
			print('s', summ)
		else:
			summ += d.get(num[i])
	return summ


# _______________________________________________________
# Из десятичной в римскую

def to_rim(num):
	num = str(num)
	rim = ''
	if len(num) == 4:
		rim += 'M' * int(num[0])
		num = num[1:]
	if len(num) == 3:
		if int(num[0]) <= 3:
			rim += 'C' * int(num[0])
			num = num[1:]
		elif int(num[0]) == 4:
			rim += 'CD'
			num = num[1:]
		elif int(num[0]) <= 8:
			rim += 'D' + 'C' * (int(num[0]) - 5)
			num = num[1:]
		else:
			rim += 'CM'
			num = num[1:]
	if len(num) == 2:
		if int(num[0]) <= 3:
			rim += 'X' * int(num[0])
			num = num[1:]
		elif int(num[0]) == 4:
			rim += 'XL'
			num = num[1:]
		elif int(num[0]) <= 8:
			rim += 'L' + 'X' * (int(num[0]) - 5)
			num = num[1:]
		else:
			rim += 'XC'
			num = num[1:]
	if len(num) == 1:
		if int(num[0]) <= 3:
			rim += 'I' * int(num[0])
			num = num[1:]
		elif int(num[0]) == 4:
			rim += 'IV'
			num = num[1:]
		elif int(num[0]) <= 8:
			rim += 'V' + 'I' * (int(num[0]) - 5)
			num = num[1:]
		else:
			rim += 'IX'
			num = num[1:] 

	return rim

# _______________________________________________________
# Перевод из восьмиричной в двоичную с использованием словарей

def from_8_to_2(num):
	d = {'0':'000', '1':'001', '2':'010', '3':'011', 
	     '4':'100', '5':'101', '6':'110', '7':'111'}
	new_ch = ''

	int_part, float_part = str(num).split('.')
	
	for i in range(0, len(int_part)):
		new_ch += d.get(int_part[i])

	new_ch += '.'

	for i in range(0, len(float_part)):
		new_ch += d.get(float_part[i])

	return new_ch


# _______________________________________________________
# Перевод из двоичной в шестнадцатиричную с использованием словарей

def from_2_to_16(num):
	d = {'0000':'0', '0001':'1', '0010':'2', '0011':'3', 
	     '0100':'4', '0101':'5', '0110':'6', '0111':'7',
	     '1000':'8', '1001':'9', '1010':'A', '1011':'B', 
	     '1100':'C', '1101':'D', '1110':'E', '1111':'F'}
	new_ch = ''

	int_part, float_part = str(num).split('.')

	if len(int_part) % 4 != 0:
		int_part = '0' * (4 - len(int_part) % 4) + int_part


	for i in range(0, len(int_part), 4):
		new_ch += d.get(int_part[i:i + 4])

	new_ch += '.'

	if len(float_part) % 4 != 0:
		float_part = float_part + '0' * (4 - len(float_part) % 4)

	for i in range(0, len(float_part), 4):
		new_ch += d.get(float_part[i:i + 4])

	while new_ch[0] == '0':
		new_ch = new_ch[1:]

	return new_ch


print(from_grey_to_10('10'))





















