"""
Project 3
CSE 331 F21 (Onsay)
Your Name: Sidharth Amarnath
AVLTree.py
"""

import queue
from typing import TypeVar, Generator, List, Tuple

# for more information on typehinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")  # represents generic type
Node = TypeVar("Node")  # represents a Node object (forward-declare to use in Node __init__)
AVLWrappedDictionary = TypeVar("AVLWrappedDictionary")  # represents a custom type used in application


####################################################################################################


class Node:
    """
    Implementation of an AVL tree node.
    Do not modify.
    """
    # preallocate storage: see https://stackoverflow.com/questions/472000/usage-of-slots
    __slots__ = ["value", "parent", "left", "right", "height"]

    def __init__(self, value: T, parent: Node = None,
                 left: Node = None, right: Node = None) -> None:
        """
        Construct an AVL tree node.

        :param value: value held by the node object
        :param parent: ref to parent node of which this node is a child
        :param left: ref to left child node of this node
        :param right: ref to right child node of this node
        """
        self.value = value
        self.parent, self.left, self.right = parent, left, right
        self.height = 0

    def __repr__(self) -> str:
        """
        Represent the AVL tree node as a string.

        :return: string representation of the node.
        """
        return f"<{str(self.value)}>"

    def __str__(self) -> str:
        """
        Represent the AVL tree node as a string.

        :return: string representation of the node.
        """
        return f"<{str(self.value)}>"


####################################################################################################


