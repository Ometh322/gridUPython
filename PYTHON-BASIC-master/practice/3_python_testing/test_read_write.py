"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import unittest
import tempfile
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../2_python_part_2'))
from task_read_write import read_write_files


class TestingReadWrite(unittest.TestCase):
    def test_correct(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            with open(os.path.join(tmpdirname, 'file_1.txt'), 'w') as f:
                f.write('23')
            with open(os.path.join(tmpdirname, 'file_2.txt'), 'w') as f:
                f.write('78')
            with open(os.path.join(tmpdirname, 'file_3.txt'), 'w') as f:
                f.write('3')
            read_write_files(tmpdirname)
            with open(os.path.join(tmpdirname, 'result.txt'), 'r') as f:
                content: str = f.read()
                self.assertEqual(content, '23, 78, 3')

    def test_empty_content(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            with open(os.path.join(tmpdirname, 'file_1.txt'), 'w') as f:
                f.write('')
            with self.assertRaises(TypeError):
                read_write_files(tmpdirname)

    def test_without_files(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            read_write_files(tmpdirname)
            with open(os.path.join(tmpdirname, 'result.txt'), 'r') as f:
                content: str = f.read()
                self.assertEqual(content, '')


if __name__ == '__main__':
    unittest.main()
