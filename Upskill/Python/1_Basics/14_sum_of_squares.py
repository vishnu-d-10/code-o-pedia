# Python3 program for Sum of squares of first n natural numbers

n = int(input("Enter the input: "))

def sumofsquare(n):
    i = 1
    temp = 0
    while(i<=n):
        temp = temp + (i**2)
        i = i+1
    return temp
    
print("Output: ", sumofsquare(n))