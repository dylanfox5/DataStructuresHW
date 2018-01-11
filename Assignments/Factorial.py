#Dylan Fox
#Write a program that uses recursion to compute the factorial of 10. 

def factorial(n):
    if n<1:
        return 1
    else:
        return n * factorial(n-1)
