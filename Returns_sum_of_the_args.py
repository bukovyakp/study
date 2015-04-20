def suma(*args):
        result = 0
        for arg in args:
            if hasattr(arg, '__len__') and type(arg) == str:
                result += suma(*arg)
            if hasattr(arg, '__len__') and type(arg) != str:
                result += suma(*arg)
            elif type(arg) != str:
                result += arg
    
        return result

print suma(2,3,4)