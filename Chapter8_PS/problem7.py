'''Write a python function to remove a given word from a list ad strip it at the same
time.'''

def remove(lis, word) :
    n = []
    for i in lis:
        if not i == word:
            n.append(i.strip(word))
    return n

lis = ["Piyush", "Rohan", "Subham", "an"]
print(remove(lis, "an"))