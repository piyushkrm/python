# tuple are immutable
tup = (1, "pihu", "pihu", 530.58, 'a', False)
print(type(tup))
# tup[1] = "sona"                             #occur error because of tuple are immutable
print(tup)

print(tup.count("pihu"))                    #count
print(tup.index(1))                         #indexing
t1 = (1, 2, 3, 4)
t2 = ("pihu", "sona")
print(t1 + t2)                              #concatenation 

ep = ("pihu", "sona")                       #Repetition
print(ep*5)

print(tup[1:3])                             #slicing
print(len(tup))                             #length 


print(1 in tup)                             #contain or not(Membership)