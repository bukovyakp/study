#!/usr/bin/env python 
# -*- coding: utf-8 -*-

def sumtree(L):
	tot = 0
	for x in L:							# Обхід елементів одного рівня
		if not isinstance(x, list):
			tot += x					# Числа сумуються безпосередньо
		else:
			tot += sumtree(x)			# Списки обробляються рекурсивними викликами
	return tot

# Произвольная глубина вложения

#print(sumtree([1, [2, [3, [4, [5]]]]])) 			# Выведет 15 (центр тяжести справа)
print(sumtree([[[[[1], 2], 3], 4], 5])) 			# Выведет 15 (центр тяжести слева)
#print(sumtree([1, [2, [3, 4], 5], 6, [7, 8]]))		# Выведет 36
