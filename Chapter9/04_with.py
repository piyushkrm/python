file = open("/workspaces/python/Chapter9/file.txt")
print(file.read())
file.close()

# The same can be written using with statement like this
with open("/workspaces/python/Chapter9/file.txt") as op:
    print(op.read())
# Dont have to explicitly close the file