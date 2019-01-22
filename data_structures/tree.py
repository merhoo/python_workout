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

    def preorder(self):
        print self.value,
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print self.value,
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.inorder()
        if self.right:
            self.right.inorder()
        print self.value,


# def level(head):
#     queue = Queue()
#     queue.enqueue(head)
#     while not queue.isEmpty():
#         current = queue.dequeue()
#         print current,
#         if current.left is not None:
#             queue.enqueue(current.left)
#         if current.right is not None:
#             queue.enqueue(current.right)


root = Node(5)
root.add(4)
root.add(3)
root.add(9)
print(root.find(4))
root.preorder()
print
root.postorder()
print
root.inorder()
print
# level(root)
# print
