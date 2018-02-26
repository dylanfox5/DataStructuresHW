#Sorting and Searching

list1 = [7, 5, 4, 1, 9, 0, 3, -2, -21, -6, 13]
sortedList = sorted(list1)

print(list1)
print(sortedList)
print(list1 == sortedList)

def bubbleSort(list):

    for i in range(len(list)-1):
        for i in range(len(list)-1):
            if list[i+1] < list[i]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

    return list

print(bubbleSort(list1))


