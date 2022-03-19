"""
Write function which receives filename and reads file line by line and returns min and mix integer from file.
Restriction: filename always valid, each line of file contains valid integer value
Examples:
    # file contains following lines:
        10
        -2
        0
        34
    >>> get_min_max('filename.txt')
    (-2, 34)

Hint:
To read file line-by-line you can use this:
with open(filename) as opened_file:
    for line in opened_file:
        ...
"""
from typing import Tuple, List


def get_min_max(filename: str) -> Tuple[int, int]:
    with open(filename, 'r') as f:
        a: List[str] = f.readlines()
        a: List[int] = list(map(int, a))
    min_value: int = a[1]
    max_value: int = a[1]
    for item in a:
        if item > max_value:
            max_value = item
        elif item < min_value:
            min_value = item
    return min_value, max_value


