def tracer(func, *pargs, **kargs):
	print ('calling: ', func.__name__)
	return func(*pargs, **kargs)
	