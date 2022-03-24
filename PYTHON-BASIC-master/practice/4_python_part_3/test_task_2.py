from task_2 import math_calculate, OperationNotFoundException
import pytest


def test_correct_functions():
    assert math_calculate('log', 1024, 2) == 10.0
    assert math_calculate('pow', 2, 3) == 8.0
    assert math_calculate('ceil', 10.7) == 11


def test_incorrect_functions_names(capfd):
    try:
        math_calculate('test', 1)
    except OperationNotFoundException:
        print('caught incorrect function name')
    out, err = capfd.readouterr()
    assert out == 'caught incorrect function name\n'

