# Testing - Checking your code does what you expect it to do
# Testing works on checking an outcome compared to an expected outcome

# 2 + 2 = 4 <-- something we know as logic, that 2 plus two is equal to 4 

def twoSum():
    x = 2
    y = 2
    return f"{x} + {y} = {x + y}"

# We need to create a test to check if this is true, if twoSum() returns the correct sum

# Functional - Testing of the code logic itself (Your primary domain of testing)
    # Unit Testing - Testing the individual 'units' of a codebase. 
      # Units are the smallest compound resource in code - functions / methods of your code
      # You test functions completely separate from other functions, A -> B -> C -> D

    # Integration Testing - Testing how the functions can work together and what is the expected outcome after many functions 

# Testing is an automatic process, just by reading and checking you are not 'testing' (Sanity Testing)
# Tests have to be written in code, and all tests run together automatically to check the codebase  

# Non Functional Testing - The implementation of the code, human nature

# For python we will be using 'pytest' - Pytest is a package with testing functions inbuilt
# `pip install pytest`  / `python pip install pytest`

print(twoSum())