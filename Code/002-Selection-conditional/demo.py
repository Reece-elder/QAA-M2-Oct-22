# Conditionals are ways of forcing the code to do different things when different situations occur
# If x is y.. do this thing.. else do this thing 

button_pressed = False

# Conditional statement, with 'if' being our command word
# = assigns a value, == checking a value 
if button_pressed == True:
    print("button is pressed!")
else: 
    print("button is not pressed :( ")

# else if 
chosen_num = int(input("Please enter a number to guess: ")) # A guessing game to tell you if you inputted the target_num

target_num = 12
# Less than 
# Greater than 
# Equal to 

# < = less than, > greater than
if chosen_num < target_num: 
    print("chosen number is less than target number")
elif chosen_num > target_num: 
    print("Number is greater than target number")
else:
    print("chosen num is equal to target num")

# <= less than or equal to, >= greater than or equal to

if chosen_num <= target_num:
    print("Chosen num is either less than OR equal to")
    if chosen_num < target_num:
        print("Chosen num is less than target num")
    else:
        print("chosen num is equal to target num ")
else: 
    print("Must be greater than")

# Within python you can use the following:
# AND both conditions must be true
# OR either conditions must be true

shape = "hexagon"
solid = True

if shape == "square" and solid == True:
    print("Shape is square and solid")
elif shape == "triangle" and solid == True:
    print("Solid triangle")
elif shape == "hexagon" or solid: # Is solid == True
    print("Shape is hexagon and isn't solid")
    print("Shape is solid and isn't hexagon")
    print("Shape is solid AND hexagon")
elif shape != "circle":
    print("Shape is not a circle")
elif not solid:
    print("Shape is not solid") 


