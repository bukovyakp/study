import mymod
from mymod import (count_lines, count_chars)

print('Count of lines ->')
print mymod.count_lines('chat_log.txt')
print('Count of symbols ->')
print mymod.count_chars('chat_log.txt')

print('Count of lines for 2 test ->')
print count_lines('chat_log.txt')
print('Count of symbols for 2 test ->')
print count_chars('chat_log.txt')
