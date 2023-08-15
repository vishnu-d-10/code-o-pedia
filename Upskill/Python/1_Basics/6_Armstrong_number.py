# Python3 program to check Armstrong number

num = input("Enter the Input number: ")

def armstrong(a):
    sum = 0
    n = len(str(a))
    for digit in a:
        sum += int(digit)**n
    if int(sum) == int(a):
        print("Input {0} is a Armstrong number" .format(a))
    else:
        print("Input {0} is not a Armstrong number" .format(a))

armstrong(num)