#Dylan Fox
#Dictionary Search


file = open("wordlist.txt", "r")

#lines = file.read().split(",")

words = ["hello", "my", "name", "is", "Dylan", "Fox"]


def linearSearch(word):

    index = 0

    for line in file:
        for entry in line.split():
            if entry == word:
                return index
            else:
                index += 1

##    for entry in words:
##        if entry == word:
##            return index
##        index += 1
                                    
#print(linearSearch("hello"))
print(linearSearch("abbot"))


