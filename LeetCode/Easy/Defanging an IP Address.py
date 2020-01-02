# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:55:44 2020

@author: joera
"""


def defangIPaddr(address):
    new_address = address.replace(".", "[.]")
    return new_address
        
x = "255.100.50.0"
print(defangIPaddr(x))