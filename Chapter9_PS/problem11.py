'''Write a python program to rename a file to "renamed_by_python.txt.'''

with open("/workspaces/python/Chapter9_PS/11_rename.txt") as f:
    content = f.read()


with open("/workspaces/python/Chapter9_PS/renamed_by_python.txt", "w") as f:
    f.write(content)

