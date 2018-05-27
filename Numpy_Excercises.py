# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:14:19 2018

@author: Venkat
"""

import numpy as np

print("ARRAY OF 10 ZEROS")
print(np.zeros(10))


print("ARRAY OF 10 ONES")
print(np.ones(10))


print("ARRAY OF 10 FIVES")
print((np.ones(10)) * 5)
print((np.zeros(10)) + 5)

print("Array of the integers from 10 to 50")
print(np.arange(10,51))


print("Array of even integers from 10 to 50")
print(np.arange(10,51,2))


print("3x3 matrix with values ranging from 0 to 8")
three_array = np.arange(0,9).reshape(3,3)
print(three_array)

print(np.arange(0,9).reshape(3,3))

print("3x3 identity matrix")
print("Gothila")
print(np.eye(3))
print("Eevage gothaythu")

print("RANDOM NUMBER BETWEEN 0 and 1")
#print(np.random.randint(0.0,2.0,1))
print(np.random.rand(1))

print("Array of 25 random numbers sampled from a standard normal distribution")
print("USING RAND")
print(np.random.rand(5,5))

print("USING RANDN")
print(np.random.randn(5,5))

print("A SPECIFIC MATRIX")
print(np.arange(0.01,1.01,0.01).reshape(10,10))
print("A SPECIFIC MATRIX USING LINSPACE")
print(np.linspace(0.01,1,100).reshape(10,10))

#print("20 LINEARLY SPACED POINTS BETWEEN 0 AND 1")
#print(np.arange(0,1.05263158,0.05263158))

print("20 LINEARLY SPACED POINTS BETWEEN 0 AND 1 USING LINSPACE")
print(np.linspace(0,1,20))

print("NUMPY INDEXING AND SELECTION")
print("Excercise 1")
mat = np.arange(1,26).reshape(5,5)
print(mat)
#print(np.linspace(1,25,25).reshape(5,5))

print("Excercise 2")
#print(mat[2:2,3])
print(mat[2:,1:])

print("Excercise 2.1")
print(mat[3,4])

print("Excercise 3")
print(mat[0:3,1].reshape(3,1))
print("A FINER APPROACH")
print(mat[0:3,1:2])

print("Excercise 4")
"""exc4 = [21,22,23,24,25]
print(np.array(exc4).reshape(1,5))"""
#print(mat)
#print("\n")
#print(np.arange(21,26).reshape(1,5))
#print("\n")
print(mat[4:,])

print("Excercise 5")
print(mat[3:,])

print("NOW DO THE FOLLOWING")
print("Excercise 6")

#exc6 = np.arange(0,25).reshape(5,5)
#print(exc6)
print(mat.sum())

print("Excercise 7")

exc7 = np.arange(0,25).reshape(5,5)
print(mat.std())

print("Excercise 8")

exc8 = np.arange(0,25).reshape(5,5)
print(mat.sum(axis = 0))