"""
Write function which executes custom operation from math module
for given arguments.
Restrition: math function could take 1 or 2 arguments
If given operation does not exists, raise OperationNotFoundException
Examples:
"""
import math


class OperationNotFoundException(Exception):
    def __init__(self, message):
        self.message = message + ' function not found in math module'
        super().__init__(self.message)


def math_calculate(function: str, *args):
    try:
        result = getattr(math, function)(*args)
        return result
    except AttributeError:
        raise OperationNotFoundException(function)


"""
Write tests for math_calculate function
"""