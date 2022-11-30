class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def bfs_iterative(root):
  if root is None: return []
  stack = [root]
  vals = []
  while len(stack) > 0:
    node = stack.pop()
    vals.append(node.val)
    if node.right is not None: stack = stack + [node.right]
    if node.left is not None: stack = stack + [node.left]
  return vals

# node a --> node b --> node d
#       \           \-> node e
#        \-> node c --> node f

# dfs --> a b d e c f

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
c.left = f

print(bfs_iterative(a))