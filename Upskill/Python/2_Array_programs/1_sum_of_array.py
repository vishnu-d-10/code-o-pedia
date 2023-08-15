# Python3 program to find sum of an array

arr = [1, 12, 14, 15]

def sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

print("Sum of array: ", sum(arr))