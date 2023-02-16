# CC6 FS 2021
# Jacob Caurdy, Alexander Woodring, Jordyn Rosario
# Problem: Create a deepcopy of a graph given a node of the graph
# Return: Copy of the node given which points to a copy
# of the rest of the graph (through adjacency's)

from typing import TypeVar, List, Tuple

T = TypeVar('T')
NecklaceNode = TypeVar('NecklaceNode')  # NecklaceNode Class Instance


class NecklaceNode:
    """ Class representing a Necklace Bead which can be connected with other Nodes to form a necklace"""

    __slots__ = ['adj', 'value']

    def __init__(self, val: T, adj: List[T] = [], adj_V: List[NecklaceNode] = None) -> None:
        """
            DO NOT MODIFY
            Initializes a NecklaceNode
            :param val: Value of the NecklaceNode
            :param adj: List of adjacent necklace nodes
            """
        self.value = val
        if adj:
            # adjacency list (list of neighbor vertices)
            self.adj = [NecklaceNode(value) for value in adj]
        elif adj_V:
            self.adj = adj_V
        else:
            self.adj = []

    def __repr__(self) -> str:
        """
        DO NOT MODIFY
        :return: string representing NecklaceNode object
        """
        if self.adj:
            lst = [f"{n.value}" for n in self.adj]
        else:
            lst = []

        return f"<val: '{self.value}'" + ", Adjacencies: " + ",".join(lst) + ">"

    def __str__(self) -> str:
        """
        DO NOT MODIFY
        :return: string representing NecklaceNode object
        """
        return repr(self)


def ReplicateNecklace(start: NecklaceNode) -> NecklaceNode:
    """
    param NecklaceNode: Node: Starting point of necklace
    Returns: Node: NecklaceNode containing starting point of necklace after replicated
    """
    if not start:
        return None

    queue = [start]
    root = NecklaceNode(start.value)

    hash_map = {}
    hash_map[start] = root

    while queue:
        current = queue.pop(0)
        if current.adj:
            for neighbor in current.adj:
                if neighbor not in hash_map:
                    new_node = NecklaceNode(neighbor.value)
                    hash_map[neighbor] = new_node
                    queue.append(neighbor)
                    #if neighbor:
                hash_map[current].adj.append(hash_map[neighbor])

    return root
