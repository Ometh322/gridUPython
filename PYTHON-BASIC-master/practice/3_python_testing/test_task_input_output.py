"""
Write tests for a read_numbers function.
It should check successful and failed cases
for example:
Test if user inputs: 1, 2, 3, 4
Test if user inputs: 1, 2, Text

Tip: for passing custom values to the input() function
Use unittest.mock patch function
https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

TIP: for testing builtin input() function create another function which return input() and mock returned value
"""
from unittest.mock import patch, Mock
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../2_python_part_2'))
from task_input_output import read_numbers


@patch("task_input_output.input", side_effect=['1', '2', '3', '4'])
def test_read_numbers_without_text_input(mock_input, capfd):
    print(read_numbers(4))
    out, err = capfd.readouterr()
    assert out == 'Avg: 2.5\n'


@patch("task_input_output.input", side_effect=['1', '2', 'Text'])
def test_read_numbers_with_text_input(mock_input, capfd):
    print(read_numbers(3))
    out, err = capfd.readouterr()
    assert out == 'Avg: 1.5\n'


@patch("task_input_output.input", side_effect=['Text', 'Test'])
def test_read_number_without_numbers(mock_input, capfd):
    print(read_numbers(2))
    out, err = capfd.readouterr()
    assert out == 'No numbers entered\n'
