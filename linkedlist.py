class Node:
    def __init__(self, data):
        self.header = None
        self.tail = None
        self.size = 0

#adding node at the front
    def prepend(self, data):
        n = Node(data)
        if(self.size==0):
            self.header = n
            self.tail = n
        else:
            n.next = self.header
            self.header = n
        self.size +=1
        print(self.size)

# adding node at the end
    def(self, data):
        n = Node(data)
        if self.size == 0:
            self.header = n
            self.tail = n
        else:
            temp = self.tail
            self.tail = n
            temp.next = self.tail
        self.size += 1

# printing node
    def printList(self):
        data = ""
        current = self.header
        while(current != None): #None is the end end of the linkedlist
            data = data + str(current.data)
            current = current.next
        print(data)
        return data

    def removeFirst(self):
        if(self.size == 0):
            return None
        data = self.header.data
        if self.size == 1:
            self.header = None
            self.tail = None
        else:
            self.header = self.header.next
        self.size -=1
        return data