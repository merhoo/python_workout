class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def enqueue(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.length += 1

    def dequeue(self):
        if self.head is not None:
            self.head = self.head.next
            self.length -= 1

    def peek(self):
        return self.head.value
