'''Write a program to find out the line number where python is present from ques 6.'''

with open("/workspaces/python/Chapter9_PS/7_log.txt") as f:
    lines = f.readlines()

lineNo = 1
for line in lines:
    if  "Python" in line:
        print(f"Yes ! python is present at line no {lineNo}")
        break
    lineNo += 1

else:
    print("No ! python is not present")
