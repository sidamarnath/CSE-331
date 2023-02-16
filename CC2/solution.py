"""
CC2
Name: Sidharth Amarnath
"""

from typing import List


def solar_power(heights: List[int]) -> int:
    """
    Insert docstring here. See CC1 for an example docstring.
    """

    max_area = 0
    stack = []
    for i, data in enumerate(heights):
        start = i
        while stack and stack[-1][1] > data:
            index, height = stack.pop()
            area = height * (i - index)

            if area > max_area:
                max_area = area
            start = index
        stack.append((start, data))

    for i, data in stack:
        area = data * (len(heights) - i)
        if area > max_area:
            max_area = area

    return max_area
