from bst import BinarySearchTree

class AlternatingBinarySearchTree(BinarySearchTree):
    def __init__(self, value):
        super().__init__(value)
        self.preferLeft = True

    def insert(self, new_value):
        new_node = AlternatingBinarySearchTree(new_value)
        parent = None
        current = self.root
        while current is not None:
            current.preferLeft = not current.preferLeft
            parent = current
            if new_node.value == current.value:
                current = current.left_node if parent.preferLeft else parent.right_node
            elif new_node.value < current.value:
                current = current.left_node
            else:
                current = current.right_node

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.value == parent.value:
            if parent.preferLeft:
                parent.left_node = new_node
            else:
                parent.right_node = new_node
        elif new_node.value < parent.value:
            parent.left_node = new_node
        else:
            parent.right_node = new_node

        return new_node
