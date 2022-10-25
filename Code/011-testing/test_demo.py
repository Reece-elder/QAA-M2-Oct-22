def sumFunc(num):
    return num * 2

# Not a test, but is a sanity test / check
print(f"Should equal 8: {sumFunc(4)} ")

# Test functions start with test_<name of the function>
def test_sumFunc():
    # Arrange - Arranging and bringing together our resources we need
    num = 5 # num we are passing in
    result = 0 # result we are expecting

    # Act - Doing the thing we are testing 
    result = sumFunc(num) # result should be 10

    # Assert - Asserting if our act did what we expect
    assert result == 10 # assert is essentially an if, returns true or false if the condition is correct


# Function that either returns true or false depending on the code
# Testing if the function returns True when expected 
# Function returns False when expected 
def boolColour(colour):
    if colour == "red":
        return True
    else: 
        return False

def test_boolColour_true():
    # Arrange
    colour = "red"
    result = None
    # Act
    result = boolColour(colour)
    # Assert
    assert result

def test_boolColour_false():
    # Arrange
    colour = "blue"
    result = None
    # Act
    result = boolColour(colour)
    # Assert
    assert not result

# Testing you NEED to show multiple results so there is a requirement to do it that way
# You do have to run your test suite.. but only once (or every time there is a change)