#Dylan Fox
#Dictionary Search

import wordlist

def linearSearch(word):

    index = 0

    for entry in wordlist.words:
        if entry == word:
            return index
        else:
            index += 1

print(linearSearch("abbot"))

def binaryRecursive(word, x):

    index = 0
    middle = int((len(wordlist.words) - 1)/2)
    item = wordlist.words[middle]

    if item == word:
        return index

    elif item>word:
        index += 1
        return binaryRecursive([0, middle], index)
    
    elif item<word:
        index += 1
        return binaryRecursive([middle], index)
    
print(binaryRecursive("abbot", 0))
