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

    # toString in most other languages - replacing the default string method (Cake@63837191718)
    def __str__(self):
        return f"Colour: {self.colour} Flavour: {self.flavour} Candles: {self.candles} Vegan: {self.vegan}"

# Creating an object by passing in our values
# blackForest and carrotCake ARE NOT ATTRIBUTES (cake1, cake2, cake3)
blackForest = CakeConstructor("Black", "Cherry", 5, True)
carrotCake = CakeConstructor("Beige", "Carrots", 0, False)
spongeCake = CakeConstructor("Yellow", "Vanilla", 10, True)

print(blackForest.flavour)
print(blackForest)
blackForest.bake()

# Exercise - Plan and create a class for an animal of your choice, 
# it must contain atleast 4 variables and one function (with a simple print statement)
# Create 3x objects of this class with different values, print some values and run the object print function  

# Stretch goal - Implement some way of looping through all of your objects and printing one of their values out

cakeList = [blackForest, carrotCake, spongeCake, CakeConstructor("Pink and Yellow", "Bakewell tart flavour", 0, False)]
print(cakeList[3].colour)

print(cakeList[3])

print("*********************************************************88")
# For every element in our list cakeList, call the element cake and do this with it
for cake in cakeList:
    print(cake)


# Modifying and setting our attribute values(These aren't *strictly* getters and setters)
# getattr takes in an object and a string of the attribute you're interested in
print(getattr(carrotCake, 'colour'))
print(carrotCake.colour)

# Allows you to modify the attribute by passing in a value 
chosen_attr = "vegan"
print(getattr(carrotCake, chosen_attr))

# hasattr - checks if this object contains this attribute (returns True or False)
print(hasattr(blackForest, 'calories')) # Used to check if an attribute is there for avoiding exceptions 

# setattr - Takes in object, attribute name and value and sets it. 
# Set an attribute that it doesn't already have
print(setattr(blackForest, 'calories', 12000)) # returns None, because setattr doesn't return anything
print(hasattr(blackForest, 'calories'))

# delattr - Takes in object, attribute name and removes this attribute (not just value)
print(f"Calories: {blackForest.calories}")
delattr(blackForest, 'colour')
print(blackForest.colour)

# Because python doesnt specify type it assumes the user has done it right
# But you should still verify whether it is right 

# Exercise - Implement a custom __str__ function into your class
# Use the get, set, has and del to Add a custom attribute, check they are added, 
# if they are set them to a new value and delete an existing attribute 
