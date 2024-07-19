'''Repeat program 4 for a list of such words to be censored.'''

words = ["Donkey", "bad", "good", "boy"]

with open("/workspaces/python/Chapter9_PS/5_listword.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "*" * len(word))

with open("/workspaces/python/Chapter9_PS/5_listword.txt", "w") as f:
    f.write(content)