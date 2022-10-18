# Functions are repeatable command blocks that you can trigger with their name
print("Text") # Triggering the print function and passing in our parameter 

# def is used to define a function
def greeting():
    print("Hello!")

print("HERE!")

# Trigger our function (or call it) w/ <name of function>()
# greeting()

# When you call addSum() you must pass in two params
def addSum(x, y):
    # takes in two numbers and adds them together
    # Wherever x or y is written in the code, replace them with the params
    total = x + y
    # return -> Takes the data from our function and output it
    return total

# addSum() returns the sum of the two nums, to see this we need to print the calling
print(addSum(5,7))

# Most functions should return something, whether its useful data or feedback that the function was triggered
# When testing code, we check what the return is

def returnColour():
    text = "Purple"
    return text # As soon as you return from a function, the function exits
    # print("Function has returned..")

# We're expecting the user to pass in some text
def returnName(name):
    text = f"Hello {name}"
    return text


# Callback - When we pass in a function as a parameter to another function 
# The callback is the function we're passing in

# We expect it to take in a text
def nameFunc(name):
    return f"Hello {name}"

# We expect it to take in a function
def greetFunc(func):
    return f"{func}, how are you?"

print(nameFunc("Ian"))
print(greetFunc(nameFunc("Jonas")))
# new_list.sort().map().someFunc()

# Scope  - Accessibility of variables within files
# Global - Accessible anywhere within the program
# Local  - Accessible only within where it is defined (function)

# Global, created directly in my file
colour = "Purple"
print(colour)

def textFunc():
    print(f"{colour} within a func!")
    localVar = 123
    print(localVar)

textFunc()
print(localVar)