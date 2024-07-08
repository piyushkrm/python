print ("Hello World!")
print("Codewithpihu")

print("My name is piyush Mishra")
print("My age is 20")

print("My name is piyush Mishra", "My age is 20")
print(20+56)

name = "Piyush Mishra"
age = 20
print(name, + age)
print("My name is : ",name, "My age is : ",age )
print("My age is : ",age )

print(type(name))
print(type(age))

# # STRING
print('Piyush')
print("Piyush")
print('''Piyush''')

# # Boolean and None
old = True
no = None
print(type(old))
print(type(no))

# # CALCULATION
a = 5
b = 7
sum = a + b
print(sum)
print(type(sum))

# CONVERSION 
# Type Conversion ---> Automatically conversion by compiler
a = 15
b = 63.3
print(type(a))
print(type(b))
print(type(a+b))

# Type casting ---> Manually by user
x = "45"
y = 18
c = int(x)
print(c + y)
print(type(c))


# INPUT 
name = input("Enter Your name :")
age = int(input("Enter Your Age : "))
marks = float(input("Enter Your marks : "))

print("Hey",name, "Good Evening")
print("Your age is :", age)
print("Your age is :", marks)
print(type(name))
print(type(age))
print(type(marks))




# LETS PRACTICE
# QUESTION 1
print("Write a Program to input 2 numbers & print their sum")
num1 = int(input("Enter First Number for sum : "))
num2 = int(input("Enter Secong Number for sum: "))
sum = num1 + num2
print("Sum of Number is : ",sum)


# QUESTION 2
print("Write a program to input side of a square and print its area")
area = float(input("Enter side of a square : "))
area *= area
print("Area pf the square is : ", area)


# QUESTION 3
print("Write a program to 2 floating point numbers and print their average")
numb1 = float(input("Enter first float number for calculate average : "))
numb2 = float(input("Enter second float number for calculate average : "))
average = (numb1 + numb2) / 2
print("Average of above defined number is : ",average)


# QUESTION 3
print("Write a program to input 2 int numbers, a and b. \nPrint True if a is greater than or equal to b. If not print False")
one = int(input("Enter first number : "))
two = int(input("Enter second number : "))

gt = one >= two
print(gt)
