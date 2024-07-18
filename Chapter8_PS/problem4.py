'''Write a recursive function to calculate the sum of first n natural numbers.'''

def sumNatural(n) :
    if n == 1:
        return 1
    return sumNatural(n-1) + n

x = int(input("Enter the number : "))
print(sumNatural(x))