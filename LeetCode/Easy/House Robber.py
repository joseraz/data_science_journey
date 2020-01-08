# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 20:15:13 2020

@author: joera
"""

def rob(nums):
    a, L = 0, []
    for k in range(2, len(nums)):
        a = 0
        for i in range(0,len(nums),k):
            a += nums[i]
        L.append(a)
    for k in range(2, len(nums)):
        a = 0
        for j in range(1,len(nums),k):
            a += nums[j]
        L.append(a)
    if len(nums) == 1:    
        L.append(nums[0])
    if len(nums) == 2:    
            L.append(max(nums[0],nums[1]))
    if not L:
        return 0
    else:
        return max(L)


def rob_2(nums):
    a, b = 0, 0
    for i in range(0,len(nums),2):
        a += nums[i]
    for j in range(1,len(nums),2):
        b += nums[j]
    return max(a,b)

x= [4,1,2,7,5,3,1]
print(rob(x))
