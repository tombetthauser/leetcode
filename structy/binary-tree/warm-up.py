class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def treePrint(root):
  children = [root]
  while len(children) > 0:
    newNode = children.pop()
    print(newNode.val)
    if newNode.left: children.append(newNode.left)
    if newNode.right: children.append(newNode.right)

treePrint(a)