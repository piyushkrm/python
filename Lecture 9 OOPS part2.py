class Student :
    def __init__(self, name, age, phone) -> None:
        self.name = name
        self.age = age
        self.phone = phone

s1 = Student("Piyush", 20, 7488241964)
# print(s1.name)
# del s1.name
# # del s1
# print(s1.age)
# print(s1.phone)


# s1 = Student("Abhinav")
# print(s1.name)


# PUBLIC AND PRIVATE ALLTIBUTE

class Account :
    def __init__(self, account_no, account_pass) -> None:
        self.account_no = account_no
        # self.account_pass = account_pass        #public
        self.__account_pass = account_pass        #private

    def resetpass(self):
        print(self.__account_pass)

acc = Account("748596", "pihu")
print(acc.account_no)
print(acc.resetpass())
# print(acc.account_no)
# print(acc.account_pass)
# print(acc.__account_pass)
