#Dylan Fox
#Dictionary Search


file = open("wordlist.txt", "r")
lines = file.read().split(",")

words = ["hello", "my", "name", "is", "Dylan", "Fox"]


def linearSearch(word):

    index = 0

    for entry in lines:
        if entry == word:
            return index
        index += 1
                                    
print(linearSearch("hello"))
print(linearSearch("abbot"))


