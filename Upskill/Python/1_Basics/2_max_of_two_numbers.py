# Python3 program to find maximum of two numbers

num1 = input("First number: ")
num2 = input("\nSecond number: ")

def maximum(a,b):
    if a > b:
        return a
    else:
        return b
    
print("The maximum of {0} and {1} is {2}" .format(num1,
											num2, maximum(num1,num2)))