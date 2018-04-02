#Review - Queues

class ListItem:
    
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.next = None
        self.prev = None

class MyList:
    
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def add(self, value):
        item = ListItem(value, self.length)
        
        if self.length == 0:
            self.head = item

        else:
            item.prev = self.tail
            self.tail.next = item
            
        self.tail = item
        self.length += 1

    def __str__(self):
        ans = str(self.head.value)
        current = self.head
        for entry in range(self.length - 1):
            current = current.next
            ans += ", " + str(current.value)
        return ans


newlist = MyList()
newlist.add(5)
newlist.add(7)
newlist.add("hello")
print(newlist.head.value)
print(newlist.head.next.value)
print(newlist.tail.value)
print(newlist)
