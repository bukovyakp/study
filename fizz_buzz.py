n = 1

while 0 < n <= 100:
	print n
	if n%3 == 0 and n%5 > 0:
		print('fizz %d') %n
	elif n%5 == 0 and n%3 > 0:
		print ('buzz %d') %n
	elif n%5 == 0 and n%3 == 0:
		print ('fizzbuzz %d') %n
	n = (n + 1)