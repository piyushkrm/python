# Recursion
# Factorial with recursion
def recursion(fact):
    if fact == 1 or fact == 0:
        return 1
    return recursion(fact - 1)*fact

facto = int(input("Enter number for calculate their factorial : "))
print(f"Factorial of {facto} is {recursion(facto)}")