#!/usr/bin/env python 
# -*- coding: utf-8 -*-

""" 3. (Повышенная сложность) Написать программу декодирования телефонного номера для АОН. 
По запросу АОНа АТС посылает телефонный номер, используя следующие правила:
— Если цифра повторяется менее 2 раз, то это помеха и она должна быть отброшена
— Каждая значащая цифра повторяется минимум 2 раза
— Если в номере идут несколько цифр подряд, то для обозначения «такая же цифра как предыдущая» используется идущий 2 или более подряд раз знак #

Например, входящая строка 4434###552222311333661 соответствует номеру 4452136
Кстати, регулярные выражения использовать в этих заданиях — нельзя
"""

number = '4434###552222311333661'
decodenum = ''
prev_char = 0
num_char = 0
is_num = 0
n = 0
count_n = 0
octothorpe = 0

for x in number:
	try:
		num_char = int(x)
		is_num = 1
	except:
		is_num = 0
	
	if n == 0 and is_num == 1:
		prev_char = num_char
	if n > 0 and is_num == 1:
		if prev_char == num_char:
			count_n += 1
			if count_n == 1:
				decodenum = decodenum + str(num_char)
		if prev_char != num_char:
			prev_char = num_char
			count_n = 0
			
	if x == '#' and is_num == 0:
		octothorpe += 1
		if octothorpe == 2:
			decodenum = decodenum + str(num_char)
	else:
		octothorpe = 0
	n += 1
	
print decodenum