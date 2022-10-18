# Get a salary from the user
def getSalary():
    salary = int(input("Please enter salary: "))
    return salary

# Simple Salary way
def getIncomeTax(getSalary):
    tax = 0

    if getSalary < 11850:
        return f"Starting salary is {getSalary} which is within allowance, no tax is paid"
    elif getSalary < 34500:
        tax = 20
    elif getSalary < 150000:
        tax = 40
    else:
        tax = 45

    taxableSalary = getSalary - (getSalary * (tax / 100))
    return taxableSalary

# Complex Salary way
def getComplexTax(getSalary):
    # Staggering the tax, so you only pay x amount of tax per bracket
    # 0 - 11850 not taxed, 11851 - 34500 20%, 34501 - 150000 40%, over is 45%

    smallTax = 0
    medTax = 0
    largeTax = 0

    if getSalary <= 11850:
        return f"Starting salary is {getSalary} which is within allowance, no tax is paid"
    
    if getSalary > 11850:
        # We're subtracting the allowance and taxing the rest
        smallTax = (getSalary - 11850) * 0.2

    if getSalary > 34550:
        # We're subtracting the allowance and taxing the rest
        medTax = (getSalary - 34500) * 0.4

    if getSalary > 150000:
        # We're subtracting the allowance and taxing the rest
        largeTax = (getSalary - 150000) * 0.45

    finalTax = smallTax + medTax + largeTax
    return getSalary - finalTax

print(getIncomeTax(52000))
print(getComplexTax(52000))