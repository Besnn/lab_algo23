from bst import BinarySearchTree
from bst_bool import AlternatingBinarySearchTree
from bst_lg import ListGroupedBinarySearchTree
from test_utils import *

import sys

sys.setrecursionlimit(99999)

if __name__ == '__main__':
    max_value = 0
    root_value = 0
#######################################################±#######################
# Test 1: ~0.1% of values are duplicates
###############################################################################
    max_value = 9999
    size = 5000
    root_value = max_value//2

    roberto = \
    BinarySearchTree(root_value)
    alberto = AlternatingBinarySearchTree(root_value)
    umberto = ListGroupedBinarySearchTree(root_value)

    for i in \
        SyntheticData. \
        generate_integer_list(size, max_value):
        roberto.insert(i)
        alberto.insert(i)
        umberto.insert(i)
    #
    # print(roberto)
    # print(alberto)
    # print(umberto)
    output = str(roberto.get_height()) + " " + \
            str(alberto.get_height()) + " " + \
            str(umberto.get_height())

    print(output)
    Export.export_values_to_file(output)