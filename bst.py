class BinarySearchTree():
    def __init__(self, value):
        self.parent = None
        self.left_node = None
        self.right_node = None
        self.value = value
        self.root = self

    def __str__(self):
        return self._BinarySearchTree__tree_walk_helper()


    def __tree_walk_helper(self):
        buffer = list()
        buffer.append(str(self.value))
        buffer.append("\n")
        if self.right_node:
            self.right_node._BinarySearchTree__tree_walk(buffer, "")
        if self.left_node:
            self.left_node._BinarySearchTree__tree_walk(buffer, "")
        return "".join(buffer)


    def __tree_walk(self, buffer, vbranch):
        buffer.append(vbranch)
        buffer.append("├──" if self.parent.right_node is self and self.parent.left_node else "└──")
        buffer.append(str(self.value))
        buffer.append("\n")

        vbranch += "|  " if self.parent.right_node is self and self.parent.left_node else "   "

        if self.right_node:
            self.right_node._BinarySearchTree__tree_walk(buffer, "" + vbranch)
        if self.left_node:
            self.left_node._BinarySearchTree__tree_walk(buffer, "" + vbranch)
        return "".join(buffer)


    def insert(self, new_value):
        new_node = BinarySearchTree(new_value)
        parent = None
        current = self.root
        while current is not None:
            parent = current
            if new_node.value <= current.value:
                current = current.left_node
            else:
                current = current.right_node

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.value <= parent.value:
            parent.left_node = new_node
        else:
            parent.right_node = new_node

        return new_node

    def search(self, value):
        if self.value == value:
            return self
        elif self.left_node and self.value >= value:
            return self.left_node.search(value)
        elif self.right_node:
            return self.right_node.search(value)
        else:
            return None


    def delete(self, node):
        if node is None:
            return

        if node.left_node is None or node.right_node is None:
            parent = node
        else:
            parent = node._BinarySearchTree__successor()

        if parent.left_node:
            current = parent.left_node
        else:
            current = parent.right_node

        if current:
            current.parent = parent.parent

        if parent.parent is None:
            self.root = current
        elif parent == parent.parent.left_node:
            parent.parent.left_node = current
        else:
            parent.parent.right_node = current

        if parent is not node:
            node.value = parent.value

        return parent


    def __min(self):
        min_node = self
        while min_node.left_node:
            min_node = min_node.left_node
        return min_node


    def __successor(self):
        if self.right_node:
            return self.right_node._BinarySearchTree__min()
        parent = self.parent
        current = self
        while parent and current == parent.right_node:
            current = parent
            parent = parent.parent
        return parent