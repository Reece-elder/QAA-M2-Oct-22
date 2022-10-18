# Arrays
# Array is a collection of like data, that has some association to each other

# Lists - [], ordered (indexed), mutable, collection of any values 
cafe_order = [12, ["latte", "Carrot Cake"], True, "Harry Hill"]
print(cafe_order[2])
print(cafe_order[1][1]) # Multi dimensional Arrays
cafe_order[0] = 7 # Updating values of array
print(cafe_order)
cafe_order.remove("Harry Hill") # Remove via value
del cafe_order[0] # Remove via index
print("************************************")
print(cafe_order)

# Tuple - (), immutable (cannot be modified), ordered, any data type
fruit_tuple = ("orange", "pineapple", "kiwi", True)
print(fruit_tuple)
print(fruit_tuple[2])
# fruit_tuple[2] = "apple" Cannot update tuple values

# Dictionaries - Collection of key value pairs (drink = coffee), unordered, mutable {}
animal_noises = {"cow" : "Moo!", "Duck" : "Quack!"}
print(animal_noises["cow"]) # Grab the value via its key
animal_noises["Duck"] = "Duck quacks don't echo"
animal_noises["Chicken"] = "Cluck!" # Add a value by assigning it a key value pair
print(animal_noises)

animal_noises.pop("Chicken") # pop removes the value of this key
print(animal_noises)

# Sets - Unordered, mutable, collections of unique values. You cannot have duplicate values, {}
fruit_set = {"Orange", "Kiwi", "Grape", "Kiwi", "Banana", "Orange", "Pineapple"}
print(fruit_set)

# Range - A list of numerical values from 0 - max value
# A for loop does something for each element of a list
colours = ["Aqua", "Green", "Purple", "Orange", "Red"]
for colour in colours:
    print(colour)