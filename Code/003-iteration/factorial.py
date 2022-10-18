# Create a function / command that takes in a number and gives us the factorial
# Factorial 5! = 1 * 2 * 3 * 4 * 5 

# While loop method
number = int(input("Please enter an integer: "))
count = 1 # Number of times looped through loop
result = 1 # The final factorial value 

# While loops are used when you don't know how many times the loop will run 
while count <= number:
    # New result is equal to old result * number of times looped
    result = result * count 
    count += 1 

print(f"Factorial of {number} is {result}")

# For loop
result_for = 1

for value in range(1, number + 1):
    result_for = result_for * value

print(f"Factorial of {number} is {result_for}")