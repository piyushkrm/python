'''Question 2 : Write a python program using function to convert Celsius to Fahrenheit.'''
def celsisToFahrenheit():
    while True:
        try:
            cal = int(input("Enter celsius : "))
            return (cal * 9/5) + 32
    
        except ValueError:
            print("Invalid celsius")

print(f"Convert Celsius to Fahrenheit is : {celsisToFahrenheit()} Fahrenheit")