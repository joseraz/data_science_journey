# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:10:55 2020

@author: joera
"""
n = 15
L=[]
def fizzBuzz(n):
    for i in range(1, n+1):
        if i%3 == 0 and i%5 == 0:
            L.append(str("FizzBuzz"))    
        elif i%3 == 0:
            L.append(str("Fizz"))
        elif i%5 == 0:
            L.append(str("Buzz"))
        else:
            L.append(str(i))
    return L        
    
print(fizzBuzz(n))