print("*Note are mutable in python..")
marks = [96, 65, 75, 69, 89.8, 46.23]
print(marks)
print(marks[0])
print(len(marks))

student = ["Piyush", 77.08, "Bihar", 7488241964, 20, "piyushkuma045@gmail.com"]
print(student)

student[0] = "Abhinav"
print(student)
print(student[0 : 3])
print(student[0 : ])

# # Methods
# = [20, 50, 89]
# print(
# append(45)
# append(49)
# sort()
# print(
# sort(reverse = True)
# print(
# reverse()
# print(
# insert(0, 55645)
# insert(3, 55645)
# print(

# = [10, 25, 89, 45, 78, 96, 36, 74, 52, 36, 22, 33, 66, 99, 77, 77, 88, 44]
# remove(89)
# pop(14)
# pop(0)
# count(77)
# print(


# TUPLE 
tup = (10, 10, 10, 25, 89, 45, 78, 96, 36, 74, 52, 36, 22, 33, 66, 99, 77, 77, 88, 44)
print(type(tup))
print(tup[10])

emptTuple = (1,)
print(emptTuple)
print(type(emptTuple))

print(tup.index(25))
print(tup.count(10))

# PRACTICE
print("Q.1 WAP to ask the user to enter names of their 3 favorite movies and store them in a ")
print("enter names of their 3 favorite movies---")
movies = []
movie1 = input("Enter first movie name : ")
movie2 = input("Enter first movie name : ")
movie3 = input("Enter first movie name : ")
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)

# # Other method
movies.append(input("Enter First movie name : "))
movies.append(input("Enter Second movie name : "))
movies.append(input("Enter Third movie name : "))
print(movies)

print("Q.2 WAP to check if a list contain a palindrone of elements. (Hind : use copy() method)")
list = [5, 1, 2, 3, 2, 1, 5]
copylist = list.copy()
copylist.reverse()
if(list == copylist):
    print("List is palindrone")
else:
    print("List not is palindrone")


print('Q.3 WAP to count the number of students with the "A" grade in the following tuple. \n["C", "D", "A", "A", "B", "B", "A"]')
grade = ["C", "D", "A", "A", "B", "B", "A"]
print(grade.count("A"))

print('Q.4 Store the above values in a list and sort them from "A" to  "D"')
list = ["C", "D", "A", "A", "B", "B", "A"]
list.sort()
print(list)