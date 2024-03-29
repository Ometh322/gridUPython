"""
Write function which reads a number from input nth times.
If an entered value isn't a number, ignore it.
After all inputs are entered, calculate an average entered number.
Return string with following format:
If average exists, return: "Avg: X", where X is avg value which rounded to 2 places after the decimal
If it doesn't exists, return: "No numbers entered"
Examples:
    user enters: 1, 2, hello, 2, world
    >>> read_numbers(5)
    'Avg: 1.67'

    user enters: hello, world, foo, bar, baz
    >>> read_numbers(5)
    'No numbers entered'

"""


def read_numbers(n: int) -> str:
    s: int = 0
    counter: int = 0
    for i in range(n):
        try:
            cur = input()
            if int(cur):
                s += int(cur)
                counter += 1
        except ValueError:
            pass

    if counter > 0:
        x: float = round(s / counter, 2)
        return f'Avg: {x}'
    else:
        return 'No numbers entered'
