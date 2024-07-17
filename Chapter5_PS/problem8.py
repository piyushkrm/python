'''Question 8 : If languages of two friends are same; what will happen to the program in problem 6?'''
dic = {}
for i in range(4):
    name = input("Enter name : ")
    lang = input("Enter language name : ")
    dic.update({name:lang})
    
print(dic)