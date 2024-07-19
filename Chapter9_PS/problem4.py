'''A file contains a word "Donkey" multiple times. You need to write a program which
replace this word with ##### by updating the same file.'''

word = "Donkey"
with open("/workspaces/python/Chapter9_PS/4_dunkey.txt", "r") as f:
    content = f.read()  # Read the entire file

newContent = content.replace(word, "#####")
with open("/workspaces/python/Chapter9_PS/4_dunkey.txt", "w") as f:
    f.write(newContent)