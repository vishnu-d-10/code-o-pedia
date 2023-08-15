# Python3 program for array rotation

arr = [1, 2, 3, 4, 5, 6]
#output2 = [3, 4, 5, 6, 1, 2] (d=2)
#output1 = [2, 3, 4, 5, 6, 1] (d=1)

def rotate(arr,d):
    n = len(arr)
    i=0
    temp=[]
    while i<d:
        temp.append(arr[i])
        i = i+1
    i=0
    while d<n:
        arr[i] = arr[d]
        d = d+1
        i = i+1
    arr[:] = arr[:i] + temp
    return arr

d = int(input("Enter the rotation required: "))
print("The rotated array: ", rotate(arr,d))