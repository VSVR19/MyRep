# -*- coding: utf-8 -*-
"""
Created on Fri May 11 10:34:44 2018

@author: Venkat
"""
"""
my_list = [1,2,3,4,6,7]

my_list.append(5)

print(my_list.pop())

print(my_list)"""

def my_first_function(name="Default", name1="Default1"):
    """
        Just a returning function
    """
    return name + str(name1)
        
out = my_first_function("VSVR",19)
print(out)
print("\n")

def add_two_numbers(n=0,n1=0):
    """
    Just adding two numbers
    """
    return(n+n1)
    
result = add_two_numbers(19,33)
print(result)
print("\n")

#Find out if a string has a word 'dog' in it'

def string_search(sentence="default"):
    return 'dog' in sentence.lower()

result = string_search("Aks Dog ran away")
print(result)


def pig_latin(test):
    for word in test.split(' '):
        for i in word:
            if i not in ['a','e','i','o','u']:
                word.join('ay')
                return(word)
            elif i in ['a','e','i','o','u']:
                word.join(i)
                word.join('ay')
                return(word)

outs = pig_latin("Roger Federer Sourav Ganguly")
print(outs)


def pig_latin(test):
    list_names = []
    for word in test.split(' '):
        letter = [word[0]]
        #for i in word:
            if i not in ['a','e','i','o','u']:
                word = word + 'ay'
                list_names.append(word)
                
            elif i in ['a','e','i','o','u']:
                word = word + i + 'ay'
                list_names.append(word)
    print(list_names)

pig_latin("Roger Anil Sourav Inzamam")


def pig_latin(test):
    list_names = []
    for word in test.split(' '):
        letter = [word[0]]
        if letter not in ['a','e','i','o','u']:
                word = word + 'ay'
                list_names.append(word)
                
        elif letter in ['a','e','i','o','u']:
                word = word + i + 'ay'
                list_names.append(word)
    print(list_names)

pig_latin("Roger Anil Sourav Inzamam")