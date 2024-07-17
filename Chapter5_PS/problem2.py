# Question 2 : Write a program to input eight numbers from the user and display all the unique numbers (once).
print("Enter eight number")
unique = set()
for i in range(8):
    a = int(input("Enter number : "))
    unique.add(a)

print("Your unique entered number is : ",unique)
