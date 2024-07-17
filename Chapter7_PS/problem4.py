'''Write a program to find whether a given number is prime or not.  '''
enter_number = int(input("Enter the number to check which is prime or not : "))
if enter_number > 1:
    for i in range(2, enter_number):
        if (enter_number % i) == 0:
            print(f"{enter_number} is not a prime number")
            break
    else: 
        print(f"{enter_number} is a prime number")
else:
    print(f"{enter_number} is not a prime number")