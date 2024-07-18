'''Question 1 : Write a program using functions to find greatest of three numbers.'''

import time


def findMax() :
    print("Please enter three numbers:")
    while True:
        try:
            num1 = int(input("Enter the Number 1 : "))  
            num2 = int(input("Enter the Number 2 : "))
            num3 = int(input("Enter the Number 3 : "))
            return max(num1, num2, num3)
        except ValueError:
            print("Invalid input. Please enter valid number")
            time.sleep(1)
            print("Please try again")

print(f"Greatest in three number is {findMax()}")