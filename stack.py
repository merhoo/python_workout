class Stack:

    def __init__(self, ):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def isBalanced(braces):
    stack = Stack()
    for i in range(len(braces)):
        if braces[i] is '{':
            stack.push('{')
        if braces[i] is '[':
            stack.push('[')
        if braces[i] is '(':
            stack.push('(')
        if braces[i] is '}':
            if stack.pop() is not '{':
                return False
        if braces[i] is ']':
            if stack.pop() is not '[':
                return False
        if braces[i] is ')':
            if stack.pop() is not '(':
                return False
    return stack.isEmpty()
