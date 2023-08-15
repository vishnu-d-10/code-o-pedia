# Python3 program to find largest element in an array

arr = [1, 12, 14, 15]

def largest(arr):
    num2 = 0
    for i in arr:
        num1 = i
        if num1 > num2:
            num2 = num1
    return num2

print("Largest element in array: ", largest(arr))