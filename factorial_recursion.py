# С использованием рекурсии (Такой процесс называется линейно рекурсивным процессом (linear recursive process))
def fact(n):
	if n == 0:
		return 1
	return fact(n-1)*n

print fact(10)

----------------------------
# С использованием цикла

def fac(n):
    fac = 1
    i = 0
    while i < n:
        i += 1
        fac = fac * i
    return fac

----------------------------
# lambda

def factorial(x):
    return 1 if x==0 else reduce(lambda x,y:x*y,xrange(1,x+1))

----------------------------

# lambda and recursion

f = lambda n: n-1 + abs(n-1) and f(n-1)*n or 1
----------------------------

'''Мы можем описать правило вычисления n!, сказав, что мы сначала умножаем 1 на 2, 
   затем результат умножаем на 3, затем на 4, и так пока не достигнем n. 
   Мы можем описать это вычисление, сказав, что счетчик и произведение с каждым шагом одновременно изменяются согласно правилу:

    произведение = счетчик · произведение
    счетчик = счетчик + 1

и добавив условие, что n! — это значение произведения в тот момент, когда счетчик становится больше, чем n. 
ТТакой процесс называется линейно итеративным процессом (linear iterative process) '''

def factorial(n):
    def factIter(product, counter):
        if counter > n:
            return product
        else:
            return factIter(counter*product, counter+1);
    return factIter(1, 1)