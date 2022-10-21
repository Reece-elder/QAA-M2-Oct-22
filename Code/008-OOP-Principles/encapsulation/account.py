# Encapsulation - The process of compiling and storing all necessary info about an object in one location
# As well as ensuring you are limiting the read and write access to confidential data 

# When we don't specify a class' parent, its parent is the Python Super Object 
class BankAccount:

    # When assigning variables in Python a _leading underscore suggests this SHOULD be PRIVATE
    _pin = "1234" 
    _money = 100 

    # Our Bank Account object does not require any values to be passed in, 
    # therefore we don't need to create a constructor 

    # Encapsulation - Restricting Read write access
    # Getter - Gets the data and returns it
    def displayMoney(self, pin):
        # No difference between this and just accessing the _money directly
        if pin == self._pin: # our if statement is validating the user 
            return self._money

    def updateBalance(self, pin, money):
        if pin == self._pin:
            self._money = money

account1 = BankAccount()

print(account1._pin)

# Ensure we are never accessing the variable directly, but instead use 'Getters and Setters'
account1.updateBalance("1234", 7494719)
print(account1.displayMoney("1234"))

# Exercise - On your current class, add getters and setters for 3 of your attributes
# Add if statements to validate the data coming in (Age > 0, ensure food isn't broccoli, validate the data type)