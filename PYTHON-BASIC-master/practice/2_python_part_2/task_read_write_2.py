"""
Use function 'generate_words' to generate random words.
Write them to a new file encoded in UTF-8. Separator - '\n'.
Write second file encoded in CP1252, reverse words order. Separator - ','.

Example:
    Input: ['abc', 'def', 'xyz']

    Output:
        file1.txt (content: "abc\ndef\nxyz", encoding: UTF-8)
        file2.txt (content: "xyz,def,abc", encoding: CP1252)
"""
import os
from typing import List


def generate_words(n=20):
    import string
    import random

    words: List[str] = list()
    for _ in range(n):
        word: str = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words


def write_first_file(dirpath: str, words_number: int) -> List[str]:
    content: List[str] = generate_words(words_number)
    filepath: str = os.path.join(dirpath, 'file1.txt')
    with open(filepath, encoding='UTF-8', mode='w') as f:
        f.write('\n'.join(content))
    return content


def write_second_file(dirpath: str, content: List[str]) -> None:
    reversed_content: List[str] = content[::-1]
    filepath: str = os.path.join(dirpath, 'file2.txt')
    with open(filepath, encoding='cp1252', mode='w') as f:
        f.write(','.join(reversed_content))


if __name__ == '__main__':
    dirpath: str = os.environ.get('path')
    content_list: List[str] = write_first_file(dirpath, 5)
    write_second_file(dirpath, content_list)
