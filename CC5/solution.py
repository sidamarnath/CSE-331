"""
CC5 Student Submission
Name: Sidharth Amarnath
"""

from typing import List, Tuple


def scooter_rentals(times: List[Tuple[int, int]]) -> int:
    """
    Calculates the minimum number of scooters needed to satisfy demand
    given points.
    :param times: list of tuples containing time intervals.
    :return: Minimum number of scooters needed -> int.
    """
    if len(times) == 0:
        return 0
    if len(times) == 1:
        return 1




