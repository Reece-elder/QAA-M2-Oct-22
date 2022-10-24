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
print(data)
print(data[2])

# 1. List of a List
# 2. comma separated string
# 3. As its laid out in fruit.txt

# Exercise - Create a list of 7 colours as a .txt file,
# use python to read the file and print the 1st, 3rd, 5th and 7th colours to the console 