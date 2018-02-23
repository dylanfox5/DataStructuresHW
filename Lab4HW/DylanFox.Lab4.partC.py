#Dylan Fox
#Lab 4 - Part C: Dynamic Programming

import time

array = [1,2]

def fibonacci(n):

    if n == 0:
        return 1
    elif n <= len(array):
        return array[n-1]
    else:
        temp = fibonacci(n-1) + fibonacci(n-2)
        array.append(temp)
        return temp

def main():

    for i in range(30, 100, 10):
        startTime = time.clock()
        fibonacci(i)
        stopTime = time.clock()
        print("It took", stopTime - startTime,"seconds to run dynamically.")


main()