class AVLTree:
    """
    Implementation of an AVL tree.
    Modify only below indicated line.
    """
    # preallocate storage: see https://stackoverflow.com/questions/472000/usage-of-slots
    __slots__ = ["origin", "size"]

    def __init__(self) -> None:
        """
        Construct an empty AVL tree.
        """
        self.origin = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the AVL tree as a string. Inspired by Anna De Biasi (Fall'20 Lead TA).

        :return: string representation of the AVL tree
        """
        if self.origin is None:
            return "Empty AVL Tree"

        # initialize helpers for tree traversal
        root = self.origin
        result = ""
        q = queue.SimpleQueue()
        levels = {}
        q.put((root, 0, root.parent))
        for i in range(self.origin.height + 1):
            levels[i] = []

        # traverse tree to get node representations
        while not q.empty():
            node, level, parent = q.get()
            if level > self.origin.height:
                break
            levels[level].append((node, level, parent))

            if node is None:
                q.put((None, level + 1, None))
                q.put((None, level + 1, None))
                continue

            if node.left:
                q.put((node.left, level + 1, node))
            else:
                q.put((None, level + 1, None))

            if node.right:
                q.put((node.right, level + 1, node))
            else:
                q.put((None, level + 1, None))

        # construct tree using traversal
        spaces = pow(2, self.origin.height) * 12
        result += "\n"
        result += f"AVL Tree: size = {self.size}, height = {self.origin.height}".center(spaces)
        result += "\n\n"
        for i in range(self.origin.height + 1):
            result += f"Level {i}: "
            for node, level, parent in levels[i]:
                level = pow(2, i)
                space = int(round(spaces / level))
                if node is None:
                    result += " " * space
                    continue
                result += f"{node}".center(space, " ")
            result += "\n"
        return result

    def __str__(self) -> str:
        """
        Represent the AVL tree as a string. Inspired by Anna De Biasi (Fall'20 Lead TA).

        :return: string representation of the AVL tree
        """
        return repr(self)

    def height(self, root: Node) -> int:
        """
        Return height of a subtree in the AVL tree, properly handling the case of root = None.
        Recall that the height of an empty subtree is -1.

        :param root: root node of subtree to be measured
        :return: height of subtree rooted at `root` parameter
        """
        return root.height if root is not None else -1

    def left_rotate(self, root: Node) -> Node:
        """
        We are giving you the implementation of left rotate, use this to write right rotate ;)
        Perform a left rotation on the subtree rooted at `root`. Return new subtree root.

        :param root: root node of unbalanced subtree to be rotated.
        :return: new root node of subtree following rotation.
        """

        if root is None:
            return None

        # pull right child up and shift right-left child across tree, update parent
        new_root, rl_child = root.right, root.right.left
        root.right = rl_child
        if rl_child is not None:
            rl_child.parent = root

        # right child has been pulled up to new root -> push old root down left, update parent
        new_root.left = root
        new_root.parent = root.parent
        if root.parent is not None:
            if root is root.parent.left:
                root.parent.left = new_root
            else:
                root.parent.right = new_root
        root.parent = new_root

        # handle tree origin case
        if root is self.origin:
            self.origin = new_root

        # update heights and return new root of subtree
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))
        return new_root

    ########################################
    # Implement functions below this line. #
    ########################################

    def right_rotate(self, root: Node) -> Node:
        """
        This function will be implemented during live class activity!
        Come to class to learn about it :) Oct 28th live class,
        in case you can't and you do  not want to
        you can easily look at rotate left function and use symmetry as your friend to complete
        rotate right this..
        You don't really need that much help to complete it.
        """
        if root is None:
            return None

        # pull right child up and shift right-left child across tree, update parent
        new_root, lr_child = root.left, root.left.right
        root.left = lr_child
        if lr_child is not None:
            lr_child.parent = root

        # right child has been pulled up to new root -> push old root down left, update parent
        new_root.right = root
        new_root.parent = root.parent
        if root.parent is not None:
            if root is root.parent.right:
                root.parent.right = new_root
            else:
                root.parent.left = new_root
        root.parent = new_root

        # handle tree origin case
        if root is self.origin:
            self.origin = new_root

        # update heights and return new root of subtree
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))
        return new_root

    def balance_factor(self, root: Node) -> int:
        """
        param root: Node: The root Node of the subtree on which to compute the balance factor.
        Returns: int representing the balance factor of root
        """
        if root is None:
            return 0
        else:
            return self.height(root.left) - self.height(root.right)

    def rebalance(self, root: Node) -> Node:
        """
        param root: Node: Root node of tree to rebalance.
        Returns: root of the rebalanced tree
        """
        if self.balance_factor(root) == -2:
            if self.balance_factor(root.right) > 0:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
            else:
                return self.left_rotate(root)
        elif self.balance_factor(root) == 2:
            if self.balance_factor(root.left) < 0:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
            else:
                return self.right_rotate(root)
        else:
            return root

    def insert(self, root: Node, val: T) -> Node:
        """
        param root: Node: The root Node of the subtree on which to compute the balance factor.
        param val: value to be inserted into tree
        Returns: Node: root node of balanced subtree after insertion
        """
        if self.origin is None:
            self.origin = Node(val)
            self.size += 1
            return self.origin
        elif root is None:
            root = Node(val)
            self.size += 1
            return root
        elif root.value > val:
            root.left = self.insert(root.left, val)
        elif root.value == val:
            pass
        else:
            root.right = self.insert(root.right, val)
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        return self.rebalance(root)

    def min(self, root: Node) -> Node:
        """
        param root: Node: The root Node of the subtree in which to search for a minimum
        Returns: Node: object containing the smallest value in the subtree rooted at root
        """
        if root is None:
            return None
        if root.left is None:
            return root
        return self.min(root.left)

    def max(self, root: Node) -> Node:
        """
        param root: Node: The root Node of the subtree in which to search for a maximum
        Returns: Node: object containing the largest value in the subtree rooted at root
        """
        if root is None:
            return None
        if root.right is None:
            return root
        return self.max(root.right)

    def search(self, root: Node, val: T) -> Node:
        """
        param root: Node: The root Node of the subtree in which to search for val
        param val: The value being searched in the subtree rooted at root
        Returns: Node object containing val if it exists, else the Node object
        below which val would be inserted as a child
        """
        if root is None:
            return None
        elif val == root.value:
            return root  # Return potential parent
        elif val > root.value and root.right is not None:
            return self.search(root.right, val)
        elif val < root.value and root.left is not None:
            return self.search(root.left, val)
        return root

    def inorder(self, root: Node) -> Generator[Node, None, None]:
        """
        param root: Node: The root Node of the subtree currently being traversed
        Returns: Node: Generator object which yields Node objects only (no None-type yields).
        Once all nodes of the tree have been yielded, a StopIteration exception is raised
        """
        if root is not None:
            yield from self.inorder(root.left)
            yield root
            yield from self.inorder(root.right)

    def preorder(self, root: Node) -> Generator[Node, None, None]:
        """
        param root: Node: The root Node of the subtree currently being traversed
        Returns: Node: Generator object which yields Node objects only (no None-type yields).
        Once all nodes of the tree have been yielded, a StopIteration exception is raised
        """
        if root is not None:
            yield root
            yield from self.preorder(root.left)
            yield from self.preorder(root.right)

    def postorder(self, root: Node) -> Generator[Node, None, None]:
        """
        param root: Node: The root Node of the subtree currently being traversed
        Returns: Node: Generator object which yields Node objects only (no None-type yields).
        Once all nodes of the tree have been yielded, a StopIteration exception is raised
        """
        if root is not None:
            yield from self.postorder(root.left)
            yield from self.postorder(root.right)
            yield root

    def levelorder(self, root: Node) -> Generator[Node, None, None]:
        """
        param root: Node: The root Node of the subtree currently being traversed
        Returns: Node: Generator object which yields Node objects only (no None-type yields).
        Once all nodes of the tree have been yielded, a StopIteration exception is raised
        """
        if root is None:
            return None
        q = queue.SimpleQueue()
        q.put(root)
        while not q.empty():
            temp = q.get()
            yield temp
            if temp.left:
                q.put(temp.left)
            if temp.right:
                q.put(temp.right)

    def remove(self, root: Node, val: T) -> Node:
        """
        We give you this function but you should understand its functionality for the exam!!!!
        Remove the node with `value` from the subtree rooted at `root` if it exists.
        Return the root node of the balanced subtree following removal.

        :param root: root node of subtree from which to remove.
        :param val: value to be removed from subtree.
        :return: root node of balanced subtree.
        """
        # handle empty and recursive left/right cases
        if root is None:
            return None
        elif val < root.value:
            root.left = self.remove(root.left, val)
        elif val > root.value:
            root.right = self.remove(root.right, val)
        else:
            # handle actual deletion step on this root
            if root.left is None:
                # pull up right child, set parent, decrease size, properly handle origin-reset
                if root is self.origin:
                    self.origin = root.right
                if root.right is not None:
                    root.right.parent = root.parent
                self.size -= 1
                return root.right
            elif root.right is None:
                # pull up left child, set parent, decrease size, properly handle origin-reset
                if root is self.origin:
                    self.origin = root.left
                if root.left is not None:
                    root.left.parent = root.parent
                self.size -= 1
                return root.left
            else:
                # two children: swap with predecessor and delete predecessor
                predecessor = self.max(root.left)
                root.value = predecessor.value
                root.left = self.remove(root.left, predecessor.value)

        # update height and rebalance every node that was traversed in recursive deletion
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        return self.rebalance(root)


################################## APPLICATION PROBLEM #############################################
####################################################################################################


class Employee(Node):
    "Represents an employee as a modified node"
    __slots__ = ["nominations", "total", "parent", "left", "right", "height"]

    def __init__(self, value: T, parent: Node = None,
                 left: Node = None, right: Node = None, nominations: int = 0, ):
        super().__init__(value, parent, left, right)
        self.nominations = nominations

    def __repr__(self) -> str:
        """
        Represent the Employee node as a string.

        :return: string representation of the node.
        """
        return f"({str(self.value)},{str(self.nominations)})"

    def __str__(self) -> str:
        """
        Represent the Employee node as a string.

        :return: string representation of the node.
        """
        return f"({str(self.value)}, {str(self.nominations)})"

    def __eq__(self, other) -> bool:
        return self.value == other.value and self.nominations == other.nominations


class Company:
    """Represents a company, implemented as a BST"""

    def __init__(self) -> None:
        self.ceo = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the AVL tree as a string. Inspired by Anna De Biasi (Fall'20 Lead TA).
        :return: string representation of the AVL tree
        """
        if self.ceo is None:
            return "Empty AVL Tree"

        # initialize helpers for tree traversal
        root = self.ceo
        result = ""
        q = queue.SimpleQueue()
        levels = {}
        q.put((root, 0, root.parent))
        for i in range(self.ceo.height + 1):
            levels[i] = []

        # traverse tree to get node representations
        while not q.empty():
            node, level, parent = q.get()
            if level > self.ceo.height:
                break
            levels[level].append((node, level, parent))

            if node is None:
                q.put((None, level + 1, None))
                q.put((None, level + 1, None))
                continue

            if node.left:
                q.put((node.left, level + 1, node))
            else:
                q.put((None, level + 1, None))

            if node.right:
                q.put((node.right, level + 1, node))
            else:
                q.put((None, level + 1, None))

        # construct tree using traversal
        spaces = pow(2, self.ceo.height) * 12
        result += "\n"
        result += f"Sum Tree: size = {self.size}, height = {self.ceo.height}".center(spaces)
        result += "\n\n"
        for i in range(self.ceo.height + 1):
            result += f"Level {i}: "
            for node, level, parent in levels[i]:
                level = pow(2, i)
                space = int(round(spaces / level))
                if node is None:
                    result += " " * space
                    continue
                result += f"{node}".center(space, " ")
            result += "\n"
        return result

    def __str__(self) -> str:
        """
        Represent the AVL tree as a string. Inspired by Anna De Biasi (Fall'20 Lead TA).
        :return: string representation of the AVL tree
        """
        return repr(self)

    def height(self, root: Employee) -> int:
        """
        Return height of a subtree in the AVL tree, properly handling the case of root = None.
        Recall that the height of an empty subtree is -1.
        :param root: root node of subtree to be measured
        :return: height of subtree rooted at `root` parameter
        """
        return root.height if root is not None else -1

    def insert(self, root: Employee, employee: Employee) -> Employee:
        if root is None:
            self.ceo = employee
            self.size = 1
            return self.ceo

        val = employee.value
        if val == root.value:
            return root

        if val > root.value:
            if root.right:
                self.insert(root.right, employee)
            else:
                root.right = employee
                self.size += 1
        else:
            if root.left:
                self.insert(root.left, employee)
            else:
                root.left = employee
                self.size += 1

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        return root


