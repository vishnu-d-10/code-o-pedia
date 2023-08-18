# Python program to interchange first and last elements in a list
# Input : [12, 35, 9, 56, 24]

#Input program
list1 = list(map(int, input("Enter the elements of array: ").strip().split()))
print("Input: ",list1)
n = len(list1)

def interchange(list1,n):
    temp = []
    temp = list1[0]
    list1[0] = list1[n-1]
    list1[n-1] = temp
    return list1

print("Output: ", interchange(list1,n))
