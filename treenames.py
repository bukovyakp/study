'''def suma(*args):
        result = 0
        for arg in args:
            if hasattr(arg, '__len__') and type(arg) != str:
                result += suma(*arg)
            elif type(arg) != str:
                result += arg
    
        return result

print suma(1,2,3,4)'''

def suma(*args):
    result = 0
    for arg in args:
        if type(arg) == str:
            for x in arg:
                try:
                    int(x)
                except:
                    pass
                else: 
                    b = (int(x))
                    result += b
    return result
print suma('12,4')        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    