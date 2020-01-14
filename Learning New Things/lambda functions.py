# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 22:48:47 2020

@author: joera
"""
# Normal function form
def square(a):
    return a*a

result = square(5)

print(result)

# My first lambda function
f = lambda b : b*b

test = f(5)

print(test)

# Second lambda function
# Why does this not work?
g = lambda x,y : x + y

ans = f(5,6)

print(ans)