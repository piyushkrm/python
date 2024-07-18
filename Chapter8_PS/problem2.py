'''Question 2 : Write a python program using function to convert Celsius to Fahrenheit.'''
# Convert Fahrenheit to Celsius
def fahrenheitToCelsis():
    while True:
        try:
            f = int(input("Enter Fahrenheit : "))
            return 5*(f - 32) / 9
    
        except ValueError:
            print("Invalid Fahrenheit")

print(f"Convert Fahrenheit to Celsius is : {fahrenheitToCelsis()}°C")


#  Convert Celsius to Fahrenheit
def celsisToFahrenheit():
    while True:
        try:
            cal = int(input("Enter celsius : "))
            return (cal * 9/5) + 32
    
        except ValueError:
            print("Invalid celsius")

print(f"Convert Celsius to Fahrenheit is : {celsisToFahrenheit()} Fahrenheit")