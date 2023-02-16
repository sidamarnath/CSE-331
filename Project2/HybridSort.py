"""
Your Name: Sidharth Amarnath
Project 2 - Hybrid Sorting
CSE 331 Fall 2021
Professor Sebnem Onsay
"""
import random
from typing import TypeVar, List, Callable, Tuple, Dict

T = TypeVar("T")  # represents generic type


def merge_sort(data: List[T], threshold: int = 0,
               comparator: Callable[[T, T], bool] = lambda x, y: x <= y) -> int:
    """
    Given a dictionary of data, threshold, and comparator calculate the inversion count
    :param data: List of items to be sorted
    :param threshold: int at which insertion sort should be used
    :param comparator: function which takes in two arguments
     and returns true / false if condition is true
    Returns: inversion count -> int
    """
    inv_count = 0
    data_len = len(data)
    if data_len < 2:
        return inv_count
    mid = data_len // 2
    left_arr = data[0:mid]
    right_arr = data[mid:data_len]
    if threshold <= len(left_arr) and threshold <= len(right_arr):
        inv_count += merge_sort(left_arr, threshold, comparator)
        inv_count += merge_sort(right_arr, threshold, comparator)
        inv_count += merge(left_arr, right_arr, data, mid, comparator)
    else:
        insertion_sort(data, comparator)
        return 0

    if threshold > 0:
        return 0

    return inv_count


def merge(left_arr, right_arr, data, mid, comparator: Callable[[T, T], bool] = lambda x, y: x <= y):
    i = j = 0
    inv_count = 0
    while i + j < len(data):
        if j == len(right_arr) or (i < len(left_arr) and comparator(left_arr[i], right_arr[j])):
            data[i + j] = left_arr[i]
            i = i + 1
        else:
            data[i + j] = right_arr[j]
            j = j + 1
            inv_count += mid - i

    return inv_count


def insertion_sort(data: List[T], comparator: Callable[[T, T], bool] = lambda x, y: x <= y) -> None:
    """
    Given a dictionary of data and comparator, calculates sorted list and returns none
    :param data: List of items to be sorted
    :param comparator: function which takes in two arguments
     and returns true / false if condition is true
    Returns: None
    """
    idx_length = range(1, len(data))
    for i in idx_length:
        value_to_sort = data[i]

        while i > 0 and comparator(value_to_sort, data[i - 1]):
            data[i], data[i - 1] = data[i - 1], data[i]
            i -= 1

    return None


def hybrid_sort(data: List[T], threshold: int,
                comparator: Callable[[T, T], bool] = lambda x, y: x <= y) -> None:
    """
    Given a dictionary of data, threshold, and comparator, calculates sorted list and returns none
    Calls merge sort function
    :param data: List of items to be sorted
    :param threshold: Point at which insertion_sort is used
    :param comparator: function which takes in two arguments
     and returns true / false if condition is true
    Returns: None
    """

    merge_sort(data, threshold, comparator)


def inversions_count(data: List[T]) -> int:
    """
    Given a dictionary of data and comparator, calculates
     inversion count with function call to merge sort
    Calls merge sort after copying data
    Calls merge sort function
    :param data: List of items to be sorted
    :param threshold: Point at which insertion_sort is used
    :param comparator: function which takes in two arguments
     and returns true / false if condition is true
    Returns: invserion count -> int
    """
    temp_list = data.copy()
    return merge_sort(temp_list)


def reverse_sort(data: List[T], threshold: int) -> None:
    """
    Given a dictionary of data, threshold, calculates sort
     in reverse with function call to merge sort
    Calls merge sort after copying data
    Calls merge sort function
    :param data: List of items to be sorted
    :param threshold: Point at which insertion_sort is used
    :param comparator: function which takes in two arguments
    and returns true / false if condition is true
    Returns: None
    """
    merge_sort(data, threshold, comparator=lambda x, y: x > y)


# forward reference
Ship = TypeVar('Ship')

# DO NOT MODIFY THIS CLASS
class Ship:
    """
    A class representation of a ship
    """

    __slots__ = ['name', 'x', 'y']

    def __init__(self, name: str, x: int, y: int) -> None:
        """
        Constructs a ship object
        :param name: name of the ship
        :param x: x coordinate of the ship
        :param y: y coordinate of the ship
        """
        self.x, self.y = x, y
        self.name = name

    def __str__(self):
        """
        :return: string representation of the ship
        """
        return "Ship: " + self.name + " x=" + str(self.x) + " y=" + str(self.y)

    __repr__ = __str__

    def __eq__(self, other):
        """
        :return: bool if two ships are equivalent
        """
        return self.x == other.x and self.y == other.y and self.name == other.name

    def __hash__(self):
        """
        Allows Ship to be used as a key in a dictionary (pretty cool, right?)
        :return: hash of string representation of the ship
        """
        return hash(str(self))

    def euclidean_distance(self, other: Ship) -> float:
        """
        returns the euclidean distance between `self` and `other`
        :return: float
        """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** .5

    def taxicab_distance(self, other: Ship) -> float:
        """
        returns the taxicab distance between `self` and `other`
        :return: float
        """
        return abs(self.x - other.x) + abs(self.y - other.y)


# MODIFY BELOW
def navigation_test(ships: Dict[Ship, List[Ship]], euclidean: bool = True) -> List[Ship]:
    """
    Given a dictionary of data, and a boolean value, returns
     the list of ships in order of mistakes
    Calls merge sort after copying data
    Calls merge sort function
    :param data: List of items to be sorted
    :param threshold: Point at which insertion_sort is used
    :param comparator: function which takes in two arguments
     and returns true / false if condition is true
    Returns: invserion count -> int
    """
    final_ships_list = []

    if not ships:
        return final_ships_list
    list_of_ships = list(ships)
    if len(list_of_ships) == 1:
        final_ships_list.append(list_of_ships[0])
        return final_ships_list

    for main_ship, nearby_ships in ships.items():
        distance_list = []
        for each in nearby_ships:
            if euclidean is True:
                distance = main_ship.euclidean_distance(each)
            else:
                distance = main_ship.taxicab_distance(each)
            distance_list.append(distance)
        mistakes = inversions_count(distance_list)
        final_ships_list.append(tuple((main_ship, mistakes)))

    # done calculating mistakes for each ship in dictionary, now sort
    # Define a custom comparator that does that. It should return true if the first ship has less mistakes,
    # or equal mistakes and less a name which comes first alphabetically
    comp_one = lambda x, y: x[1] < y[1] or (x[1] == y[1] and x[0].name <= y[0].name)
    merge_sort(final_ships_list, 0, comp_one)
    ret_list = []
    for idx in final_ships_list:
        ret_list.append(idx[0])

    return ret_list


