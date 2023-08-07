from bst import BinarySearchTree

class MultisetBinarySearchTree(BinarySearchTree):
    def __init__(self, value):
        super().__init__(value)
        self.duplicates = None
    def insert(self, new_value):
        new_node = MultisetBinarySearchTree(new_value)
        parent = None
        current = self.root
        while current is not None:
            parent = current
            if new_node.value == current.value:
                if current.duplicates is None:
                    current.duplicates = [current.value]
                else:
                    current.duplicates.append(new_node.value)
                return new_node
            elif new_node.value < current.value:
                current = current.left_node
            else:
                current = current.right_node

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left_node = new_node
        else:
            parent.right_node = new_node

        return new_node

    def __str__(self):
        return self._MultisetBinarySearchTree__tree_walk_helper()

    def __tree_walk_helper(self):
        buffer = list()
        buffer.append(str(self.value) + ("[-]" if self.duplicates is None
                                         else "[" + str(len(self.duplicates)) + "]"))
        buffer.append("\n")
        if self.right_node:
            self.right_node._MultisetBinarySearchTree__tree_walk(buffer, "")
        if self.left_node:
            self.left_node._MultisetBinarySearchTree__tree_walk(buffer, "")
        return "".join(buffer)


    def __tree_walk(self, buffer, vbranch):
        buffer.append(vbranch)
        buffer.append("├──" if self.parent.right_node is self and self.parent.left_node else "└──")
        buffer.append(str(self.value) + ("[-]" if self.duplicates is None
                                         else "[" + str(len(self.duplicates)) + "]"))
        buffer.append("\n")

        vbranch += "|  " if self.parent.right_node is self and self.parent.left_node else "   "

        if self.right_node:
            self.right_node._MultisetBinarySearchTree__tree_walk(buffer, "" + vbranch)
        if self.left_node:
            self.left_node._MultisetBinarySearchTree__tree_walk(buffer, "" + vbranch)
        return "".join(buffer)