'''Write a program to calculate the grade of a student from his marks from the
following scheme:
90-100=> Ex
80-90=> A
70-80=> B
60-70 =>C
50-60=> D
<50 =>F'''

my_marks = int(input("Enter your marks : "))
if my_marks > 100:
    print("Invalid marks")
elif my_marks >= 90:
    print("Excellent")
elif my_marks >= 80:
    print("A grade")
elif my_marks >= 70:
    print("B grade")
elif my_marks >= 60:
    print("C grade")
elif my_marks >= 50:
    print("D grade")
else:
    print("Fail. Better Luck Next Time")