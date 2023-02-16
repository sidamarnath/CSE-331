"""
CC7
Name: Sidharth Amarnath
"""

from typing import Dict, List

class PerkGraph:
    """
    DO NOT MODIFY
    Implementation of a perk tree
    """
    def __init__(self):
        """
        DO NOT MODIFY
        Initializes a PerkGraph
        :return: None
        """
        self.graph = {}  # Dictionary containing adjacency List
        self.vertices = set()  # Set of vertices

    def add_edge(self, first, second) -> None:
        """
        DO NOT MODIFY
        Adds an edge to a PerkGraph
        :param first: First vertex
        :param second: Second vertex
        :return: None
        """
        if first not in self.vertices:
            self.vertices.add(first)
            self.graph[first] = []
        if second not in self.vertices:
            self.vertices.add(second)
            self.graph[second] = []
        self.graph[first].append(second)

    def perk_organizer(self, vertex: str, visited: Dict[str, bool], stack: List[str], target: str) -> bool:
        """
        ** OPTIONAL UTILITY FUNCTION **
        REPLACE
        Be sure to include :param: and :return: fields!
        See CC1 or Project 1 for examples of proper docstrings.
        """
        pass

    def perk_traversal(self, target: str, points: int = float("inf")) -> List[str]:
        """
        :param self: PerkGraph given.
        :param target: string indicates the desired perk.
        :param points: int indicating points available.
        :return: List representing an order of perks.
        """
        if len(self.graph) == 0:
            return []

        in_degree = {}
        for i in self.graph:
            in_degree[i] = 0

        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        queue = []
        for k in self.graph:
            if in_degree[k] == 0:
                queue.append(k)

        top_order = []

        while queue:
            at = queue.pop(0)
            top_order.append(at)
            for ldx in self.graph[at]:
                in_degree[ldx] = in_degree[ldx] - 1
                if in_degree[ldx] == 0:
                    queue.append(ldx)

        final_list = []
        for i in top_order:
            final_list.append(i)
            if i == target:
                break
        if len(final_list) <= points:
            return final_list

        return []
