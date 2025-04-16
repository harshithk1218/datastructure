class TreeNode:
    """Class to represent a node in a binary tree."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """Class to represent the binary tree."""
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert a new node with the given data into the binary tree."""
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        """Helper method to insert data recursively."""
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)

    def in_order_traversal(self):
        """Perform an in-order traversal of the tree and print the data."""
        self._in_order_recursive(self.root)

    def _in_order_recursive(self, node):
        """Helper method to perform in-order traversal recursively."""
        if node is not None:
            self._in_order_recursive(node.left)
            print(node.data, end=" ")
            self._in_order_recursive(node.right)

# Example usage
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    print("In-order traversal of the binary tree:")
    tree.in_order_traversal()
