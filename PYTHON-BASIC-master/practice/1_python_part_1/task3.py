"""
Write function which receives list of text lines (which is space separated words) and word number.
It should enumerate unique words from each line and then build string from all words of given number.
Restriction: word_number >= 0
Examples:
    >>> build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1)
    'b 2 dog'
    >>> build_from_unique_words('a b c', '', 'cat dog milk', word_number=0)
    'a cat'
    >>> build_from_unique_words('1 2', '1 2 3', word_number=10)
    ''
    >>> build_from_unique_words(word_number=10)
    ''
"""
from typing import Iterable, Set, List


def build_from_unique_words(*lines: Iterable[str], word_number: int) -> str:
    result: List[str] = list()
    for line in lines:
        tmp_set: Set[str] = set()
        tmp_list: List[str] = list()
        for item in str(line).split(' '):
            if (item not in tmp_set) and item:
                tmp_list.append(item)
                tmp_set.add(item)
        if len(tmp_list) > word_number:
            result.append(str(tmp_list[word_number]))
    return ' '.join(result)
