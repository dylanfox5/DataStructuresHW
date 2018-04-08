#Dylan Fox
#Lab 7 - Linear Data Structures


class ListItem:

    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.next = None
        self.prev = None

class Queue:

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

    def remove(self):

        if self.length == 0:
            return
        else:
            #first = self.head 
            self.head = self.head.next
            self.length -= 1

    def __str__(self):
        
        ans = str(self.head.value)
        current = self.head
        for entry in range(self.length - 1):
            current = current.next
            ans += ", " + str(current.value)
        return ans       

class Stack:

    def __init__(self):
        self.length = 0
        self.top = None

    def add(self, value):

        item = ListItem(value, self.length)
        
        item.prev = self.top
        self.top = item
        self.length += 1

    def remove(self):

        if self.length == 0:
            return
        else:
            self.top = self.top.prev
            self.length -= 1

    def __str__(self):
        
        ans = str(self.top.value)
        current = self.top
        for entry in range(self.length - 1):
            current = current.prev
            ans += ", " + str(current.value)
        return ans

print("Here is a stack:")
stack = Stack()
stack.add(7)
stack.add(3)
stack.add(14)
stack.add(1)
stack.add(21)
stack.add(0)
stack.add(0)
stack.add(56)
print(stack)
print("Length:", stack.length)
stack.remove()
print(stack)
print("Length:", stack.length)
print("Here is a queue:")
queue = Queue()
queue.add(7)
queue.add(3)
queue.add(14)
queue.add(1)
queue.add(21)
queue.add(0)
queue.add(0)
queue.add(56)
print(queue)
print("Length:", queue.length)
queue.remove()
print(queue)
print("Length:", queue.length)
