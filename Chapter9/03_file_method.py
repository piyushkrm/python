# # Readlines
# file = open("/workspaces/python/Chapter9/file.txt")
# read = file.readlines()             # read all lines
# print(read)
# file.close()

# Readline
file = open("/workspaces/python/Chapter9/file.txt")
read = file.readline()             # read one line at a time
# print(read)
# read2 = file.readline()             # read one line at a time
# print(read2)

# we print all line using loop
while read != "":
    print(read)
    read = file.readline()

file.close()

# append
file = open("/workspaces/python/Chapter9/file.txt", "a")
file.write("\nThis is piyush mishra")
file.close()