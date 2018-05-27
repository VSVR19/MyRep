# -*- coding: utf-8 -*-
"""
Created on Mon May 21 18:51:59 2018

@author: Venkat
"""
print("NUMPY LEARNING; FOR THE FIRST TIME!!")

my_list = [19,33,44,32]
#print(my_list)

import numpy as np

arr = np.array(my_list)
print(arr)

my_mat = [[1,2,3],[4,5,6],[7,8,9]]
print(np.array(my_mat)) 

my_array = np.arange(0,19,2)
print(my_array)

print(np.zeros(5))
zero_array = np.zeros((3,3))
#print(zero_array)

print("COMEBACK BID!")
import numpy as np

print("A LIST AND A MATRIX")
my_list = [19,32,33,]

print(my_list)

print(np.array(my_list))

my_mat = [[19,32,33],[19,22,99],[12,5,27]]

print(my_mat)
print(np.array(my_mat))

print("A-RANGE FUNCTION")
print(np.arange(0,11))
print(np.arange(0,11,2))

print("ZERO ARRAY")
print(np.zeros(3))
print(np.zeros((2,3)))

print("ONE ARRAY")
print(np.ones((3,5)))

print("LINSPACE")
print(np.linspace(0,10,15))

print("A RANDOM MATRIX")
print(np.random.rand(5))
print(np.random.rand(5,5))

print("RANDOM N")
print(np.random.randn(7,7))

print("RAND INT")
print(np.random.randint(1,100,3))

print("USEFUL ATTRIBUTES AND METHODS OF A ARRAY OBJECT")
arr = np.arange(25)
print(arr)

print(np.random.randint(0,50,10))

print("RESHAPE METHOD")
print(arr.reshape(5,5))

print("MAX AND MIN IN A RAND ARR")
randarr = np.random.randint(0,50,10)
print(randarr,randarr.max(),randarr.min())

print("LOCATION OF MAX AND MIN IN A RAND ARR")
print(randarr.argmax(),randarr.argmin())

print(randarr.reshape(2,5))

print("DATA TYPE OF A ARRAY")
print(randarr.dtype)

print("************************************")
print("NUMPY ARRAY INDEXING AND SELECTION")

print(np.arange(0,20))

print(arr)
print(arr[:])
print("SAME AS LIST LISING")

two_d = np.random.rand(5,5)
print(two_d)
print(two_d[2:])

print("ARRAY BROADCASTING")
two_d[3:5] = 19
print(two_d)

print("ARRAY COPY METHOD")
two_dee = two_d.copy()
print(two_dee)

print("INDEXING A MATRIX")
two_d_array = np.array([[22,33,44],[55,77,99],[11,66,88]])
print(two_d_array)

array_two = np.arange(25)
print(array_two)
print(array_two.reshape(5,5))

print(two_d_array[0])
print("PRINT PARTICULAR PORTIONS OF A MATRIX")
print(two_d_array)
print(two_d_array[:2,1:])

print(two_d_array[1:,1:])

print("TRUE OR FALSE IN A ARRAY")
true_array = np.arange(1,11)
bool_array = true_array > 5
print(bool_array)
print(true_array[bool_array])

check_array = np.arange(1,9)
print(check_array[check_array > 5])

three_array = np.arange(0,20)
print(three_array[three_array > 15])

print("EXCERCISE ARRAY")
exc_array = np.arange(50).reshape(5,10)
print(exc_array)
print(exc_array[1:3, 3:5])

print("NUMPY OPERATIONS")

opp_array = np.arange(0,11)
print(opp_array)
print(opp_array + opp_array)
"""
print("Dividing array by itself")
print(opp_array / opp_array)

print("Dividing array by one")
print(1 / opp_array)
"""
print("UNIVERSAL ARRAY FUNCTIONS")

print(np.sqrt(opp_array))
print(np.exp(opp_array))
print(np.max(opp_array))
print(np.min(opp_array))
