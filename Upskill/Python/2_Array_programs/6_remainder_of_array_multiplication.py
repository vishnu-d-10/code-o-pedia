# Python3 program for remainder of array multiplication divided by n

# Input : arr[] = {100, 10, 5, 25, 35, 14}, n = 11
# Output : 9
# Explanation: 100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9

def rem(arr,d):
    i = 0
    n = len(arr)
    temp = 1
    while i<n:
        temp = temp * arr[i]
        i = i+1
    remainder = temp%d
    return remainder

arr = [100, 10, 5, 25, 35, 14]
d = int(input("Enter the divisor: "))
print("The Remainder is: ",rem(arr,d))
