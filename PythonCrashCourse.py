# -*- coding: utf-8 -*-
"""
Created on Wed May 16 13:37:21 2018

@author: Venkat
"""

print(20/4)

num = 19
name = 'VSVR'

print(f"My number is {num} and name is {name}")
print("My number is {} and name is {} ".format(num, name))
print("My number is {one} and name is {two} and am {one} ".format(one= num, two= name))

nest = [1,2,3,[4,5,['target']]]
print(nest[3])
print(nest[3][2][0])

nesty = [1,2,[3,4]]
#print(nesty[2][1])

print("DICTIONARIES")

first_dict = {'key1': 'VSVR',
              'key2': 19}

print('key1')
print(['key1'])
print(first_dict['key1'], first_dict['key2'])

list_dict = {'k1':[19,33,22]}
print(list_dict['k1'])
print(list_dict['k1'][0])

my_list = list_dict['k1']
print(my_list[1])


nested_dict = {'k1':{'innerkey':[1,2,3]}}
print(nested_dict['k1']['innerkey'][1])

print("WHILE LOOP")

i = 0
while i <= 5:
    #print(i)
    print("i value here is: {}".format(i))
    #print(f,"i value is: {i}")
    i = i + 1

"""
print(f"Account owner is: {acct1.ownerName}")
    
print(f"My number is {num} and name is {name}")
print("My number is {} and name is {} ".format(num, name))
print("My number is {one} and name is {two} and am {one} ".format(one= num, two= name))
"""

list_num = [1,2,3,4]
print([num**2 for num in list_num])
print([num % 2 == 0 for num in list_num])

print("MAP FILTER AND LAMBDA!! AGAIN!!")

seq = [1,2,3,4,5]

print(list(map(lambda num: pow(num,2), seq)))
print(list(filter(lambda num: pow(num,2), seq)))

print("TUPLE UNPACKING")

x = [(1,2), (3,4), (5,6)]

a = (3,6)
b = (6,9)

x , y = a
i, j = b

print(x,y,i,j)