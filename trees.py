from anytree import Node, RenderTree

root = Node(1)

child1 = Node(2, parent=root)
child2 = Node(3, parent=root)
