#Dylan Fox
#Lab 4: Part B - Fibonacci Sequence

import time

def fibRecursive(integer):

    if integer == 1 or integer == 0:
        return 1
    else:
        return fibRecursive(integer-1) + fibRecursive(integer-2)

def fib(integer):
    prevNum = 1
    num = 1
    counter = 0
    for i in range(integer):
        counter = prevNum+num
        prevNum = num
        num = counter
    return prevNum

def compare():

    for i in range(30, 100, 10):
        startTimeR = time.clock()
        fibRecursive(i)
        stopTimeR = time.clock()
        startTimeL = time.clock()
        fib(i)
        stopTimeL = time.clock()

        secondsR = stopTimeR - startTimeR
        secondsL = stopTimeL - startTimeL
        
        print(i, secondsR, secondsL)

        if secondsR < secondsL:
            print("Recursive function was faster for", i,"th fibonacci number")
        else:
            print("Linear function was faster for", i,"th fibonacci number")
