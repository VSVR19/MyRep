# -*- coding: utf-8 -*-
"""
Created on Tue May 15 17:44:53 2018

@author: Venkat
"""

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square, my_nums):
    print(item)
    
print(list(map(square, my_nums)))

def square(lists=[]): 
    squr = []
    for i in lists:
        i = i**2
        squr.append(i)
    return squr
print(square([1,2,3]))

def splicer(stringe):
    reses = ''
    if(len(stringe) % 2 == 0):
        reses = 'EVEN'
    else:
        reses = 'ODD'
    return reses

namo = ['Venkat', 'Chinnu', 'Bullaa','Ram']
print(list(map(splicer, namo)))
#namo = 'Ram'
#print(map(splicer, namo))

def check_even(nums):
    return(nums % 2 == 0)

my_nums = ([1,2,3,4,5,6,7])

print(list(filter(check_even, my_nums)))
"""
STARTING CONVERSION FROM A NORMAL TO LAMBDA EXPRESSION
"""
def square(num):
    result = num**2
    return result   

print(square(5))


def square(num):
    return num ** 2

print(square(5))

def square(num): return num ** 2

print(square(5))

lambda num: num **2

print(square(5))
"""
ENDING CONVERSION
"""
"""A LAMBDA EXPRESSION FOR SQUARING"""
print(list(map(lambda num: num ** 2, my_nums)))

"""A LAMBDA EXPRESSION FOR EVEN FILTERING"""
print(list(map(lambda nums:nums % 2 == 0, my_nums)))

"""FILTER FUNCTION"""
def check_even(nums):
    return(nums % 2 == 0)

my_nums = ([1,2,3,4,5,6,7])

print(list(filter(lambda nums: nums % 2 == 0, my_nums)))

""" TRYING OUT A HARDER FUNCTION FOR CONVERSION"""
def first_char(jinxy = []):
    jinxs = []
    for i in jinxy:
        jinxs.append(i[0])
    return jinxs

print(first_char(['Chinnu','Bullaa']))
    

""" SIMPLYFING THE ABOVE FUNCTION"""
def first_char(jinx):
    jinxs = []
    jinxs.append(jinx[0])
    return jinxs
        
print(first_char("Bulla"))

"""NOW TRYING OUT"""

names = ["Bulla","Chinnu"]
print(list(filter(lambda wordie: wordie[0], names)))
print(list(map(lambda wordie : wordie[::-1], names)))
print(list(filter(lambda wordie : wordie[0], names)))
print(list(filter(lambda wordie : wordie[0], names)))



"""LAMBDA TO FIND GREATER OF TWO NUMBERS"""
print("LAMBDA TO FIND GREATER OF TWO NUMBERS")
greatest_num = lambda num, num1: a if(a >= b) else b
print(greatest_num(9,9))