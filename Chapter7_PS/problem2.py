'''Write a program to greet all the person names stored in a list 'per' and which starts
with S.
person =["Pihu", "Soham", "Sona", "Rahul"]'''

person =["Pihu", "Soham", "Sona", "Rahul", "Sam", "Sunder", "saurav", "Sumit", "sudhir", "Piyush", "Palak"]
person_list = [element.capitalize() for element in person]
for i in person_list:
    if i[0] == "S":
        print(f"Hello {i}!")