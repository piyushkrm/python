# """Question 1 : Write a program to find the greatest of four numbers entered by the user."""
# print("Enter the numbers")
# listt = []
# for i in range(4):
#     num = int(input("Enter the number : "))
#     listt.append(num)

# listt.sort()
# print(listt[len(listt)-1])


# Other methods
# a = int(input("Enter the number 1 : "))
# b = int(input("Enter the number 2 : "))
# c = int(input("Enter the number 3 : "))
# d = int(input("Enter the number 4 : "))

# if(a > b and a > c and a > d):
#     print(a, "Is greatest of all")
# elif(b > a and b > c and b > d):
#     print(b, "Is greatest of all")
# elif(c > a and c > b and c > d):
#     print(c, "Is greatest of all")
# else:
#     print(d, "Is greatest of all")


# Another method
e = int(input("Enter the number 1 : "))
f = int(input("Enter the number 2 : "))
g = int(input("Enter the number 3 : "))
h = int(input("Enter the number 4 : "))
getMax = max(e, f, g, h)
print(getMax)