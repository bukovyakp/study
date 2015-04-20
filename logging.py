def logging(func, *args, **kwargs):
    res = func(*args, **kwargs)
    print 'calling %s, returned %r' % (func.__name__, res)
    return res

def double(x):
    "Doubles a number"
    return 2*x

print logging(double, 155)