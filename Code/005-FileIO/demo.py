# When working with FileIO it is easier to work from command line rather than the play button 
# `python demo.py` <- in my terminal 

# Telling python to 'open' our file, we pass in to open("Path/to/file.md")
file = open("fruit.txt")
# Creating a var 'line' that is equal to the firstline of our file 
line = file.readline() # By adding a num you are limiting the chars of that line
print(line)
# Close your file to save memory
# file.close()
# line2 = file.readline()

# Reads ALL the data from the file and stores it as a variable
# An Array containing strings separated by new lines 
data = file.readlines()
# print(data)
# print(data[2])

# Modulus (%) Divides x by y and returns the leftover 
# 7 % 3 = 1
# 7 / 3 = 2 (remainder 1)

# count = 0
# for fruit in data:
#     if count % 2 == 1: # is count odd?
#         print(fruit.strip()) #.strip() removes whitespace and newline chars (/n)
#     count += 1 # Increment count by 1

# 1. List of a List
# 2. comma separated string
# 3. As its laid out in fruit.txt

# Exercise - Create a list of 7 colours as a .txt file,
# use python to read the file and print the 1st, 3rd, 5th and 7th colours to the console 


# line_numbers = [1, 3, 5, 7]
#     # To store lines
# lines = []
# for i, line in enumerate(line):
#     if i in line_numbers:
#             lines.append(line.strip())
#     elif i > 6:
#             # avoid getting out of range
#         break
# print(lines)

file.close()

# By default the command we open a file with is "r" (read), "w" (write), "a" (append), "x" (create)
# With "r" it won't work if the file doesn't exist
# With "w" and "a" (and "x") it works if the file doesn't exist
colourFile = open("colours.txt", "w")

newColour = "Red\n"
colourFile.write(newColour)

colourFile.close()

colourFile = open("colours.txt", "a")

newerColour = "Purple\n"
colourFile.write(newerColour)

print(data)
for fruit in data:
    newLine = f"New fruit added: {fruit}"
    colourFile.write(newLine)

# Easy to forget to close your files
colourFile.close()

# with command - Opens a specific file, and runs nested commands within the file
with open("fruit.txt", "r") as file:
    for line in file:
        print(line)

# Exercise - File IO Lab