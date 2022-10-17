num1 = int(input("Please enter first num: "))
num2 = int(input("Please enter second num: "))

print("1. Add +")
print("2. Subtract -")
print("3. Multiply *")
print("4. Divide /")
print("5. power p")
sum = input("Enter the sign of the sum you wish to")

if sum == "+":
    total = num1 + num2
    print(total)
elif sum == "-":
    total = num1 - num2
    print(total)
elif sum == "*":
    # Anything between the {} of an fString is a direct variable
    print(f"{num1} * {num2} = {num1 * num2}") # f format String / fString and lets us add variables directly
    print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
elif sum == "/":
    print(f"{num1} {sum} {num2} = {num1 / num2}")
elif sum == "p":
    print(f"{num1 ** num2}")



 
 
