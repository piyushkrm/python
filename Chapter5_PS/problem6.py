'''Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.'''
dic = {}
for i in range(4):
    name = input("Enter name : ")
    lang = input("Enter language name : ")
    dic.update({name:lang})
    
print(dic)
