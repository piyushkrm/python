'''Question 7 : If the names of 2 friends are same; what will happen to the program in problem 6?'''

dic = {}
for i in range(4):
    name = input("Enter name : ")
    lang = input("Enter language name : ")
    dic.update({name:lang})
    
print(dic)