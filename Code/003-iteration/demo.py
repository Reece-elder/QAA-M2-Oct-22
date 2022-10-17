# Iteration - looping and repeating code, so as to limit the code and request we write
# Print all numbers from 1 - 10 not too bad, but if your code wanted to print 1 - 10,000 
# DRY - Don't Repeat Yourself 

# While - Command that repeats functions until a condition is met
time_left = 10
while time_left > 0:
    print(f"There is still {time_left} seconds left! ")
    time_left -= 1 # decrementing the variable by 1

print("Time over!")

# Write a command that counts from 0 - 505 in increments of 6
count = 0
while count < 505:
    print(f"Current value of count: {count}")
    count += 6

colour = "red"
while colour == "red":
    print(f"Current colour: {colour}")
    colour = "blue"

# For loops - Do a function for each element in a list 
# range() - function that generates a list of numbers based on input

print(range(5)) # Generates a list of nums from 0 - 4
print(*range(5)) # Generates a list of nums from 0 - 4
print(*range(2,9)) # List from 2 - 8
print(*range(10, 0, -2)) # List starting from 10 going to 0, subtracting 2 

# Print the word Hello 10 times 
for x in range(10):
    print(f"Hello! Value of x: {x}")

for x in range(192, -43, -7):
    print(f"Hello! Value of x: {x}")

    # while in a loop you may need to exit the loop in certain conditions
    # This can be done with the break command
    if x == 59:
        print("X is 59, loop broken!")
        break # this stops the loop and the control flow passes on

print("Happens after break")