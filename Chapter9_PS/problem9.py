'''Write a program to find out whether a file is identical & matches the content of
another file.'''

with open("/workspaces/python/Chapter9_PS/9_file1.txt") as f:
    content1 = f.read()

with open("/workspaces/python/Chapter9_PS/9_file2.txt") as f:
    content2 = f.read()


if content1 == content2:
    print("Yes ! these files are identical")
else:
    print("No ! these files are not identical")
