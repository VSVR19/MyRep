# -*- coding: utf-8 -*-
"""
Created on Sat May 12 17:45:47 2018

@author: Venkat
"""


"""
WARMUP SECTION
Lesser of two evens

"""
def even_odd(a,b):
    print("LESSER OF TWO EVENS")
    result = 0
    if((a % 2 == 0) and (b % 2 == 0) and (a < b)):
        result = a
    elif((a % 2 == 0) and (b % 2 == 0) and (a > b)):
        result = b
    elif(((a % 2 == 0) or (b % 2 == 0)) and (a < b)):
        result = b
    elif(((a % 2 == 0) or (b % 2 == 0)) and (a > b)):
        result = a
    elif(((a % 2 != 0) or (b % 2 != 0)) and (a > b)):
        result = a
    if((a % 2 != 0) and (b % 2 != 0) and (a < b)):
        result = b
    elif((a % 2 != 0) and (b % 2 != 0) and (a > b)):
        result = a
    
    return result

print(even_odd(0,19))

"""
ANIMAL CRACKERS
"""

def animal_crackers(word):
    print("ANIMAL CRACKERS")
    outs = 0
    word_list = word.lower().split(' ')
    if(word_list[0][0] == word_list[1][0]):
        #print("In If")
        outs = True
    elif(word_list[0][0] != word_list[1][0]):
        #print("In Elif")
        outs = False
    
    return outs

print(animal_crackers('Chinnu Bullaa'))
#print(animal_crackers('Chinnu Bullaa'))

"""
"""

def makes_twenty(num, num1):
    print("MAKES TWENTY")
    if((num >= 20) or (num1 >= 20) or (num+num1 >= 20)):
        out = True
    else:
        out = False
    return out

print(makes_twenty(20,20))

"""
LEVEL 1 PROBLEMS
OLD MACDONALD
"""
"""
def old_macdonald(text):
    res_list = []
    for i in text:
        if((text.index(i) == 0) or (text.index(i) == 3)):
            print("if i",i)
            res_list.append(i.upper())
            print(res_list)
        else:
            print("else i",i)
            res_list.append(i.lower())
            print(res_list)
    #return(res_list)

old_macdonald('venkatvkker')

"""
"""
R O G E R F E D E R E  R
0 1 2 3 4 5 6 7 8 9 10 11
"""

def old_macdonald(text):
    print("OLD MACDONALD")
    indexes = (0,3)
    chars = list(text)
    for i in indexes:
        chars[i] = chars[i].upper()
    res_str = ''.join(chars)
    return(res_str)
print(old_macdonald("rogerfederer"))

def master_yoda(texts):
    print("MASTER YODA")
    reses= []
    result = ''
    for i in texts.split(' '):
        reses.append(i)
        result = reses[::-1]
        result = ' '.join(result)
    return(result)

print(master_yoda("Roger Watson Venkata Ramana Shewag Gambhir"))

def almost_there(nums):
    print("ALMOST THERE")
    outs = False
    res = abs(nums) - 100
    res1 = abs(nums) - 200
    
    if((abs(res) in range(0,21)) or (abs(res1) in range(0,21))):
        outs = True
    return outs

print(almost_there(209))

"""
LEVEL 2 PROBLEMS
"""

"""def has_33(jinks = []):
    print("Has 33")
    #outs = False
    place= 0
    place1 = 0
    for i in jinks:
        if(i == 3):
            place = jinks.index(i)
            #place1 = jinks.index(place + 1)
    print("Place Place1 " ,place,place1)
            #print("Place1" ,place1)
        #if((place == 3) and (place1 == 3)):
            #outs = True
    #return outs
    
has_33([3,3,44,67])"""

"""def has_33(jinx= []):
    print("HAS_33")
    maja = False
    place = 0
    place1 = 0
    for i in jinx:
        if (i == 3):
            place = jinx.index(i)
            place1 = place + 1
            place0 = place - 1
            #print(place1)
            #place2 = jinx.index(place1)
            j = jinx[place1]
            k = jinx[place0]
            if((i == j) and (i == k)):
                maja = True
                
    return maja
    #print(place,place1, " Place Place1")
    #print("I, J and K ",i,j,k)
#has_33([3,1,3]) 
print(has_33([1,3,3]))"""

def find_33(lists= []):
    print("FIND 33")
    reses = False
    for i in lists:
        if(i == 3):
            target_i = lists.index(i)
    left = target_i - 1
    right = target_i + 1
    
    #print("Target_i Left Right", target_i,left, right)
    #print("ListLeft, ListRight",lists[abs(left)], lists[abs(right)])
    
    if((lists[abs(left)] == 3) or (lists[abs(right)]) == 3):
        reses = True
    
    return reses
    
#print(find_33([3,1,3]))
#print(find_33([1,3,1,3]))
print(find_33([1,3,3]))
#find_33([3,1,3])

def paper_doll(test):
    print("PAPER_DOLL")
    reso = ''.join([charss*3 for charss in test])
    return reso

print(paper_doll("Mississippi"))

def blackjack(a,b,c):
    print("BLACKJACK")
    sum = a + b + c
    sum1 = 0
    if(sum <= 21):
        #print("In If 1")
        return sum
    if((sum > 21) and ((a == 11) or (b == 11) or (c == 11))):
        sum1 = sum - 10
        #print("Reducing Sum")
        
        #print("Sum1",sum1)
        #if(sum <= 21):
         #   return sum1
    #if(sum > 21):
     #   sum1 = sum - 10
        
    if(sum1 >= 21):
        #print("Assigning BUST")
        #sum = 'BUST
        #return "BUST"
        sum = "BUST"
    return sum
print(blackjack(9,11,11))

def summer_69(list= []):
    print("SUMMER 69")
    index_6 = 0
    index_7 = 0
    sum_part = 0
    sum_whole = 0
    sum_answer = 0
    for i in list:
        if(i == 6):
            index_6 = list.index(i)
        if(i == 9):
            index_7 = list.index(i)
    #print("Index 6, Index 7:", index_6, index_7)
    #print("Index_7+1 List Length",index_7+1, len(list))
    for i in range(index_6, index_7+1):
        sum_part = sum_part + list[i]
    for j in range(0, len(list)):
        sum_whole = sum_whole + list[j]
    
    sum_answer = sum_whole - sum_part
    #print(index_6, index_7)
    #print("Sum Part Sum Whole Sum Answer",
     #    sum_part, sum_whole, sum_answer)
    return sum_answer
    
#summer_69([1,3,5])
#summer_69([4,5,6,7,8,9])
#summer_69([1,3,5])    
print(summer_69([2,1,6,9,11]))
# 0 1 2 3 4 5-- 39

def spy_game(listy=[]):
    print("SPY GAME")
    seven_index = 0
    for i in listy:
        if(i == 0):
            first_zero = listy.index(i)
            #listy.remove(i)
            #listy[first_zero] = 99
        if(i == 0):
            second_zero = listy.index(i)
            #listy.remove(i)
        if(i == 7):
            seven_index = listy.index(i)
    
    #print("First Zero, Second Zero, Seven Index",
     #     first_zero, second_zero, seven_index)
    #print("Final List",listy)
    
    if((seven_index > first_zero) and (seven_index > second_zero)):
        resy = True
    else:
        resy = False
    return resy
#print(spy_game([1,2,4,0,0,7,5]))
#print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))