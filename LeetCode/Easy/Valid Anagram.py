# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 19:36:30 2020

@author: joera
"""

def isAnagram(s, t):
    d1, d2 = {}, {}
    for i in s:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    for i in t:
        if i in d2:
            d2[i] += 1
        else:
            d2[i] = 1
    return d1==d2
    
s="anagram"
t="nagaram"
isAnagram(s,t)