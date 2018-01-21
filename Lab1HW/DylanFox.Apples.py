#Dylan Fox
#Apples

def main():
    priceList = [14, 6, 9, 7, 8, 10, 3, 9]
    length = len(priceList)
    largestDifference = 0
    highestProfit = 0.0

    for x in range(length):
        if x+1 < length and priceList[x+1] - priceList[x] > largestDifference:
            largestDifference = priceList[x+1] - priceList[x]
            highestProfit = ((100 / priceList[x]) * priceList[x+1]) - 100

    print("Highest possible profit is:", highestProfit)

main()
