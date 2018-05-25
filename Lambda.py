# -*- coding: utf-8 -*-
"""
Created on Wed May 16 16:21:58 2018

@author: Venkat
"""

def square(num):
    return(pow(num, 2))
print(square(4))

def square(num): return(pow(num, 2))
print(square(5))


square = lambda num: pow(num, 2)
print(square(6))

"""TRYING LAMBDA FOR EVEN CHECK"""
def even_check(numo):
    return(numo % 2 == 0)
print(even_check(4))

result = lambda numo: numo % 2 == 0
print(result(5))
"""CONVERTED"""

"""TRYING LAMBDA TO GRAB FIRST CHARACTER OF A STRING"""
def first_char(word):
    return(word[0])
print(first_char("Sindhu Yasho"))

wordie = lambda word: word[0]
print(wordie("Hems Heena"))
"""CONVERTED"""

"""TRYING LAMBDA TO REVERSE A STRING"""
def str_rev(str):
    return(''.join(str[::-1])).lower()
print(str_rev("Bullaa"))

rev = lambda str: ''.join(str[::-1]).lower()
print(rev("Vaishu Ka"))
"""CONVERTED"""

"""MAKE A LAMBDA TO ACCEPT MULTIPLE PARAMETERS"""
"""ADDING 2 NUMBERS"""

def add_two(num, num1):
    return(num + num1)
print(add_two(2,22))

resi = lambda num, num1: num + num1
print(resi(22,222))
"""CREATED AND CONVERTED"""

"""MAKE A LAMBDA TO CHECK THE LENGTH OF A STRING"""

def str_len(str):
    return(len(str))
print(str_len("V.S.Venkata Ramana"))

length = lambda str : len(str)
print(length("V.S.Venkata Ramana"))