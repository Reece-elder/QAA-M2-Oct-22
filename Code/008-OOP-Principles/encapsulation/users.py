class User:

    def __init__(self, name, existing_customer, age):
        self.name = name
        self.existing_customer = existing_customer
        self.age = age

    # Name being passed in is what we wish to update it with 
    def setName(self, name):
        # We are not validating whether this is a string or not
        if type(name) is str: # Returns true if is a string, else returns false
            self.name = name
        else:
            print("Name entered is not valid")

user1 = User("Tony", True, 28)
user1.setName("Toni")