#!/usr/bin/env python
#coding: utf8

"""
Есть лог-файл какого-то чата. Посчитать «разговорчивость» пользователей в нем в виде ник — количество фраз. 
Посчитать среднее число букв на участника чата (це скучно, порахував загальну кількість букв(лише букв) у розрізі кожного учасника чату)
"""

import re

# 1 считываем из файла строки и делим их на логин -> руплика
raw = [x.split('  ->  ') for x in open('chat_log.txt')]

# 2 заполняем словарь

repcount = {}
wordcount = {}
for login, rep in raw:
    if login in repcount:
        repcount[login] += 1
    else:
        repcount[login] = 1
    
    if login in wordcount:
        wordcount[login] += len(re.split(r'[^0-9A-Za-z]+', rep))        #Считаем только слова, другия знаки не берем во внимание
    else:
        wordcount[login] = len(re.split(r'[^0-9A-Za-z]+', rep))

# 3 переводим в список первый словарь
lst = repcount.items()

# 4 проверяем если ли записи по ключам во втором словаре
# если есть записуем в третью колонку кортежа значение из второго словаря и все это складируем в список finlist
finlist = []
for key, val in lst:
    if key in wordcount:
        finlist.append((key, val, wordcount[key]))

# сортируем по количеству реплик
finlist.sort(key = lambda(key,val1,val2):val1)

print ('Login\tCount_replics\t     Sr_words\n')
print '\n'.join('%s\t\t%d\t\t%d'%(key, val1, val2) for key, val1, val2 in finlist)