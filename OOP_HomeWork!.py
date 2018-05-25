# -*- coding: utf-8 -*-
"""
Created on Sat May 19 09:16:38 2018

@author: Venkat
"""

print("CYLINDER CLASS")

class Cylinder:
    
    def __init__(self, height = 1, radius = 1):
            self.height = height
            self.radius = radius

    def volume(self):
        volume = 3.14 * (self.radius * self.radius) * self.height
        #print(f"Volume: {volume}".format(volume))
        return(volume)
        
    
    def surface_area(self):
        #2pirh
        #surface_area = (2 * 3.14 * self.radius * self.radius) + (2 * 3.14 * self.radius * self.radius)
        surface_area = (2 * 3.14 * self.radius * self.height)
        #Both these formulas are wrong!
        return(surface_area)
    

c = Cylinder(2,3)
print("Volume is: ",c.volume(),"cc")
print("Surface area is:",c.surface_area(),"m^2")


print("Line Class")

import math
class Line:
    
    tuple_list = []
    
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        Line.tuple_list = [self.coor1, self.coor2]
        part_one = pow((self.tuple_list[1][0] - self.tuple_list[0][0]), 2)
        part_two = pow((self.tuple_list[1][1] - self.tuple_list[0][1]), 2)
        sum = part_one + part_two
        distance = math.sqrt(sum)
        return(distance)
        
        """print("00 element is:",self.tuple_list[0][0])
        print("01 element is:",self.tuple_list[0][1])
        print("10 element is:",self.tuple_list[1][0])
        print("11 element is:",self.tuple_list[1][1])        """

        #(3,	2)   (8,	10)
        #x1	y1     x2	y2
    def slope(self):
        y_part = (self.tuple_list[1][1] - self.tuple_list[0][1])
        x_part = (self.tuple_list[1][0] - self.tuple_list[0][0])
        slope = y_part/ x_part
        return(slope)
        
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print("Distance is: ",li.distance())
print("Slope is: ",li.slope())

print("CHALLENGING PROBLEM!!")

class Account:
        
    def __init__(self,ownerName, accountBalance):
        self.ownerName = ownerName
        self.accountBalance = accountBalance
        
    def __str__(self):
        return(f"Account Owner: {self.ownerName}; Opening Account balance: Rs.{self.accountBalance}")
        
    def depositHere(self, depositAmount):
        #self.depositAmount = depositAmount
        self.accountBalance = self.accountBalance + depositAmount
        print(f"You deposited Rs.{depositAmount} and your new balance is {self.accountBalance}")
        
    def withdrawHere(self, withdrawalAmount):
        if(withdrawalAmount > self.accountBalance):
            print("You dont have sufficient funds to proceed with this transaction")
        
        if(withdrawalAmount <= self.accountBalance):
            self.accountBalance = self.accountBalance - withdrawalAmount
            print(f"You withdrew Rs.{withdrawalAmount} and your new balance is {self.accountBalance}")
        
acct1 = Account('VVS',5000)
print(acct1)
acct1.depositHere(500)
acct1.withdrawHere(55)

print(f"Account owner is: {acct1.ownerName}")
print(f"Account balance is: Rs.{acct1.accountBalance}")