#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Імітація функції print версії 3.0 у версії 2.6 і раніших
Сигнатура виклику: print(*args, sep=' ', end='\n', file=None)
"""

import sys

def print30(*args, **kargs):
	sep = kargs.get('sep', ' ')
	end = kargs.get('end', '\n')
	file = kargs.get('file', sys.stdout)
	output = ''
	first = True

	for arg in args:
		output += ('' if first else sep) + str(arg)
		first = False
	file.write(output + end)




# Удаляет допустимые именованные аргументы со значениями по умолчанию

def print30_pop(*args, **kargs):
	sep = kargs.pop('sep', '')
	end = kargs.pop('end', '\n')
	file = kargs.pop('file', sys.stdout)
	if kargs: raise TypeError('extra keywords: %s' % kargs)
	output = ''
	first = True

	for arg in args:
		output += ('' if first else sep) + str(arg)
		first = False
	file.write(output + end)
