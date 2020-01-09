# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 17:23:00 2020

@author: joera
"""

def isPalindrome(s):
    x = ''
    for i in s:
      if i.isalnum():
        x += i.lower()
    return x==x[::-1] 

x = "A man, a plan, a canal: Panama"
print(isPalindrome(x))

y = "race a car"
print(isPalindrome(y))
