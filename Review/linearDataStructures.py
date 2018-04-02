#Dylan Fox
#Linear Data Structure

class LinearItem:

    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

    def setNext(self, item):
        self.next = item
        
    def setPrev(self, item):
        self.prev = item
        
    def getNext(self):
        return self.next
    
    def getPrev(self):
        return self.prev

    def getVal(self):
        return self.val

class Linear:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def add(self, item):
        newItem = LinearItem(item)
        if self.length == 0:
            self.first, self.last = newItem, newItem
            self.length += 1
        else:
            self.last.setNext(newItem)
            newItem.setPrev(self.last)
            self.last = newItem
            
            self.length +=1
