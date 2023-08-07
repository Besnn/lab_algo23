from bst import BinarySearchTree
from bst_bool import AlternatingBinarySearchTree
from bst_multiset import MultisetBinarySearchTree
from mock import Mock

if __name__ == '__main__':
    umberto = MultisetBinarySearchTree(50)
    alberto = AlternatingBinarySearchTree(50)
    roberto = BinarySearchTree(50)

    for i in Mock.generate_integer_list(20, 100):
        if i > 50:
            umberto.insert(81)
            roberto.insert(81)
            alberto.insert(81)
        umberto.insert(i)
        roberto.insert(i)
        alberto.insert(i)

    # print(str(bonsai))
    print(umberto)
    print(alberto)
    print(roberto)