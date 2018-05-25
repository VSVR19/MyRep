# -*- coding: utf-8 -*-
"""
Created on Sun May 20 19:56:22 2018

@author: Venkat
"""

class Exercise1():
    print("Excercise 1")
    
    result_list = []
    
    def __init__(self, square_list):
        self.square_list = square_list
        
    def calculate_power(self):
        for i in self.square_list:
            Exercise1.result_list.append(pow(i,2))
        
        return(Exercise1.result_list)
        
    def calculate_power_lambda(self):
        return(list(map(lambda num: pow(num, 2), self.square_list)))
        
exc1 = Exercise1([5,6])
    #print(exc1.calculate_power())
print(exc1.calculate_power_lambda())


class Excercise2():
    print("Excercise 2")
    
    def __init__(self,user_string):
        self.user_string = user_string
        
    def split_string(self):
        return(self.user_string.split(' '))

user_string = input("Enter your string to be split:")
exc2 = Excercise2(user_string)
print(exc2.split_string())

class Excercise3():
        print("Excercise 3")
    
    def __init__(self):
        pass
        
    def string_return(self,planet, diameter):
        return("The diameter of {} is {} kilometers".format(planet, diameter))
        
planet= input("Enter planet name:")
diameter= input("Now enter its diameter")
exc3 = Excercise3()
print(exc3.string_return(planet, diameter))


class Excercise4():
    print("Excercise 4")
    
    def __init__(self, user_list):
        self.user_list = user_list
        
    def return_hello(self):
        return(self.user_list[3][1][2])

exc4 = Excercise4([1,2,[3,4],[5,[100,200,['hello']],23,11],1,7])
print("".join(exc4.return_hello()))


class Excercise5():
    print("Excercise 5")
    
    def __init__(self):
        pass
    
    def dict_hello(self,user_dict):
        return(user_dict['k1'][3]['tricky'][3]['target'] [3])
        
exc5 = Excercise5()
print(exc5.dict_hello({'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}))


class Excercise5():
    print("Excercise 5")
    mailID = input("Enter your mailID:")
    def __init(self,mailID):
        self.mailID = mailID
    
    def mail_domain(self):
        at_index= self.mailID.index('@')
        #return(at_index)
        return(self.mailID[at_index+1:])
        
exc5 = Excercise5()
print(exc5.mail_domain())


class Excercise6():
    print("Excercise 6")
    
    def __init(self):
        pass
    
    def findDog(self, search_string):
        return('dog' in search_string.lower())

search_string = input("Enter a stirng for 'Dog' search:")        
exc6 = Excercise6()
print(exc6.findDog(search_string))


class Excercise7():
    print("Excercise 7")
    
    def __init__(self,search_string):
        self.search_string = search_string.lower()
        
    def dogCount(self):
        return(self.search_string.count('dog'))

search_string = input("Enter a string for 'Dog' search:")
exc7 = Excercise7(search_string)
print(exc7.dogCount())


class Excercise8():
    print("Excercise 8")
    
    def __init__(self):
        pass
    
    def s_filter(self, work_list):
        return(list(filter(lambda word: word[0] == 's',work_list)))
        #return(list(map(lambda word: word[0] == 's',work_list)))
        
exc8 = Excercise8()
print(exc8.s_filter(['soup','dog','salad','cat','great','suguna','motors']))

class Excercise9():
    result = ''
    def __init__(self):
        pass
    
    def determine_ticket(self,train_speed, is_birthday):
        if(train_speed <= 60):
            Excercise9.result = "No Ticket"

        if(is_birthday == 'True'):
            if(train_speed in range(66,86)):
                Excercise9.result = "Small Ticket"
            elif(train_speed >= 86):
                Excercise9.result = "Big Ticket"
    
        elif(is_birthday == 'False'):
            if(train_speed in range(61, 81)):
                Excercise9.result = "Small Ticket"
            elif(train_speed >= 81):
                Excercise9.result = "Big Ticket"
                
        return(Excercise9.result)
        
            
train_speed = int(input("Enter the speed at which you drove the train:"))
is_birthday = input("Is your birthday today ?")
exc9 = Excercise9()
print((exc9.determine_ticket(train_speed, is_birthday)))