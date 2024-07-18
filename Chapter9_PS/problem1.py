'''Wrte a program to read the text from a given file 'poems.txt' and find out whether it
contains the word 'twinkle'.'''

f = open("/workspaces/python/Chapter9_PS/twinkel.txt")
content = f.read()
rd = content.lower()
if "twinkle" in content:
    print("The word twinkle is present in the file")
else:
    print("The word twinkle is not present in the file")

f.close()