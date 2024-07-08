dict = {
    "name" : "piyush",
    "roll" : 87215110,
    "cgpa" : 8.64,
    "gmail" : "piyushkrm03@gmail.com",
    "is adult" : True,
    "tup" : ("piyush", "Bihar", "7488241964", "piyushkuma045@gmail.com"),
    "list" : [7488, 93049, 880392, "Radhey", "Krishna", "Mahakal"],
    18 : "Virat",
    45.0 : "Rohit"
}

print(dict)
print(type(dict))
print(dict["name"])
print(dict["list"])
print(dict["tup"])
print(dict[18])
dict["name"] = "Aditya"
print(dict)
dict["surname"] = "Mishra"
print(dict)

# EMPTY DICTINORY
null_dict = {

}
print(null_dict)
null_dict["Subject"] = "C"
null_dict["mnSubject"] = ("C", "python", "java")
null_dict["intSubject"] = ["C++", "python advance", "javascript"]
print(null_dict)


# NESTED DICTIONARY
student = {
    "name" : "Abinav",
    "age" : 17,
    "Score" : {
        "math" : 95,
        "physics" : 89,
        "English" : 95,
        "Hindi" : 99,
        "chemistry" : 92
    },
    "passingyear" : 2024,
    "division" : "1st Devision"
}
print(student)
print(student["Score"])
print(student["Score"]["math"])


# METHODS
print(student.keys())
# type casting
print(list(student.keys()))
print(tuple(student.keys()))
print(len(student))
print(len(student.keys()))

print(student.values())
print(list(student.values()))
print(tuple(student.values()))

print(student.items())

print(student.get("Score"))
print(student.get("Score12345"))  #no error return
print(student.items("Score12345")) # error return
print(student.get("name"))

student.update({"city" : "Araria"})
print(student)

new_dict = {"state" : "Bihar", "name": "piyushu"}
student.update(new_dict)
print(student)




# SETS
num = {1, 2, 3, 4}
num = {1, 2, 3, 4, 5, 4, 3, 2, 1, "set is immutable"}
print(num)
print(len(num)) #duplicate values are ignored
print(type(num))


null_set = {} #dictionary
print(type(null_set
))

null_set = set() #empty set
print(type(null_set))

null_set.add(5)
null_set.add(15)
null_set.add(25)
# null_set.add(["piyush", "kumar"])
null_set.add(95)
# null_set.add({23, "pihu", "sona"})
null_set.add(2.0)
null_set.add("piyush")
null_set.add("mishra")
null_set.remove(25)
print(null_set)
null_set.remove(15)
print(null_set)
null_set.pop()
print(null_set)
null_set.pop()
print(null_set)
null_set.clear()
print(null_set)


set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, "piyush"}
set2 = {11, 12, 13, 14, 15, 16, 17, 18, 19, "mishra"}
set = set1.union(set2)
# print(set)

set01 = {1, 2, 3, 4, 5, 6, 7, 8, 9, "piyush"}
set02 = {1, 3, 91, 4, 5, 6, 7, 8, 9, "aditya"}
interset = set01.intersection(set02)
print(interset)


# PRACTICE
print("Q.1 Store following words meaning in apython dictionary : table :'a piece of furtuner', 'list of facts', 'figures' cat : 'a small animal'")
tab = {
    "table" : ('a piece of furtuner', 'list of facts', 'figures'),
    "cat" : "a small animal"
}

print(tab)
print(type(tab))

print('Q.2 You have given a list of subjects for student. Assume one classroom is required for 1 subject. How many classroom are needed by all students. "python , "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"')
subject = {"python" , "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print("We required : ",len(subject), "number of classes")

print('Q.3 WAP to enter marks of 3 subjects from the user and stores them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key and marks as value.')
marks = {
    "subject1" : input("Enter subject1 marks : "),
    "subject2" : input("Enter subject2 marks : "),
    "subject3" : input("Enter subject3 marks : ")
}
print(marks)
print(marks.values())
print(marks.keys())
print(type(marks))


# OTHER METHOD
marks = {}
sub1 = int(input("Enter subject1 marks : "))
marks.update({"subjext1" : sub1})
sub2 = int(input("Enter subject1 marks : "))
marks.update({"subject2" : sub2})
sub3 = int(input("Enter subject1 marks : "))
marks.update({"subject3" : sub3})

print(marks)
print(type(marks))


print("Q.4 Figure out a way to store 9 and 9.0 as seprate values in the set.")
val = {9.0, "9"}   #first solution
val1 = {                #2nd solution
    int : 9,
    float : 9.0
}
print(val1.values())

val2 = {   #3rd solution
    ("int", 9),
    ("float", 9.0)
}
print(val2)