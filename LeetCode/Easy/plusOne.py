# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:34:13 2020

@author: joera
"""
def plusOne(digits):
    L = []
    num = ""
    for i in digits:
        num += str(i)
    num = int(num)+1
    num = str(num)
    for i in num:
        L.append(int(i))
    return L

digits = [1,2,3]
plusOne(digits)   

digits = [1,2,9]
plusOne(digits)   