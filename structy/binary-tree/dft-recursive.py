class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def dft_recursive(root):
  if root is None: return []
  lefts = dft_recursive(root.left)
  rights = dft_recursive(root.right)
  return [root.val] + lefts + rights

# a ---> b --> d
#   \      \-> e
#    \-> c --> f

# dft --> a b d e c f

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

print(dft_recursive(a))