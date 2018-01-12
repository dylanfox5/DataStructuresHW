#Dylan Fox
#Write a program that iterates through all numbers <50 and determines if they are prime or not.

def main(n):
    for x in range(2,n):
        isPrime = True
        for y in range(2, x):
            if x%y == 0:
                isPrime = False
                break
        if isPrime:
            print(x, "is prime")

print(main(50))


    
