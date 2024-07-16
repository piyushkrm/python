# Question 2 Write a program to accept marks of 6 students and display them in a sorted manner.
marks = []
for i in range(6):
    score = input("Enter you marks : ")
    marks.append(score)
marks.sort()
print("Your marks are  : ",marks)