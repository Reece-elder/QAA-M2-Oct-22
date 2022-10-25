# This is a test python file connected to our calculator (only by name)
# Users will not be using this file

from calculator import *

def test_addSum():
    x = 5
    y = 7
    result = 0

    result = addSum(x, y)

    assert result == 12

# Exercise 
# Look at previous exercises (loops, conditionals etc) and convert them to functions if need be 
# Write tests for those functions you have created 