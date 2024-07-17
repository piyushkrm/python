'''Write a program to find the sum of first n natural numbers using while loop.'''

num = int(input("Enter number for print the sum : "))
i = 1
sum = 0
while i <= num:
    sum += i
    i+=1
print(f"Sum of first n natural numbers is {sum}")