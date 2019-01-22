from queues import Queue


class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    def add(self, value):
        if value > self.value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.add(value)
        else:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.add(value)

    def find(self, value):
        if self.value < value:
            if self.right is None:
                return False
            return self.right.find(value)
        elif self.value > value:
            if self.left is None:
                return False
            return self.left.find(value)
        else:
            return True
root = Node(5)
root.add(4)
root.add(3)
root.add(9)
print(root.find(4))
