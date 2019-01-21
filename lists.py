class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        string = ""
        current = self.head
        while current is not None:
            string += str(current.value) + " "
            current = current.next
        return string

    def get(self, index):
        if index > self.length:
            raise Exception("index should not exceed length.")
        current = self.head
        for i in range(index):
            current = current.next
        return current.value

    def add(self, next_value):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(next_value)
        self.length += 1

    def update(self, index, value):
        if index > self.length:
            raise Exception("index should not exceed length.")
        current = self.head
        for i in range(index):
            current = current.next
        current.value = value


linked_list = SLinkedList()
linked_list.head = Node(1)
linked_list.add(2)
linked_list.add(4)
linked_list.update(1, 6)
print(linked_list)
print(linked_list.get(2))
