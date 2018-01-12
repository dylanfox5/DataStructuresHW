#Dylan Fox
#Write a program that uses recursion to compute the factorial of 10. 

def main(n):
    if n == 1:
        return 1
    else:
        return n * main(n-1)

print(main(10))
