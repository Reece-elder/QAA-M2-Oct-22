def vowels(word):
    number_of_vowels = 0
    the_vowels = ["a", "e", "i", "o", "u"]
    for letter in word.lower():
        if letter in the_vowels:
            number_of_vowels += 1
    return number_of_vowels

print(vowels("apple"))

def test_vowels():
    # Arrange
    test_word = "aeiouABCDE" # Should be 7
    result = 0
    # Act
    result = vowels(test_word)
    # Assert
    assert result == 7