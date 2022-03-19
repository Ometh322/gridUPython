"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]
"""
from typing import List


def calculate_power_with_difference(ints: List[int]) -> List[int]:
    tmp: int = 0
    result_list: List[int] = list()
    for item in ints:
        result_list.append(item ** 2 - (tmp ** 2 - tmp))
        tmp = item
    return result_list
