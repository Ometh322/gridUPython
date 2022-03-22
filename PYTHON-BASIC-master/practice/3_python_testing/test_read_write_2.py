
"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import unittest
import tempfile
import os
import sys
from typing import List
sys.path.insert(1, os.path.join(sys.path[0], '../2_python_part_2'))
from task_read_write_2 import write_first_file, write_second_file


class TestingReadWritePartTwo(unittest.TestCase):
    def test_correct(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            content: List[str] = write_first_file(tmpdirname, 5)
            with open(os.path.join(tmpdirname, 'file1.txt'), encoding='UTF-8', mode='r') as f:
                self.assertEqual('\n'.join(content), f.read())
            write_second_file(tmpdirname, content)
            with open(os.path.join(tmpdirname, 'file2.txt'), encoding='CP1252', mode='r') as f:
                reversed_content: List[str] = content[::-1]
                self.assertEqual(','.join(reversed_content), f.read())

    def test_empty_content(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            content: List[str] = write_first_file(tmpdirname, 0)
            with open(os.path.join(tmpdirname, 'file1.txt'), encoding='UTF-8', mode='r') as f:
                self.assertEqual('', f.read())
            write_second_file(tmpdirname, content)
            with open(os.path.join(tmpdirname, 'file2.txt'), encoding='CP1252', mode='r') as f:
                reversed_content: List[str] = content[::-1]
                self.assertEqual(''.join(reversed_content), f.read())

    def test_negative_content_len(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            content: List[str] = write_first_file(tmpdirname, -10)
            with open(os.path.join(tmpdirname, 'file1.txt'), encoding='UTF-8', mode='r') as f:
                self.assertEqual('', f.read())
            write_second_file(tmpdirname, content)
            with open(os.path.join(tmpdirname, 'file2.txt'), encoding='CP1252', mode='r') as f:
                reversed_content: List[str] = content[::-1]
                self.assertEqual(''.join(reversed_content), f.read())

    def test_type_error(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            with self.assertRaises(TypeError):
                content: List[str] = write_first_file(tmpdirname, 'abc')


if __name__ == '__main__':
    unittest.main()
