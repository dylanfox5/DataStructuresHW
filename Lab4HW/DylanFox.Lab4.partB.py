#Dylan Fox
#Lab 4: Part B - Fibonacci Sequence

import time

def fibRecursive(integer):

    if integer == 1 or integer == 0:
        return 1
    else:
        #print(integer, integer-1, integer-2)
        return fibRecursive(integer-1) + fibRecursive(integer-2)

def fib(integer):

    if integer <= 1:
        return 1
    else:
        num = 2
        numPrev = 1
        for x in range(2,integer):
            temp = num
            num += numPrev
            numPrev = temp
    return num

def main():
    n = eval(input("Enter a number:"))

    print("Recursive:",fibRecursive(n))
    print("Iterative:",fib(n))

def compare():
    time.clock()
    print("Calculating Fibonacci Sequence with Recursion:")
    print(fibRecursive(30))
    print(fibRecursive(40))
    stopTime = time.clock()
    print("It took", int(stopTime),"seconds to run it recursively")
    print("Calculating Fibonacci Sequence Interatively:")
    time.clock()
    print(fib(30))
    print(fib(40))
    stopTime1 = time.clock()
    print("It took", stopTime1,"seconds to run it interatively")
