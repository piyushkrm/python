'''Attempt problem 1 using while loop.'''
num = int(input("Enter table which you want to print : "))
i = 1
while(i < 11):
    print(f"{num} * {i} : {num * i}")
    i+=1