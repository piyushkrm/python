'''A file contains a word "Donkey" multiple times. You need to write a program which
replace this word with ##### by updating the same file.'''


with open("/workspaces/python/Chapter9_PS/4_dunkey.txt", "r+") as f:
    content = f.readlines()  # Read the entire file
    f.seek(0)  # Move the file pointer back to the beginning
    f.writelines(line.replace("Donkey", "#####") for line in content)  # Replace and write the content
    f.truncate()  # Remove any remaining content
