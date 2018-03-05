#Dylan Fox
#Dictionary Search

import wordlist
import time

def linearSearch(word):

    index = 0

    for entry in wordlist.words:
        if entry == word:
            return index
        else:
            index += 1

def binaryRecursive(low, high, word):

    middle = int((low + high)/2)

    if word == wordlist.words[middle]:
        return middle
    elif low == high:
        if wordlist.words[low] == word:
            return low
        else:
            return None
    else:
        if word < wordlist.words[middle]:
            return binaryRecursive(low, middle-1, word)
        elif word > wordlist.words[middle]:
            return binaryRecursive(middle+1, high, word)

def calcTime():
    start = time.clock()
    print(linearSearch("python"))
    stop = time.clock()
    print("It took", stop - start, "seconds to run linearly.")
    start = time.clock()
    print(binaryRecursive(0, len(wordlist.words), "python"))
    stop = time.clock()
    print("It took", stop - start, "seconds to run recursively.")

calcTime()
