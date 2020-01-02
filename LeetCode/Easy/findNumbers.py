# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 17:08:06 2020

@author: joera
"""

def findNumbers(nums):
    counter = 0
    for i in nums:
        if len(str(i))%2 ==0:
            counter += 1
    return counter

x = [12,345,2,6,76]
findNumbers(x)

def findNumbers2(nums):
    return sum(1 for i in nums if len(str(i))%2 == 0)

x = [12,345,2,6,76]
findNumbers2(x)

