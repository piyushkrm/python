'''Write a python function to print multiplication table of a given number.'''
def table(n) :
    for i in range(1, 11):
        print(f"{n} * {i} : {n * i}")

t = int(input("Enter the number for printing table : "))
table(t)