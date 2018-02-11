#Dylan Fox
#Lab 4: Part A - Collatz Conjecture

def calculate(integer, x):

    steps = x

    if integer == 1:
        steps += 1
        print("It takes",steps, "steps.")
        return 1
    else:
        if integer%2 == 0:
            steps += 1
            return calculate(integer/2, steps)
        else:
            steps += 1
            return calculate((integer*3)+1, steps)

def main():
    integer = eval(input("Enter a positive integer:"))
    calculate(integer, 0)

main()

