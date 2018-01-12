#Dylan Fox
#Write a program that iterates through all numbers <50 and determines if they are prime or not.

def main(n):
    print("0 is not prime")
    print("1 is not prime")
    for x in range(2,n):
        isPrime = True
        for y in range(2, x):
            if x%y == 0 and x != y:
                isPrime = False
        if isPrime == True:
            print(x, "is prime")
        else:
            print(x, "is not prime")

print(main(50))


    
