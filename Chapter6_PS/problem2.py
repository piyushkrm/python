"""Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user."""


passorfail = {}
total_marks = 0
for i in range(2):
    name = input("Enter subject name : ")
    marks = int(input("Enter marks of obtained in subject : "))
    passorfail.update({name : marks})
    total_marks += marks

if total_marks >= 40 and all(marks >= 33 for marks in passorfail.values()):
    print("Passed")
else:
    print("Fail")


# Another approach

sub = input("Enter Subject 1 Name : ")
score = int(input("Enter your marks : "))
sub1 = input("Enter Subject 2 Name : ")
score1 = int(input("Enter your marks : "))
sub2 = input("Enter Subject 3 Name : ")
score2 = int(input("Enter your marks : "))
if(score >= 40):
    print("You are passed in the subject ",sub)
elif(score <= 33):
    print("You are fail in the subject ",sub)

if(score1 >= 40):
    print("You are passed in the subject ",sub1)
elif(score1 <= 33):
    print("You are fail in the subject ",sub1)

if(score2 >= 40):
    print("You are passed in the subject ",sub2)
elif(score2 <= 33):
    print("You are fail in the subject ",sub2)


# Another approach
subjectName = []
obtainedScore = []

for i in range(3):
    sn = input("Enter the Subject name : ")
    subjectName.append(sn)
    sc = int(input("Enter obtained score : "))
    obtainedScore.append(sc)

for i in range(3):
    if obtainedScore[i] >= 40:
        print("You are passed in the subject",subjectName[i])
    elif obtainedScore[i] <= 33:
        print("You are failed in the subject ",subjectName[i])



#modified functions

subjectName = []
obtainedScore = []
for i in range(3):
    sn = input("Enter the Subject name : ")
    subjectName.append(sn)
    sc = int(input("Enter obtained score : "))
    obtainedScore.append(sc)
for sub, scoree in zip(subjectName, obtainedScore):
    if scoree >= 40:
        print("You are passed in the subject of ",sub)
    elif scoree <= 33:
        print("You are failed in the subject of ",sub)
