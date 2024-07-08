# READ MODE (DEFAULT MODE)
p = open("Lecture 7 Demo.txt", "r")
data = p.read()
data = p.read(10) #READ 10 CHARACTER FROM THE FILE
print(data) 
print(type(data))
p.close()


# READ ONE LINE AT A TIME
s = open("Lecture 7 Demo.txt", "r")
line1 = s.readline()
line2 = s.readline()
line3 = s.readline()
print(line1)
print(line2)
print(line3)
s.close()



# WRITE MODE
w = open("Lecture 7 Demo.txt", "w")
w.write("This is a overwriting new line.")
w.close()

w = open("Lecture 7 Demo.txt", "a")
w.write("\nI append lines using 'a' character mode")


k = open("sample.txt", "w")
k.write("when we dont have file for writing then pyton autimatic create file for me! That's awesome")
w.close()



# COMBINE MODE
# r+
q = open("Lecture 7 Demo.txt", "r+")
q.write("This is overwrite from starting of line")
print(q.read())
q.close()

# w+
t = open("Lecture 7 Demo.txt", "w+")
t.write("This is overwrite from starting of line")
print(t.read())
t.close()

# a+
a = open("Lecture 7 Demo.txt", "w+")
a.write("This is overwrite from starting of line")
print(a.read())
a.close()



# with SYNTAX
with open("Lecture 7 Demo.txt", "r") as p:
    data = p.read()
    print(data)

with open("Lecture 7 Demo.txt", "w") as s:
    s.write("My data")


# DELETE A FILE 
import os
os.remove("Demo delete.txt")




# LET'S PRACTICE
print("Q.1 Create a new file 'practice.txt' using python. Add the following data in it: Hi everyone\nwe are learning File I/O\nusing Python\nI like programming in Python")
with open("practice.txt", "w") as practice:
    practice.write("Hi everyone\nwe are learning File I/O\nusing Java\nI like programming in Java")


k = open("practice1.txt", "w")
k.write("Hi everyone\nwe are learning File I/O\nusing Java\nI like programming in Java")
print(k.read())

print("Q.2 WAF that replace all occurences of 'java' with 'python' in above file")
with open("Lecture 7 practice.txt", "r") as f:
    data = f.read()
    # print(data)
new_data = data.replace("Java", "python")
# print(new_data)

with open("Lecture 7 practice.txt", "w") as f:
    f.write(new_data)


print("Q.3 Search if the word 'learning' exists in the file or not")

def word_finding(str):
    with open("Lecture 7 practice.txt", "r") as p:
        search = p.read()
    if(search.find(str) != -1):
        print("Found")
    else:
        print("Not Found")

word_finding("learning")


print("Q.4 WAF to find in which line of the file does the word 'learning' occur first. (Print -1 if word not found)")
def check_line(word):
    data = True
    line_number = 1
    with open("Lecture 7 practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_number)
                return
            line_number += 1
    return -1

print(check_line("python"))

print("Q.4 From a file containing numbers separated by comma, print the count of even numbers.")
with open("Lecture 7 number.txt", "r") as eo:
    data = eo.read()
    # print(data)
    num = ""
    odd = 0
    even = 0
    for i in range(len(data)):
        if(data[i] == ","):
            no = int(num)
            if(no % 2 == 0):
                even += 1
            else:
                odd += 1
            print(no, end=" ")
            num = ""
        else:
            num += data[i]
print("\nCount of Even Number is = ",even)
print("Count of Odd Number is = ",odd)

# ANOTHER METHOD 
even = 0
odd = 0
with open("Lecture 7 number.txt", "r") as eo:
    data = eo.read()
    num = data.split(",")
    for val in num:
        if(int(val) % 2 == 0):
            even += 1
        else:
            odd += 1
print("Odd is ",odd)
print("Even is ",even)