# -*- coding: utf-8 -*-
"""
Created on Fri May 11 13:02:58 2018

@author: Venkat
"""

def pig_latin():
    test = "Roger Anil Sourav Inzamam"
    list_names = []
    for word in test.split(' '):
        letter = [word[0]]
        #print("Check1")
        print(letter)
        if letter not in ['a','e','i','o','u','A','E','I','O','U']:
                print("In If")    
                word = word + 'ay'
                list_names.append(word)
                
        elif letter in ['a','e','i','o','u','A','E','I','O','U']:
                print("In ElIf")    
                word = word + str(letter)
                print("Check1", word)
                word = word + 'ay'
                list_names.append(word)
    print(list_names)
    
pig_latin()