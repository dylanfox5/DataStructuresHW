#Dylan Fox
#FizzBuzz

def main():

    for x in range(1, 100):
        if x%3 == 0 and x%5 == 0:
            print(x, "FizzBuzz")
        elif x%3 == 0:
            print(x, "Fizz")
        elif x%5 == 0:
            print(x, "Buzz")

main()
