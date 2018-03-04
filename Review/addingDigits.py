#Review


def addDigits(num, count):

    x = count

    if num < 10:
        x += num
        return x
    else:
        x += num%10
        return addDigits(int(num/10), x)

print(addDigits(456, 0))
