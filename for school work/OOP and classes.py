#----------------------------------------------------------------------------------------------#

class Dog:
    #class attribute
    species = "Canis familiaris"
    #instance attribute
    def __init__(self, name, age): #properties that all X(dog) must have are defined here (every new dog class sets the initial state by assigning the value of the properties) 
        self.name = name #init initializes each new instance of the class
        self.age = age #creates an attribute called (X) and assigns to it the value of the (X) perameter 

#----------------------------------------------------------------------------------------------#

    def description(self): #description is not needed when __str__ is used
        return f"{self.name} is {self.age} years old" 

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound): #speak has a perameter called sound
        return f"{self.name} says {sound}"


buddy = Dog("Buddy", 9) #Dog() summons. the inside of the bracket is the order of init
Miles = Dog("Miles", 4) #due to order, miles is name and 4 is age

print(buddy.description()) #code when def description is used
print(buddy)  #without __str__, this just prints location of the code in the pc
print(buddy.speak("woof"))#prints buddy says woof

#----------------------------------------------------------------------------------------------#

print(buddy.name)#prints name attribute inside buddy
print(buddy.age)#prints age attribute inside buddy
print(buddy.species)#prints species of dog class as it is not in instance attribute
#attributes can be changed
buddy.age = 10
print(buddy.age)

#----------------------------------------------------------------------------------------------#

class Bulldog(Dog): #makes a child class from Dog class
    pass

class Husky(Dog):
    pass

jim = Bulldog("Jim", 5)
print(isinstance(jim, Dog))#should return with true
print(isinstance(jim, Husky))#should return with False (2nd var must be a real class or error)

#----------------------------------------------------------------------------------------------#
#override method defined in parent class

class Bulldog(Dog):
    def speak(self, sound="arf"): # sets sound to "arf"
        return f"{self.name} says {sound}"


class Bulldog(Dog):
    def speak(self, sound="arf"):  # sets sound to "arf"
        return super().speak(sound) #super() searches for a parent class and takes .speak from it


john = Bulldog("John", 8) #new instance must be made for it to work
print(john.speak())

#----------------------------------------------------------------------------------------------#
