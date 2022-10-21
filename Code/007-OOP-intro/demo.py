# Objects are 'physical' collections of data, both as variable values and functions and can be created to simplify workflow
# When creating an object, you create it out of a 'Class' 

# this is a data type of class, the name of the class is Uppercase

class Cake:
    colour = "Brown"
    flavour = "Choc"
    candles = 7
    vegan = False

    # When creating functions within a class, we need to specify what object is running the function
    # We pass in the word 'self' into the params, when the function runs it runs as an object 
    def bake(self):
        print("In the oven now!")

# Cake() is our class constructor and returns an object of type Cake
# choc_cake is equal to what Cake() returns
choc_cake = Cake()
print(choc_cake.colour)
choc_cake.colour = "Red" # Modifying the attribute
print(choc_cake.colour)
print(choc_cake)

# Print out gibberish - 161812627@Cake
# Print out memory location Cake@<reference to memory location>

class CakeConstructor: 
    # String flavour = "" - No need to declare variables BEFORE your constructor
    color = "" # Declared our cake will have a value for 'Color'
    recipe_version = "v1.2"
    # Function called __init__ takes in self and all attributes wanted
    def __init__(self, colour, flavour, candles, vegan):
        # When the function runs, the colour of THIS OBJECT is equal to the colour we pass in
        self.colour = colour
        self.flavour = flavour
        self.candles = candles
        self.vegan = vegan

    def bake(self):
        print("In the oven now!")

# Creating an object by passing in our values
blackForest = CakeConstructor("Black", "Cherry", 5, True)

print(blackForest.flavour)

# Exercise - Plan and create a class for an animal of your choice, 
# it must contain atleast 4 variables and one function (with a simple print statement)
# Create 3x objects of this class with different values, print some values and run the object print function  

# Stretch goal - Implement some way of looping through all of your objects and printing one of their values out