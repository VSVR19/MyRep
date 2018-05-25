# -*- coding: utf-8 -*-
"""
Created on Fri May 11 13:19:53 2018

@author: Venkat
"""

def pig_latin(test):
    list_names = []
    for word in test.split(' '):
        letter = [word[0]]
        checker = ''.join(letter)
        if checker in ['a','e','i','o','u','A','E','I','O','U']:
                word = word + checker
                word = word + 'ay'
                list_names.append(word)
                
        else:
            word = word + 'ay'
            list_names.append(word)
    return list_names
    
result=  pig_latin("Roger Anil Sourav Inzamam Rahane Dravid")
print('\n'.join(result))