"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""

import os
import sys
from typing import List, Tuple


def parsing(listdir: List[str]) -> List[Tuple[str, int]]:
    tuple_list: List[Tuple[str, int]] = list()
    for item in listdir:
        try:
            number: int = int(item.split('_')[-1].split('.')[0])
            tuple_list.append((item, number))
        except ValueError:
            pass
    return tuple_list


def read_write_files(dirpath: str) -> None:
    content: List[str] = list()
    listdir: List[str] = os.listdir(dirpath)
    tuple_list: List[Tuple[str, int]] = parsing(listdir)
    sorted_tuple_list: List[Tuple[str, int]] = sorted(tuple_list, key=lambda x: x[1])
    for filename in sorted_tuple_list:
        filepath: str = os.path.join(dirpath, filename[0])
        with open(filepath, 'r') as f:
            content.append(*f.readlines())
    with open(os.path.join(dirpath, 'result.txt'), 'w') as f:
        f.write(', '.join(content))


if __name__ == "__main_":
    path: str = os.environ.get('path')
    read_write_files(path)
