'''Write a program to print multiplication table of a given number using for loop.'''
table = int(input("Enter number for print these table : "))
for i in range(1, 11):
    print(f"{table} * {i} : {table * i}")