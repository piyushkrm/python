str = "Hey piysuh you are the best"
str1 = "You looking good"

file = open("/workspaces/python/Chapter9/makeFile.txt", "w")
file.write(str)
file.close()

f = open("/workspaces/python/Chapter9/makeFile.txt")
rd = f.read()
print(rd)
f.close()

file = open("/workspaces/python/Chapter9/makeFile.txt", "w")
file = file.write(str1) 