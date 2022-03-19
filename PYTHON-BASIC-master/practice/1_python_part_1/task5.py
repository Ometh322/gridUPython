"""
Write function which receives line of space sepparated words.
Remove all duplicated words from line.
Restriction:
Examples:
    >>> remove_duplicated_words('cat cat dog 1 dog 2')
    'cat dog 1 2'
    >>> remove_duplicated_words('cat cat cat')
    'cat'
    >>> remove_duplicated_words('1 2 3')
    '1 2 3'
"""
from typing import List, Set


def remove_duplicated_words(line: str) -> str:
    tmp_set: Set[str] = set()
    result_str: List[str] = list()
    for item in line.split(' '):
        if item not in tmp_set:
            tmp_set.add(item)
            result_str.append(item)
    return ' '.join(result_str)

