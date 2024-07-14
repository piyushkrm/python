name = input("Enter name : ")
date = input("Enter date : ")

print(f"Dear {name}\nYou are selected!\n{date}")

# OTHER METHOD
latter = '''Dear <|Name|>,
            You are selected!
            <|Date|>'''

print(latter.replace("<|Name|>", name).replace("<|Date|>",date))