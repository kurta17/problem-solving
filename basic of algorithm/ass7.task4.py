class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.count = 1  # new attribute, count the number of nodes in the subtree rooted at this node

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is not None:
                self._insert(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._insert(data, node.right)
            else:
                node.right = Node(data)
        node.count = 1 + self.size(node.left) + self.size(node.right)

    def size(self, node):
        if node is None:
            return 0
        else:
            return node.count

    def get_median(self):
        if self.root is None:
            return None
        count = self.root.count
        return self._get_median(self.root, count)

    def _get_median(self, node, size):
        mid = (size + 1) // 2
        if mid == self.size(node.left) + 1:
            return node.data
        elif mid < self.size(node.left) + 1:
            return self._get_median(node.left, size)
        else:
            return self._get_median(node.right, size)

# Usage:
bst = BST()
for i in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(i)
print(bst.get_median())  # Output: 5