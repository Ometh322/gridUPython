"""
Write function which executes custom operation from math module
for given arguments.
Restrition: math function could take 1 or 2 arguments
If given operation does not exists, raise OperationNotFoundException
Examples:
     >>> math_calculate('log', 1024, 2)
     10.0
     >>> math_calculate('ceil', 10.7)
     11
"""
import math


class OperationNotFoundException(Exception):
    def __init__(self, message='Operation not found'):
        self.message = message
        super().__init__(self.message)


def math_calculate(function: str, *args):
    func_dict: dict = {
        "log": math.log,
        "ceil": math.ceil,
        "pow": math.pow,
        "acos": math.acos,
        "acosh": math.acosh,
        "asin": math.asin,
        "asinh": math.asinh,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "atan2": math.atan2,

    }
    return func_dict[function](*args)


"""
Write tests for math_calculate function
"""