def findEmployeesOfTheMonth(ceo: Employee) -> List[Employee]:
    """
    param ceo: Node: An instance of the Employee class which has pointers to their 2 subordinates
    Returns: List: A list of employees who had the most nominations among all employees at their level (tree depth)
    """
    if not ceo:
        return []
    if not ceo.left and not ceo.right:
        return [ceo]

    largest_value_array = []
    result = []

    def bfs(node, level, largest_value_array):
        if not node:
            return
        if len(largest_value_array) == level:
            largest_value_array.append([])
        largest_value_array[level] .append(node)
        bfs(node.left, level + 1, largest_value_array)
        bfs(node.right, level + 1, largest_value_array)
    bfs(ceo, 0, largest_value_array)

    for val in largest_value_array:
        result.append(val)

    return result



############################ Extra Credit Only ############################

class NodeWithSum(Node):
    "Represents a node with sum of subtree that node is the root"
    __slots__ = ["sum", "total", "parent", "left", "right", "height"]

    def __init__(self, value: T, parent: Node = None,
                 left: Node = None, right: Node = None):
        super().__init__(value, parent, left, right)
        self.sum = value

    def __repr__(self) -> str:
        """
        Represent the Employee node as a string.

        :return: string representation of the node.
        """
        return f"({str(self.value)},{str(self.sum)})"

    def __str__(self) -> str:
        """
        Represent the Employee node as a string.

        :return: string representation of the node.
        """
        return f"({str(self.value)}, {str(self.sum)})"

    def __eq__(self, other) -> bool:
        return self.value == other.value and self.sum == other.sum


