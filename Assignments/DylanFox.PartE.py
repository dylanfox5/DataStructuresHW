#Dylan Fox
#Write a program that iterates through all numbers <50 and determines if they are prime or not.

def primeNumber(n):
    primeNumbers = 0
    for x in range(0,n):
        isPrime = True
        for y in range(2, x):
            if x%y == 0 and x != y:
                isPrime = False
        if isPrime == True:
            primeNumbers += 1
    print(primeNumbers)
    
