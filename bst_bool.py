from bst import BinarySearchTree

class AlternatingBinarySearchTree(BinarySearchTree):
    def __init__(self, value):
        super().__init__(value)
        self.preferLeft = False

    def __tree_walk_helper(self):
        buffer = list()
        buffer.append(str(self.value))
        buffer.append("\n")
        if self.right_node:
            self.right_node._AlternatingBinarySearchTree__tree_walk(buffer, "")
        if self.left_node:
            self.left_node._AlternatingBinarySearchTree__tree_walk(buffer, "")
        return "".join(buffer)

    def __tree_walk(self, buffer, vbranch):
        buffer.append(vbranch)
        buffer.append("├──" if self.parent.right_node is self and self.parent.left_node else "└──")
        buffer.append(str(self.value))
        buffer.append("\n")

        vbranch += "|  " if self.parent.right_node is self and self.parent.left_node else "   "

        if self.right_node:
            print("right")
            self.right_node._BinarySearchTree__tree_walk(buffer, vbranch)
        if self.left_node:
            print("left")
            self.left_node._BinarySearchTree__tree_walk(buffer, vbranch)
        return "".join(buffer)