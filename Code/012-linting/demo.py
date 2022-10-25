# Linting -Is the process of checking and validating code follows best practice
# Testing is to check does the code WORK
# Linting is checking does the code work WELL / Readable
# Linting a file is to check it for best practice and is easily maintainable

# `pip install pylint`
# `pylint <name of file>`

# Bad Code
# coolvariablenamethatistoolong="this is a really "
# def printtext(x):
#    return f"text is {x}"
# print(printtext("Hello",))

# Good Code

""" At the top of our file we should add a module docstring to explain the purpose of the file """

# Global variable, should be UPPER_CASE
STRING_VAR = "Sensible variable"

def print_text(text_string):
    """ Each function should have a docstring explaining what it does """
    return f"text is {text_string}"

print(print_text("hello"))
