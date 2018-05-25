# -*- coding: utf-8 -*-
"""
Created on Tue May 15 19:24:56 2018

@author: Venkat
"""

"""NESTED STATEMENTS AND SCOPE"""

"""VOLUME OF A SPHERE"""

def vol(rad):
    print("VOLUME OF A SPHERE")
    """4/3 pi r^3"""
    #four_three = 4/3
    #pi = 22/7
    #rads = pow(rad,3)
    #ans = ((4/3)*(22/7)*(pow(rad,3)))
    #print("Four_Three, Pi, Rads", four_three, pi, rads)
    return((4/3)*(22/7)*(pow(rad,3)))

print(vol(2))

"""CONVERTING TO A LAMBDA FUNCTION

radii = 2
print(list(map(lambda ans: ans((4/3)*(22/7)*(pow(radii,3))), radii)))
"""
"""RAN CHECK"""

def ran_check(num, low, high):
    print("RAN CHECK")
    if(num in range(low, high)):
        final = True
    elif(num not in range(low, high)):
        final = False
    
    return final

print(ran_check(55,1,10))

def up_low(s):
    print("UP LOW")
    upper = 0
    lower = 0
    word_list = s.split(' ')
    for i in word_list:
        for j in i:
            if(j.isupper()):
                upper = upper + 1
            elif(j.islower()):
                lower = lower + 1
    
    print(upper, lower)
    
(up_low("Hello Mr. Rogers, how are you this fine Tuesday?"))

def unique_list(lst):
    print("UNIQUE LIST")
    seti = set(lst)
    
    return seti
    
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

def multiply(numbers):
    print("MULTIPLY")
    res = 1
    for i in numbers:
        res = res * i
    return res

print(multiply([1, 2, 3, -4]))

def palindrome(s):
    print("PALINDROME")
    string_check = s[::-1].lower()
    if(s.lower() == string_check):
        palindrome = True
    elif(s.lower() != string_check):
        palindrome = False
    
    #print(s, string_check)
    return(palindrome)
        
#palindrome("Malayalam")
print((palindrome("Telugu")))
    
import string
def ispangram(str1, alphabet = string.ascii_lowercase ):
    print("IS PANGRAM")
    str1 = str1.replace(" ", "").lower()
    str1 = ''.join(sorted(set(str1))).strip()
    
    """
    if(str1 == alphabet):
        result_pan = True
    elif(str1 != alphabet):
        result_pan = False
        
    return result_pan"""
    
    return (str1 == alphabet)
    
#ispangram("The quick brown fox jumps over the lazy dog")
print(ispangram("The quick brown fox jumps over the lazy dog"))
#print(ispangram("The brown fox jumps over the lazy dog"))