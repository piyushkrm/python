'''Write a program to calculate the factorial of a given number using for loop.'''
number = int(input("Enter the number for calculate the factorial of a number  : "))
fact = 1
for i in range(1, number+1):
    fact *= i
print(f"Factorial of {number} is : {fact}")