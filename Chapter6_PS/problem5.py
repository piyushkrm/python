'''Question 4 : Write a program which finds out whether a given name is present in a list or not.'''
ls = ["Piyush", "Palak", "Aayush", "Harsh", "Abhinav", "Megha", "Daisy", "Prasun", "Bholu"]
name = input("Enter your name : ").strip()
if name in ls:
    print("Name found in the list!")
else:
    print("Name not found in the list!")