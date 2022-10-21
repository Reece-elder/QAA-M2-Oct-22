# Parent class
class Bird:
    def __init__ (self, feathers, name, wingspan):
        self.feathers = feathers
        self.name = name
        self.wingspan = wingspan

    def layEgg(self):
        return "Laid an Egg!"

bird1 = Bird("Blue", "Birdy mcBirdFace", 30)
print(bird1.layEgg())

# Child class will inherit everything from the parent class
# The object within the () is the parent class of this class
class Penguin(Bird):
    # We still need to tell it to expect bird values, as we need to pass in these values
    def __init__(self, feathers, name, wingspan, swimSpeed):
        # super() is referring to the parent class (Bird)
        # this will return a bird with these set values, we can then add attributes for Penguin 
        super().__init__(feathers, name, wingspan)
        self.swimSpeed = swimSpeed

    # Overriding is when we are updating what a function does from a child object
    def layEgg(self):
        return None

penguin1 = Penguin("White and Black", "Pingu", 17, 30)
print(penguin1.feathers)
print(penguin1.layEgg())

class Ostrich(Bird):

    def __init__(self, feathers, name, wingspan, runSpeed):
        super().__init__(feathers, name, wingspan)
        self.runSpeed = runSpeed

ostrich1 = Ostrich("Grey", "Olly", 142, 62)

# Exercise Using your existing animal class, either create a parent class 
# for it or create a child class from it. You should in the end have 2 child classes to one object 
# Each child class should add atleast 1 attribute and 1 unique function 

# Stretch - Have a Child parent structure where each child of the parent has 
# 2 sub children below Parent > Child > Sub Child

class RockHopper(Penguin):
    def __init__ (self, feathers, name, wingspan, swimSpeed, funnyHair):
        super().__init__(feathers, name, wingspan, swimSpeed)
        self.funnyHair = funnyHair
    
    def layEgg(self):
        return f"{self.name} laid an egg!"

        

rockHop1 = RockHopper("Blue", "Rocky", 12, 42, True)
rockHop1.setFeathers("Purple")