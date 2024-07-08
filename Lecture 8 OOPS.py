# CREATE CLASS
class Student:
    name = "piyush"
    phone = 7488241964

# for using class with the help of objects
# THIS IS A OBJECT
s = Student()
print(s.name)

p = Student()
print(p.phone)

# ANOTHER EXAMPLE
class Car:
    color = "Black"
    brand = "Audi"
    price = "5cr"
    manufactured = "in India"

car1 = Car()
print(car1.brand)
print(car1.color)
print(car1.manufactured)


# CONSTRUCTOR
class Teacher:
    def __init__(self, name):
        print("Adding new teacher in our college !")
        self.name = name
        print(name)

tech = Teacher("\nPiyush")
tech = Teacher("\nAditya")
tech2 = Teacher("\nSaloni")



class Students:
    def __init__(self, name, phone, gmail):
        # print("Student Information !")
        self.name = name
        self.phone = phone
        self.gmail = gmail
        # print(name, phone, gmail)
        # print(name, phone, gmail)

print("Student Information !\n")
print("Student 1")
tech = Students("Piyush", 7488241964, "") 
print(tech.name, tech.phone, tech.gmail)

print("\nStudent2")
tech1 = Students("Aditya", "", "piyushkrm03@gmail.com")
print(tech1.name, tech1.phone, tech1.gmail)


# DEFAULT CONSTRUCTOR
class Default:
    def __init__(self) -> None:
        pass

# PARAMETER CONSTRUCTOR
class ParameterConstructor:
    def __init__(self, name, email):
        self.name = name
        self.email = email


# INSTANCE Attribute
class Instance_Attribute:
    def __init__(self, name):
        self.name = name

inst = Instance_Attribute("PIHU")
print(inst.name)


# CLASS Attribute
class Class_Attribute:
    college_name = "SIET"
    def __init__(self, name):
        self.name = name

inst = Class_Attribute("PIHU")
print(inst.name, inst.college_name)


# METHODS
class Method:
    def __init__(self, name, age, belong):
        self.name = name
        self.belongfrom = belong
        self.age = age

    def msg(self):
        print("Welcome", self.name, self.age)

    def belonging(self):
        return self.belongfrom


m1 = Method("Piyush",18, "Bihar")
m1.msg()
print(m1.belonging())


# LETS PRACTICE
print("Q.1 Create a class that name & marks of 3 subjects as arguments in cnstructor.\nThen create a method to print the average.")
class stu:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    
    def avg(self):
        averages = (self.marks1 + self.marks2 + self.marks3) / 3
        return averages

mr = stu("piyush",95, 85, 75)
print("Average of",mr.name,"is in all subjects are",mr.avg())

# ANOTHER METHODS

class stu:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Heyy", self.name, "your average marks is ", sum/3)

ls = stu("pihu", [90, 93, 98])
ls.avg()

ls.name = "piyush Mishra"
ls.avg()


# STATIC METHOD
class static:
    @staticmethod
    def __init__() -> None:
        print("Hey Static Method")

static()

# ABSTRACTION
class Car:
    def __init__(self) -> None:
        self.acc = False
        self.cluth = False
        self.brk = False

    def start(self):
        self.acc = True
        self.cluth = True
        print("Car started....")

car1 = Car()
car1.start()


# LETS PRACTICE 
print("Q.1 Creste Account class with two attributes - balance & account no. \nCreate methods for debit, credit & printing the balance.")
class Account:
    def __init__(self, balance, account_no) -> None:
        self.account_no = account_no
        print("Account number is =",self.account_no)
        if(balance <= 0):
            self.aval_ammount_credit()
        self.balance = balance
        print("Account number is =",self.account_no)
        self.aval_ammount()

    def credit(self, ammount):
        if(ammount <= 0):
            self.aval_ammount_credit()
        self.balance += ammount
        print("Rs.",ammount,"is credited")
        self.aval_ammount()

    def debit(self, ammount):
        if(ammount > self.balance):
            self.aval_ammount_debit()
        self.balance -= ammount
        print("Rs.",ammount,"is debited")
        self.aval_ammount()

    def aval_ammount_debit(self):
        print("You have not suffecient balance for debit")

    def aval_ammount_credit(self):
        print("Invalid Ammount !")

    def aval_ammount(self):
        print("Available ammount is =",self.balance)


account = Account(-100, 784512235689)
# account.credit(1500023)
# account.debit(96)
# account.credit(-89)