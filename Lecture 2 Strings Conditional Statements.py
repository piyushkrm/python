print("STRING")
str = "PiyushMishra"
print(str)
print(len(str))

str1 = "Piyush"
str2 = "Mihra"
con = str1 + str2
print(con)


print("SLICING")
slicingstring = "PiyushMishra"
print(slicingstring[0 : 5])
print(slicingstring[0 : ])
print(slicingstring[0 : len(slicingstring)])

print("NEGATIVE SLICING") 
neg = "Coconut"
print(neg[ : -2])


cdr = "i am a Coder Coder."
cdr = "i am a Coder."
print(cdr.endswith("der."))
print(cdr.capitalize())
print(cdr.replace("Coder", "Enginner"))
print(cdr.find("am"))
print(cdr.count("a"))



print ("hey what are you doing")
strin = "hey what are you doing"
strop = input("Enter sentence........ :\n")
rep = strin.replace("Coder", "Software Engineer")
rep = strin.replace(strop, strin)
print(rep)



print("Lets PRACTICE")
print("Q.1 WAP to input from user's first name and print its length.")
name = input("Enter your first name........\n")
print("Length  : ",len(name))


print("Q.2 WAP to find the occurence of '$' in a String")
occur = "Hi i am$ the $ symbol"
print(occur.count("$"))



print("Conditional Statement")
age = int(input("Enter your age for apply licence : \n"))
if(age >= 18):
    print("You are elegible for licence.")
elif(age >= 60):
    print("You are not safe for driving")
else:
    print("You are not elegible")


print("Grade students based on marks")
grade = int(input("Enter your Marks : "))
if(grade > 100):
    print("Envalid marks")
elif(grade >= 90 and grade <= 100):
    print("You passed with A grade")
elif(grade >= 60 and grade <= 89):
    print("You passed with B grade")
elif(grade >= 40 and grade <= 59):
    print("You passed with C grade")
else:
    print("Beter Luck Next Time")

print("Nesting")
vote = int(input("Enter you age for voting.....\n"))
if(vote >= 18):
    if(vote >= 100):
        print("You are above of", vote, "So you can't give vote.")
    else:
        print("Now you are elegible for vote.")
else:
    print("You have not valid age of voting.")


print("LETS PRACTICE")
print("Q.1 WAP to check if a number entered by the user is odd or even.")
number = int(input("Enter number for checking the number is EVEN or ODD......\n"))
if(number % 2 == 0):
    print("Number is Even.")
else:
    print("Number is odd.")


print("Q.2 WAP to check if a number is multiple of 7 or not.")
mul = int(input("Enter number for checking entered number is multiple of 7 or not....\n"))
if(mul % 7 == 0 and mul != 0):
    print("Number is Multiple of 7")
else:
    print("Number is not Multiple of 7")


print("Q.3 WAP to find the greatest of 3 numbers entered by the user.")
one = int(input("Enter first Number : "))
two = int(input("Enter second Number : "))
three = int(input("Enter third Number : "))
four = int(input("Enter fourth Number : "))
if(one <=0 and two <= 0 and three <= 0 and four <= 0):
    print("Enter greterthan 0 number.")
elif(one > two and one > three and one > four):
    print("First number entered by you is greatest, you entered first number is : ",one)
elif(two > one and two > three > four):
    print("Second number is greatest, You entered second number is :", two)
elif(three > four and three > two and three > one):
    print("Third number is greatest, You entered third number is : ",three)
else:
    print("Fourth number is greatest, You entered fourth number is : ",four)