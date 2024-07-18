'''Write a python function which converts inches to cms.'''

def convert(inches):
    return inches * 2.54

inches = int(input("Enter inches : "))
print(f"{inches} inches = {convert(inches)} ")