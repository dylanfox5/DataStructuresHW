def addDigits(num):
    if num == 0:
        return 0
    else:
        return num%10 + addDigits(num//10)

print(addDigits(eval(input("Enter a number: "))))
