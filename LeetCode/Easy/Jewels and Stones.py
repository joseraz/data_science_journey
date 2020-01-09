# -*- coding: utf-8 -*-
"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  
Each character in S is a type of stone you have.  
You want to know how many of the stones you have are also jewels.
The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

def numJewelsInStones(J, S):
    stone_dict = {}
    for i in J:
        stone_dict[i] = 0
    for i in S:
        if i in stone_dict:
            stone_dict[i] += 1 
    ans = 0
    for stone, counter in stone_dict.items():
       ans += counter  
    return ans
    
x = "aA" 
y = "aAAbbbb"
print(numJewelsInStones(x, y))