count = 1
while count <= 50 :
    print('Hello Piyush!', count)
    count += 1

# PRACTICE QUESTION
print("Q.1 Print number from 1 to 100")
num = 1
while num <=100:
    print(num)
    num += 1

print("Q.2 Print number from 100 to 1")
numb = 100
while numb >=1:
    print(numb)
    numb -= 1


print("Q.3 Print the multiplication table of a number n")
mul = int(input("Enter number for print table : "))
ind = 1
while ind <= 10:
    tab = mul * ind
    print(mul , "*", ind, "=", tab)
    ind += 1


print("Q.4 Print the elements of the following list using a loop : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]")
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 150, 200]
index = 0
# while index <= len(list) - 1:
while index < len(list):
    print(list[index])
    index += 1

cricketer = ["Virat Kohli", "Rohit Sharma", "Shubham", "Shreyash", "Rahul", "Rishav", "Hardik", "Jadeja", "Yuzi", "Bumrah", "Siraj", "Shami"]
inde = 0
while inde < len(cricketer):
    print(cricketer[inde])
    inde += 1


print("Q.5 Search for a number x in this tuple using loop : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]")
serch = int(input("Enter number for searching : "))
number = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 100)
INDEX = 0
while INDEX < len(number):
    if(number[INDEX] == serch):
        print("Found number at index of : ", INDEX+1)
    INDEX += 1

# BREAK STATEMENT
i = 1
while i <= 5:
    print(i)
    i += 1
    if( i == 4):
        break


# CONTINUE STATEMENT
i = 1
while i <= 10:
    if( i == 4):
        i += 2
        continue
    print(i)
    i += 1


# PRINT ODD EVEN NUMBER USING WHILE AND CONTINUE STATEMENT
i = 1
while i <= 100:
    if(i % 2 != 0):  #EVEN NUMBER
    # if(i % 2 == 0):  #ODD NUMBER
        i += 1
        continue
    print(i)
    i+=1

# FOR LOOP
list = ["Virat Kohli", "Rohit Sharma", "Shubham", "Shreyash", "Rahul", "Rishav", "Hardik", "Jadeja", "Yuzi", "Bumrah", "Siraj", "Shami"]
for el in list:
    print(el)


# LOOP LOOP WITH ELSE 
vegitable = ("Cucumber", "Carrot", "Onion", "Patato", "Tomato")
for el in vegitable:
    print(el)
else:
    print("End of Vegitable list")


str = "Piyush Kumar Mishra"
for char in str:
    if(char == "i"):
        continue
        # print(char)
    else:
        print(char)


# PRACTICE
print("Q.1 Print the elements of the following list using a loop : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]")
elements = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for element in elements:
    print(element)

print("Q.2 Search for a number x in this tuple using loop : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]")
x = int(input("this is leniear search(single line search)  \nEnter number for searching element in tuple : "))
tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0
for tup in tuple:
    if(tup == x):
        print("found", tup, "at index", i)
        break
    i += 1


# RANGE FUNCTION
for el in range(16):
    print(el)

for ele in range(5, 15):
    print(ele)

for elem in range(1, 50, 2):
    print(elem)


# PRACTICE
print("Q.1 Print numbers from 1 to 100.")
for numb in range(1, 101):
    print(numb)

print("Q.2 Print numbers from 100 to 1.")
for number in range(100, 0, -1):
    print(number)

print("Q.3 Print the multiplication table of a number.")
x = int(input("Enter number for print table : "))
for table in range(x, x*11, x):
    print(table)

print("Q.4 WAP to find the sum of first n numbers. (Using while)")
sum = 0
indx = 1
n = int(input("Enter number for sum of those number : "))
while indx <= n:
    sum = sum + indx
    indx += 1
print("sum of your entered number is :", sum)

print("Q.5 WAP to find the sum of first n numbers. (Using for)")
n = int(input("Enter number for sum of those number : "))
sum = 0
for i in range(1, n+1):
    sum += i
print("sum of your entered number is :",sum)

print("Q.6 WAP to find the factorial of first n number (using while)")
n = int(input("Enter number for calculating the factorial : "))
fact = 1
i = 1
while i <= n:
    fact *= i
    print("Factorial of a number is : ", n ,"*", i, "=", fact)
    i += 1
print("Factorial of a number is : ",fact)



print("Q.7 WAP to find the factorial of first n number (using for)")
n = int(input("Enter number for calculating the factorial : "))
fact = 1
for facto in range(1, n+1):
    fact *= facto
    print("Factorial of a number is : ", n ,"*", facto, "=", fact)
print("Factorial of a number is : ",fact)



# PASS STATEMENT
for pas in range(15):
    pass
print("pass statement")