class TreeWithSum():
    """Represents a Tree, implemented as a BST"""

    __slots__ = ["origin", "size"]

    def __init__(self) -> None:
        """
        Construct an empty AVL tree.
        """
        self.origin = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the BST tree as a string. Inspired by Anna De Biasi (Fall'20 Lead TA).

        :return: string representation of the BST tree
        """
        if self.origin is None:
            return "Empty BST Tree"

        # initialize helpers for tree traversal
        root = self.origin
        result = ""
        q = queue.SimpleQueue()
        levels = {}
        q.put((root, 0, root.parent))
        for i in range(self.origin.height + 1):
            levels[i] = []

        # traverse tree to get node representations
        while not q.empty():
            node, level, parent = q.get()
            if level > self.origin.height:
                break
            levels[level].append((node, level, parent))

            if node is None:
                q.put((None, level + 1, None))
                q.put((None, level + 1, None))
                continue

            if node.left:
                q.put((node.left, level + 1, node))
            else:
                q.put((None, level + 1, None))

            if node.right:
                q.put((node.right, level + 1, node))
            else:
                q.put((None, level + 1, None))

        # construct tree using traversal
        spaces = pow(2, self.origin.height) * 12
        result += "\n"
        result += f"BST Tree: size = {self.size}, height = {self.origin.height}".center(spaces)
        result += "\n\n"
        for i in range(self.origin.height + 1):
            result += f"Level {i}: "
            for node, level, parent in levels[i]:
                level = pow(2, i)
                space = int(round(spaces / level))
                if node is None:
                    result += " " * space
                    continue
                result += f"{node}".center(space, " ")
            result += "\n"
        return result

    def __str__(self) -> str:
        """
        Represent the BST tree as a string. Inspired by Anna De Biasi (Fall'20 Lead TA).

        :return: string representation of the AVL tree
        """
        return repr(self)

    def height(self, root: Node) -> int:
        """
        Return height of a subtree in the BST tree, properly handling the case of root = None.
        Recall that the height of an empty subtree is -1.

        :param root: root node of subtree to be measured
        :return: height of subtree rooted at `root` parameter
        """
        return root.height if root is not None else -1

    def insert(self, root: NodeWithSum, val: T) -> NodeWithSum:
        """
        Insert a node with value into the BST
        :param root: root node of subtree in which to insert.
        :param val: value to be inserted in subtree.
        :return: root node of balanced subtree.
        """
        if root is None:
            self.origin = NodeWithSum(val)
            self.size = 1
            return self.origin

        if val == root.value:
            return root

        if val > root.value:
            if root.right:
                self.insert(root.right, val)
            else:
                root.right = NodeWithSum(val)
                self.size += 1
        else:
            if root.left:
                self.insert(root.left, val)
            else:
                root.left = NodeWithSum(val)
                self.size += 1

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        root.sum = root.value + self.subtree_sum(root.left) + self.subtree_sum(root.right)
        return root

    def subtree_sum(self, root: NodeWithSum) -> int:
        """
        Return the sum of all values in the subtree of root
        :param root: root that need to return sum
        :return: sum of subtree of root
        """
        return root.sum if root is not None else 0


def findSum(tree: TreeWithSum, rangeValues: Tuple[int, int]) -> int:
    """
    PLEASE FILL THIS DOCSTRING
    """
    pass

if __name__ == "__main__":
    pass
