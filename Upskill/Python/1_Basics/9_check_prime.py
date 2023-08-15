# Python3 program to check if it is a prime number

num = input("Enter the Input number: ")
num = int(num)

def check_prime(a):
    if int(a)>1:
        for i in range(2, int(a/2)+1):
            if(a%i)==0:
                print("{0} is not a prime number" .format(a))
                break
        else:
            print("{0} is a prime number" .format(a))
    else:
        print("{0} is not a prime number" .format(a))

check_prime(num)