'''
Created on Mar 24, 2015

@author: pavel
'''
def factorial(n):
    def factIter(product, counter):
        if counter>n:
            return product
        else:
            return factIter(counter*product, counter+1);
    return factIter(1, 1)

print (factorial(10))