
from tkinter import END


class Car:

    def __init__(self, Owner, Model, Color, license):
        self.Owner = Owner
        self.Model = Model
        self.Color = Color
        self.license = license


    def __str__(self):
        print(f"{self.Owner}'s {self.Model} is {self.Color}.") #return only needed for the last line
        if self.license == True:
            return f"License is Valid"
        elif self.license == False:
            return f"License is Invalid"

    @classmethod
    def from_input(cls):
        return cls(
            input('Name: '),
            input('Car model: '),
            input('Car color: '),
            eval(input('You have a valid license (True or False): ')), #eval used when answer is either true or false.
        )


user = Car.from_input()

print(user)

con = input("would you like to add another car?: ")
if con == "yes":
    user2 = Car.from_input()
    if con == "no":
        END

jack = Car("Jack", "Ford F150", "Silver", True)

print(jack)



