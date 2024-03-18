class Node:
    def __init__(self, value):
        self.value = value
        self.count = 1
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            node.count += 1
        return node

    def find(self, value):
        return self._find(self.root, value) is not None

    def _find(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._find(node.left, value)
        else:
            return self._find(node.right, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.count > 1:
                node.count -= 1
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._find_minimum(node.right)
                node.value = successor.value
                node.count = successor.count
                node.right = self._delete(node.right, successor.value)

        return node

    def _find_minimum(self, node):
        while node.left:
            node = node.left
        return node

bst = BST()
bst.insert(20)           # Inserts the first copy of 20
bst.insert(20)           # Inserts the second copy of 20
bst.delete(20)  
print(bst.find(20))         # Deletes one copy of 20
assert bst.find(20)      # Returns True, as one copy of 20 still exists
bst.delete(20) 
print(bst.find(20))           # Deletes the second copy of 20
assert not bst.find(20)  # Both copies are deleted, should return False


