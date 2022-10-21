# Polymorphism means many forms
# An object within Python belongs to multiple different types of Object

class Animal: 
    def animal_noise(self):
        print("Animal Noise!")

class Farm_animal(Animal):
    def farm_noise(self):
        print("Farm animal noise!")

class Cow(Farm_animal):
    def cow_noise(self):
        print("Mooooo")

animal = Animal()
farm = Farm_animal()
cow = Cow()

animal.animal_noise()
farm.animal_noise()
cow.animal_noise()