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

def bft(root):
  if root is None: return []
  vals = []
  children = [root]
  while len(children) > 0:
    newNode = children.pop()
    if newNode.left: children = [newNode.left] + children
    if newNode.right: children = [newNode.right] + children
    vals.append(newNode.val)
  return vals

def dft(root):
  if root is None: return []
  vals = []
  children = [root]
  while len(children) > 0:
    newNode = children.pop()
    if newNode.right: children = children + [newNode.right]
    if newNode.left: children = children + [newNode.left]
    vals.append(newNode.val)
  return vals

def dft_recursive(root):
  if root is None: return []
  lefts = dft_recursive(root.left)
  rights = dft_recursive(root.right)
  return [root.val] + lefts + rights

def bft_recursive(root):
  if root is None: return []
  lefts = bft_recursive(root.left) # [b, ]
  rights = bft_recursive(root.right)
  return [root.val] + lefts + rights


print(bft(a))
# print(bft_recursive(a))