# Python3 program for array reverse

arr = [1, 2, 3, 4, 5, 6]
# output = [6, 5, 4, 3, 2, 1]

def reverse(arr):
    n = len(arr)
    i = 0
    temp = []
    while i<n:
        temp.append(arr[n-i-1])
        i = i+1
    return temp

print("Reversed array: ", reverse(arr))