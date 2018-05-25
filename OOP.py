# -*- coding: utf-8 -*-
"""
Created on Fri May 18 10:34:36 2018

@author: Venkat
"""

print("----------FINALLY TAKING ON OOP IN PYTHON!!----")

my_list = [1,2,3]

print(type(my_list))

print("FIRST CLASS")
class HHMSampleClass():
    pass
"""OBJECT CREATION"""
sample_object = HHMSampleClass()
print(type(sample_object))

print("A MORE RELATABLE CLASS")

class Lion():
    classification = 'Mammal'
    
    def __init__(self, species, color, spots):
        self.species = species
        self.color = color
        self.spots = spots
        
    def roar(self, name):
        print("A defeaning roar indeed by the {} {}!".format(name, self.species))
        print("This Lion is classified as a {}".format(self.classification))

my_lion = Lion(species= 'Asiatic_Lion', color= "Silver_Sheen",
              spots= False)

print(type(my_lion))

print(my_lion.classification,
      my_lion.species, my_lion.color, my_lion.spots)

print(my_lion.roar("Shivaji"))

print("A SECOND EXAMPLE FOR A CLASS")

class HemiSphere():
    pi = 3.14
    
    def __init__(self, radius):
        self.radius = radius
        self.area = radius * radius * HemiSphere.pi
    
    def calculate_circumference(self):
        return self.radius * self.radius * 2
    
mySphere = HemiSphere(19)
print(mySphere.pi, mySphere.radius, mySphere.area)
print(mySphere.calculate_circumference())

print("INHERITANCE AND POLYMORPHISM")

print("Tennis Class")
class Tennis():
    
    def __init__(self):
        print("Game On!")
        
    def GOAT(self):
        print("Roger Federer")
        
    def grandSlams(self, count):
        print("OMG! Hes won {} of them!!".format(count))
        
tennis_game = Tennis()
tennis_game.GOAT()
tennis_game.grandSlams(20)

print("Cricket Class")
class Cricket(Tennis):
    
    def __init__(self):
        Tennis.__init__(self)
        print("Cricket On!!")
    
    def grandSlams(self, count):
        print("We have won {} World Cups!!".format(count))
        
    def greatestNames(self, legends):
        print("One of the greatest name: {}".format(legends))
            
cricket_game = Cricket()
cricket_game.GOAT()
cricket_game.grandSlams(2)
cricket_game.greatestNames("Dravid")
"""
print("POLYMORPHISM:")

class Dog():
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return self.name + " Says Milo"
    
class Cat():
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return self.name + " Says Tom"
    
doggie = Dog("Milo")
tommis = Cat("Tom")

print(doggie.speak(), tommis.speak())

def pet_speak(pet):
    print(pet.speak())

print(pet_speak('Milo'))
print(pet_speak('Tom'))"""

print("INHERITANCE PRACTICE")

class SportsPlay():
    jerseyNumber = 19
    
    def __init__(self, secondJerseyNumber):
        print("My Nums: {} {}".format(SportsPlay.jerseyNumber, secondJerseyNumber))
    
    def likedSports(self, sport1, sport2):
        print("Sports I like: {} {}"
              .format(sport1, sport2))
        
gameOn = SportsPlay(33)
print(gameOn.likedSports("Badminton and","Cricket"))

class Cricket(SportsPlay):
    def __init__(self):
        #Cricket.__init__(self)
        print("Cricket On!!")
        
    def favPlayer(self,favPlayer):
        print("My fav here: {}".format(favPlayer))
        
cricketOn = Cricket()
cricketOn.favPlayer("Dada")

print("BACK AGAIN!TO KNOCK OVER POLYMORPHISM!!")

class Dog():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return(self.name + " Says 'Hello'")
        
doggie = Dog("Milo")
print(doggie.speak())
    
class Cat():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return(self.name + " Says 'Hello'")
        
cattie = Cat("Tom")
print(cattie.speak())

print("DEMOING POLYMORPHISM VIA AN ITERATOR")
print("MUCH BETTER!")
for i in [doggie, cattie]:
    print(type(i), i.speak())

print("DEMOING POLYMORPHISM VIA A FUNCTION")
def PetsTime(pet):
    print(pet.speak())
    
print(PetsTime(doggie))
print(PetsTime(cattie))

print("ABSTRACT CLASSES!")

class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Do not implement; to be implemented by a sub-class")
        
class Dog(Animal):
    def speak(self):
        return(self.name + "Says Hi")
        
class Cat(Animal):
    def speak(self):
        return(self.name + "Says Hello")

doggy = Dog("Milo")
catty = Cat("Tomis")

print("SPECIAL METHODS!!")

class SpecialMethods():
    def specialBooks(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
    
        return("My books details Name: {} Author: {} Pages: {}".format(name, author, pages))
        
    def __str__(self):
        
        return(f"{self.name} by {self.author} has {self.pages} pages")
        
    def __len__(self):
        
        return(self.pages)
        
    def __del__(self):
        
        print("A book object has been deleted")
               
specalio = SpecialMethods()
print(specalio.specialBooks("AJCBU", "VSVR19", 619))

#print(str(specalio))
print(len(specalio))
del(specalio)

print(len(specalio))    