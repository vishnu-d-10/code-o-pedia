# Question 1
# Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# > You must write an algorithm with O(log n) runtime complexity.

def first(arr, low, high, x, n):
	if(high >= low):
		mid = low + (high - low) // 2
		if((mid == 0 or x > arr[mid - 1]) and arr[mid] == x):
			return mid
		elif(x > arr[mid]):
			return first(arr, (mid + 1), high, x, n)
		else:
			return first(arr, low, (mid - 1), x, n)

	return -1

def last(arr, low, high, x, n):
	if (high >= low):
		mid = low + (high - low) // 2
		if ((mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x):
			return mid
		elif (x < arr[mid]):
			return last(arr, low, (mid - 1), x, n)
		else:
			return last(arr, (mid + 1), high, x, n)

	return -1

#Input program
arr=list(map(int, input("Enter the elements of array: ").strip().split()))
print(arr)
n = len(arr)
#To check if input is in non-descending order
flag = 0
test_list1 = arr[:]
test_list1.sort()
if (test_list1 == arr):
    flag = 1

if (flag == 0) :
    print ("Input is not in non-descending order. Try again with a different input which is in non-descending order")
    exit()

x = int(input("Enter the Target value: "))

#Output
Output = []
Output.append(first(arr, 0, n - 1, x, n))
Output.append(last(arr, 0, n - 1, x, n))
print("Output: ", Output)

