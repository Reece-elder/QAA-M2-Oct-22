# Python is a high level dynamically typed programming language
# This is a comment, non executable, instructions, explanation etc.

# print is a function that takes in some data (text) and 'prints' it to the console
# We can run our code by typing 'python <name of file>' in our terminal
print('Hello World')

# Python works as a scripting language, reading top to bottom of the file you are on
print("z")
print("apple")
print(1)

# dynamically typed data - You don't need to specify the type of data, the interpreter will assume it for you

# Python Data Types
# int, strings, booleans, var, float, array, char (single character), set, list, tuple, dictionary,
# Number
tiers = 2 # ints are whole numbers
price = 12.99 # floats are decimal (floating point values)

# String (text)
tiers = "four" # Text
rating = 'a'   # Char, single character

# Boolean
decorated = True # Python booleans are Uppercase True or False

# Array (Collection of data types)
cakeFlavours = ["Mango", "Kiwi", "Vanilla"]

# Variable is a placeholder for data 
print("============================================")
print(price)
price = 10.55
print(price)

# Exercise - Create variables for the following data types: string, int, float, boolean, array 
# Use a print function to print the content of those variables 
# Stretch goal - Experiment with formatting your print statement to make it interesting 'print("price: " + price)'

print(cakeFlavours)   # Print out the content of the array not just the ID reference
print(cakeFlavours[1]) # Within arrays you can grab a specific value by its index, index starts at 0 and goes up by 1 


# Inputs allow us to enter values and save them as variables
fav_colour = input(">>>> Please enter your fav colour: ") # Adds some input text value to the terminal to let you enter text
print("My favourite colour is " + fav_colour)

# What type of data is fav_number? - inputs are ALWAYS strings
# We can cast our data to a number (convert from a string to an int)
fav_number = input("Please enter your fav number: ")
print("My fav number is " + fav_number)
better_num = int(fav_number) + 1 # Add 1 to an int

other_num = int(input("Please enter number"))

total = 9 + 7
print("Sum is " + str(total)) # Casting from int to string
print("*****************************************")
print(other_num)

# Exercise - Use input statements to mock a customer details app, taking in name, age, existing customer and print these details back to the user
# Stretch goal - Take the customes three favourite fruits and save as an array