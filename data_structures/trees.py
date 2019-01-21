from anytree import Node, RenderTree

root = Node(1)

child1 = Node(2, parent=root)
child2 = Node(3, parent=root)
sam = Node("Sam", parent=child1)

print(root)

for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))

print(root.children)
