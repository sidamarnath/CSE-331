from __future__ import annotations
from typing import List
import math

class Node:
    """Node that contains value, index and left and right pointers."""
    def __init__(self, val: int, left: Node = None, right: Node = None, index: int = 0):
        self.val = val
        self.index = index
        self.left = left
        self.right = right


def inorder(root, ret_val_list, ret_ind_list) -> List[int]:
    if root is None:
        return []

    inorder(root.left, ret_val_list, ret_ind_list)

    if root is not None:
        ret_val_list.append(root.val)
        ret_ind_list.append(root.index)

    inorder(root.right, ret_val_list, ret_ind_list)

    return ret_val_list, ret_ind_list


def smaller_product(root: Node) -> List[int]:
    """
     Calculates the smaller product of a node.
     :param root: root node of tree.
     :return: List of smaller products.
     """
    ret_val_list = []
    ret_ind_list = []
    new_ret = []
    if root is None:
        return new_ret
    if root.left is None and root.right is None:
        new_ret.insert(0, None)
        return new_ret

    ret_val_list, ret_ind_list = inorder(root, ret_val_list, ret_ind_list)
    new_ret = [0] * len(ret_val_list)

    num = len(ret_val_list)

    prd = 0
    j = 0
    i = 0

    for i in range(num):
        if i == 0:
            new_ret[ret_ind_list[j]] = None
        if i == 1:
            new_ret[ret_ind_list[j]] = ret_val_list[i-1]

        if i > 1:
            prd = math.prod(ret_val_list[:i])
            new_ret[ret_ind_list[j]] = prd

        i += 1
        j += 1

    return new_ret









