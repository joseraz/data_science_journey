# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:10:55 2020

@author: joera
"""
n = 18
def fizzBuzz(n):
    L =[]
    for i in range(1, n+1):
        r = ""
        if i%3 == 0: 
            r += "Fizz"
        if i%5 == 0:
            r += "Buzz"
        if i%7 == 0:
            r += "Jazz"
        if not r :
            r += str(i)
        L.append(r)
    return L

print(fizzBuzz(n))