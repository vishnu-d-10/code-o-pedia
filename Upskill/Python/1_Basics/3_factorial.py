# Python3 program to find factorial of a number

num = int(input("Input number: "))

def factorial(a):
    if a < 0:
        return 0
    elif a == 0 or a == 1:
        return 1
    else:
        fact = 1
        while (a > 1):
            fact = fact * a
            a = a - 1
        return fact
    
print("Factorial of {0} is {1}" .format(num,
                                            factorial(num)))