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
"""CREATED AND CONVERTED"""

"""MAKE A LAMBDA FOR F TO C CONVERSION"""
def temp_convert(temp):
    return(((9.0/5) * temp) + 32)
print(temp_convert(0))

temp_convert = lambda temp: (((9.0/5) * temp) + 32)
print(temp_convert(0))
"""CONVERTED"""

"""MAKE A LAMBDA FOR EVEN MULTIPLICATIONS IN A LIST"""
def mul_twos(nums=[]):
    print("MUL TWOS")
    mul = 1
    for i in nums:
        if(i % 2 == 0):
           mul = mul * i
    return mul
print(mul_twos([2,99,33,4]))

mul_twos = lambda num, num1: num * num1 * 4
print(mul_twos(4,5))
"""NOT ABLE TO DO IT"""

"""INTRODUCING MAPS"""
def temp_convert(temp):
    return(((9.0/5) * temp) + 32)
print(temp_convert(0))

temp = [22,33,44,55]

print(list(map(temp_convert, temp)))
"""END OF A NORMAL FUNCTION"""

temp_faran = lambda temp : (((9.0/5) * temp) + 32)
print(temp_faran(40))
"""A LAMBDA FUNCTION"""

"""USING MAPS"""
temps = [222,333,444,555]
print(list(map(lambda temp : (9.0/5) * temp + 32, temps)))
"""USED MAPS"""

"""USING MAPS TO ADD TWO LISTS TOGETHER"""
a = [19,33,44]
b = [32,22,55]
c = [27,5,3]

print(list(map(lambda x,y,z: x + y + z, a, b, c)))
"""DONE"""

"""USING MAPS TO ADD TWO LISTS TOGETHER"""
negs = [99, 00, 5]
print(list(map(lambda a: a * -1, negs)))

"""INTRODUCING REDUCE"""

"""A PLAIN LAMBDA STATEMENT"""
print("A PLAIN LAMBDA STATEMENT")
major_sum = lambda a,b,c,d,e,f,g,h,i,j: a+b+c+d+e+f+g+h+i+j
print(major_sum(19,33,32,44,25,55,5,99,3,27))

"""INTRODUCING MAPS TO SUM ALL THE NUMBERS"""
jerseys = [19,33,32,44]
jerseys1 = [25,55,5,99]
jerseys2 = [3,27]
print("SUMMING JERSEYS")
print(list(map(lambda a,b,c: a+b+c, jerseys,jerseys1,jerseys2)))

"""INTRODUCING REDUCE TO ....ALL THE NUMBERS"""
"""jerseys = [19,33,32,44,25,55,5,99,3,27]
import functools

jerseys = [19,33,32,44]
jerseys1 = [25,55,5,99]
jerseys2 = [3,27]
print("SUMMING JERSEYS")
#print(list(functools.reduce(lambda a,b,c: a+b+c, jerseys,jerseys1,jerseys2)))
print(list(functools.reduce(lambda a: a+a, jerseys)))"""

"""LAMBDA TO FIND GREATER OF TWO NUMBERS"""
print("LAMBDA TO FIND GREATER OF TWO NUMBERS")
greatest_num = lambda juno, juno1: juno if(juno >= juno1) else juno1
print(greatest_num(9,9999))

def max_find(num, num1):
    #print("MAX FIND NORMAL FUNCTION")
    if num > num1:
        return num
    else:
        return num1
#print(max_find(33,22))

junos = [19,33,32,44,25,55,5,99,3,27]
print("MAX FIND USING REDUCE")
import functools
print(functools.reduce(max_find,junos))

print("LAMBDA TO ADD NUMS IN A LIST")
juno = [19,33,32,44,25,55,5,99,3,27]
res_sum = lambda a,b,c,d,e,f,g,h,i,j: a+b+c+d+e+f+g+h+i+j
print(res_sum(19,33,32,44,25,55,5,99,3,27))

print("TRYING MAP IN LAMBDA TO ADD NUMS IN A LIST")
list_num = [19,33,32,44,25,55,5,99,3,27]
print(list(map(lambda a: a+a , list_num)))

"""print(list(map(lambda sum: list_num+list_num , list_num)))"""

print("TRYING REDUCE IN LAMBDA TO ADD NUMS IN A LIST")
print("A NORMAL FUNCTION")
def list_add(num1,num2):
    sum = 0
    #for i in jinx:
     #   sum = sum + i
    return num1+num2
#print(list_add([19,33,32,44,25,55,5,99,3,27]))
list_num= [19,33,32,44,25,55,5,99,3,27]
print("TRYING REDUCE IN LAMBDA TO ADD NUMS IN A LIST")
print(functools.reduce(list_add, list_num))

"""INTRODUCING FILTERS"""
def even_check(num):
#    print("A EVEN CHECK FUNCTION")
    return(num % 2 == 0)

print(even_check(5))

number_list = [0,1,2,3,4,5,6,7,8,9,10]
print(number_list)

"""INTRODUCING FILTERS"""
print(list(filter(even_check, number_list)))

"""A LAMBDA FUNCTION FOR EVEN CHECK"""

print(list(map(lambda number: number% 2 == 0, number_list)))
print(list(filter(lambda number: number% 2 == 0, number_list)))
"""BOTH WORK!!"""

"""A LAMBDA FUNCTION FOR NUM > 3"""
print(list(map(lambda number: number > 3, number_list)))
print(list(filter(lambda number: number > 3, number_list)))