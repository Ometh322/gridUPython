"""
Write tests for division() function in 2_python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""
import unittest
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../2_python_part_2'))
from task_exceptions import DivisionByOneException, division


def test_division_ok(capfd):
    ans: int = division(2, 2)
    out, err = capfd.readouterr()
    assert ans == 1
    assert out == 'Division finished\n'


def test_division_by_zero(capfd):
    ans: None = division(2, 0)
    out, err = capfd.readouterr()
    assert ans is None
    assert out == 'Division by 0\nDivision finished\n'


def test_division_by_one(capfd):
    try:
        division(1, 1)
    except DivisionByOneException:
        print('Deletion on 1 get the same result')
    out, err = capfd.readouterr()
    assert out == 'Division finished\nDeletion on 1 get the same result\n'
