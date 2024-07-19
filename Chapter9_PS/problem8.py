'''Write a program to make a copy of a text file "this. txt"'''

with open("/workspaces/python/Chapter9_PS/8_this.txt") as f:
    content = f.read()

with open("/workspaces/python/Chapter9_PS/8_this_copy.txt", "w") as f:
    f.write(content)
