# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:11:14 2020

This code is for hashing the solution of Fizz Buzz
"""

n = 18
def fizzBuzz(n):
    # This is for the answer
    L =[]
    # This is a dictionary to store all the values
    z_dict = {3: "Fizz",
              5: "Buzz"}
    
    for i in range(1, n+1):
        ans_str = ""
        for key in z_dict.keys():
            if i%key == 0:
                ans_str += z_dict[key]
        if not ans_str:
            ans_str = str(i)
        L.append(ans_str)
    return L

print(fizzBuzz(n))