#my_str = 'Lets my write this text'
my_str = str(raw_input('Input str -> '))
get_list = my_str.split(' ')
position = 0
max_len = 0
position_max_len = 0

while position < len(get_list):
	if len(get_list[position]) > max_len:
		max_len = len(get_list[position])
		position_max_len = position
	position += 1

print('"{st_line}" length -> {length}'.format(st_line = get_list[position_max_len], length = len(get_list[position_max_len])))