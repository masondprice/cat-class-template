#Revmoe pass and complete the cat class
class Cat():
    def __init__(self):
        self.name = "Unknown"
        self.age = 0

    def speak(self):
        print("Meow")

#Create objects here
#These should NOT be indented inside the class

Stella = Cat()
Stella.name = "Stella"
Stella.age = 7

Garfield = Cat()
Garfield.name = "Garfield"
Garfield.age = 50

Stella.speak()

Garfield.speak()