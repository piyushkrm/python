'''Question 10 : Write a program to print multiplication table of n using for loops in reversed
order.'''

table_number = int(input("Enter the number : "))
# using while loop 
i = 10
while (i >= 1):
    print(f"{table_number} * {i} : {table_number * i}")
    i-=1


# using for loop 
for i in range(1, 11):
    print(f"{table_number} * {11-i} : {table_number*(11 - i)}")
    print()

#  Using list
ls = []
for i in range(1,11):
    ls.append(table_number*i)
ls.reverse()
print(ls)