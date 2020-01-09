# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:42:12 2020

@author: joera
"""

def subtractProductAndSum(n):
    x, y = 0, 1
    for i in str(n):
        x += int(i)
    for j in str(n):
        y *= int(j)
    return y-x
        
x = 4421
print(subtractProductAndSum(x))


import numpy as np

def subtractProductAndSum(n):
    a = [int(x) for x in str(n)]
    return np.prod(a) - np.sum(a)

print(subtractProductAndSum(4421))