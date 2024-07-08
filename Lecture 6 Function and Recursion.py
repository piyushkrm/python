def calculation(p, s):
    sum = p + s
    return sum

print(calculation(25, 59))
print(calculation(55, 59))

def hello():
    print("hello World!")

hello()
hello()
hello()

# PRACTICE 
print("Q.1 Calculate average of three number : ")
def average(p, q, r):
    avg = (p + q +r) / 3
    print("Average of all three number is : ",avg)

one = int(input("Enter first number : "))
two = int(input("Enter second number : "))
three = int(input("Enter third nuber : "))
average(one, two, three)



# PRINT FUNCTION
print("piyush", end="-")
print("mishra")
print("piyush","mishra")


# DEFAULT PARAMETER 
def default(p=1, s=2):
    k = p + s
    print(k)
    return k


default() #default parameter

# LETS PRACTICE
print("Q.1 WAF to print the length of a list. (list is the parameter)")
number = [10, 50, 80, 45, 63, 83, 44, 12, 2, 99, 0, 36]

def length(list):
    print("Length : ",len(list))
    return list


length(number)

cities = ["Araria", "Purnia", "Karnal", "Ambala", "Kishangang", "Katihar", "Madhepura", "Patna", "Ranigang"]
length(cities)

print("Q.2 WAF to print the elements of a list in a single line. (list is the parameter)")
number = [10, 50, 80, 45, 63, 83, 44, 12, 2, 99, 0, 36]
print(number[0], end=" ")
print(number[1], end=" ")
print(number[2], end=" ")
print(number[3], end=" ")
print(number[4], end=" ")
print(number[5], end=" ")
print(number[6], end=" ")
print(number[8], end=" ")
print(number[9], end=" ")
print(number[10], end=" ")
print(number[11])

# do this using function 
def print_list(list):
    for i in list:
        print(i, end=" ")

print_list(number)
print_list(cities)

print("Q.3 WAF to find the factorial of n. (n is the parameter)")
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

factorial(8)
factorial(12)


print("Q.4 WAF to convert USD to INR")
def usd_inr(usd):
    inr = usd * 83
    print("Convert", usd, "USD to INR = ", inr)
    return inr

usd_inr(1)
usd_inr(2)
usd_inr(10)


# HOME WORK
print("Q.5 Take a input number from user and check the number is odd then print ODD otherwise print EVEN")
def even_odd(num):
    if(num % 2 == 0):
        print("EVEN")
    else:
        print("ODD")
    
num = int(input("Enter a number for check the number is ODD or EVEN : "))
even_odd(num)


#recursive function
# RECURSION
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
show(5)

# RECURSION FOR factorial
def fact(n):
    if(n == 0 or  n == 1):
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))

# PRACICE 
print("Q.1 Write a recursive function to calculate the sum of first n natural numbers.")
def natural_number(n):
    if(n == 0):
        return 0
    else:
        return n + natural_number(n - 1)
inputNum = int(input("Enter number for calculate sum of first natural number : "))
print("Sum of first",inputNum, "Natural is :",natural_number(inputNum))


print("Q.2 Write a recursive function to print all elements in a list. (Hint : Use list and index as parameter)")
element = ["piyush","abhinav","aayush","aditya","harsh","palak","megha","parsun","daisy"]
def list_recursive_fun(list, idx=0):
    if(idx ==  len(list)):
        return
    # print(list[idx], end="|")
    print(list[idx])
    list_recursive_fun(list, idx+1)
    
list_recursive_fun(element)



