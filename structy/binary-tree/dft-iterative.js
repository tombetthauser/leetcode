class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const dft = (root) => {
  if (root === null) return []
  const stack = [root];
  const vals = [];
  while (stack.length > 0) {
    const node = stack.pop();
    if (node.right) stack.push(node.right);
    if (node.left) stack.push(node.left);
    vals.push(node.val);
  }
  return vals;
}

// a --> b --> d
//  \      \-> e
//   \-> c --> f

// dft --> a b d e c f

const a = new Node('a');
const b = new Node('b');
const c = new Node('c');
const d = new Node('d');
const e = new Node('e');
const f = new Node('f');

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.left = f;

console.log(dft(a));