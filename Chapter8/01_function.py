# Function 

'''Quick quiz : Write a program to greet a  user with "Good day" using function'''

def greet() :
    name = input("Enter name : ")
    print(f"Good Day {name}!")

# greet()

# find out average of three number 

def average() :
    num1 = int(input("Enter number one : "))
    num2 = int(input("Enter number two : "))
    num3 = int(input("Enter number three : "))
    avg = (num1 + num2 + num3)/3
    print(f"Average of numbers {num1}, {num2}, {num3}, are {avg}")

average()