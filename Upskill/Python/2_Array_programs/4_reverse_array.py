# Python3 program for array reverse

arr = [1, 2, 3, 4, 5, 6]

def rev_array(arr):
    temp = []
    temp = arr[ : :-1]
    return temp

print("Output: ",rev_array(arr))