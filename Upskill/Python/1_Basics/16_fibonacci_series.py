# Python3 program to check if it is a prime number

def fib(n):
    count = 1
    num1 = 0
    num2 = 1
    output = num2
    while int(count) <= int(n):
        print(output, end=" ")
        count += 1
        num1 = num2
        num2 = output
        output = num1 + num2

num = input("Enter the Input number: ")
fib(num)