class Node:
    """Class to represent a node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    """Class to represent the stack using a singly linked list."""
    def __init__(self):
        self.top = None

    def push(self, data):
        """Push a new node with the given data onto the stack."""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Remove and return the top node from the stack. Return None if the stack is empty."""
        if self.top is None:
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def peek(self):
        """Return the data of the top node without removing it. Return None if the stack is empty."""
        if self.top is None:
            return None
        return self.top.data

    def empty(self):
        """Return True if the stack is empty, otherwise return False."""
        return self.top is None

# Example usage
if __name__ == "__main__":
    stack = Stack()
    print("Is stack empty?", stack.empty())  # True
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Top element:", stack.peek())  # 30
    print("Popped element:", stack.pop())  # 30
    print("Top element after pop:", stack.peek())  # 20
    print("Is stack empty?", stack.empty())  # False
