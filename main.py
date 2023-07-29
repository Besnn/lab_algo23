from bst import *
from bst_bool import AlternatingBinarySearchTree
from mock import Mock

if __name__ == '__main__':
    bonsai = BinarySearchTree(21)
    bonsai.insert(44)
    bonsai.insert(2)
    print(bonsai)
    bonsai.insert(54)
    bonsai.insert(43)
    bonsai.insert(5)
    bonsai.insert(81)
    bonsai.insert(1)
    bonsai.insert(123)
    bonsai.insert(99)
    bonsai.insert(5)
    bonsai.insert(17)
    bonsai.insert(81)
    bonsai.insert(81)
    print(bonsai)
    print(bonsai.search(99))
    print(bonsai.insert(81))

    alberto = BinarySearchTree(50)
    roberto = AlternatingBinarySearchTree(50)

    for i in Mock.generate_integer_list(20, 100):
        if i > 50:
            roberto.insert(81)
        roberto.insert(i)

    for i in Mock.generate_integer_list(30, 100):
        alberto.insert(i)

    print(str(bonsai))
    print(alberto)
    print(roberto)