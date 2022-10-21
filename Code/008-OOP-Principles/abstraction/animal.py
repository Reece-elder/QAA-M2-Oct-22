# Abstraction - The process of making templates or plans of our classes, that cannot be created DIRECTLY
# But can be used to create child classes which can be made

# Animal  - Not able to create a generic 'Animal' 
# Bird    - Able to create a Bird 
# Penguin - Able to create a Penguin


from abc import ABC, abstractmethod

# Abstract classes don't use default Parents, they use ABC (Abstract Base Class) as a parent
class Animal(ABC): 

    # Abstract methods - Functions with no return, but are guides as to what child classes should contain
    @abstractmethod # Annotation - something to describe a function 
    def eat(self):
        pass # This function doesn't do anything, but all children of this have to use it

# Interfaces - You can inherit as many interfaces as you want, 
# interfaces only contain 1 / 2 abstract methods


class Lizard(Animal):
    def __init__(self, scales, diet):
        self.scales = scales
        self.diet = diet
    
    # Overriding our abstract function 
    def eat(self):
        print("Glub Glub Glub")

lizzy = Lizard("Blue", "Berries")
fake_animal = Animal()

# Create a function that is in charge of sleeping and takes in 1 param (not self)
# sleep(time)