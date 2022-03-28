"""
Create virtual environment and install Faker package only for this venv.
Write command line tool which will receive int as a first argument and one or more named arguments
 and generates defined number of dicts separated by new line.
Exec format:
`$python task_4.py NUMBER --FIELD=PROVIDER [--FIELD=PROVIDER...]`
where:
NUMBER - positive number of generated instances
FIELD - key used in generated dict
PROVIDER - name of Faker provider
Example:
`$python task_4.py 2 --fake-address=address --some_name=name`
{"some_name": "Chad Baird", "fake-address": "62323 Hobbs Green\nMaryshire, WY 48636"}
{"some_name": "Courtney Duncan", "fake-address": "8107 Nicole Orchard Suite 762\nJosephchester, WI 05981"}
"""

import argparse
from faker import Faker
from typing import Dict, List


def print_name_address(args: argparse.Namespace) -> None:
    fake = Faker()
    ans = vars(args)
    number: int = ans['NUMBER']
    for _ in range(number):
        name_address_dict: Dict[str: str] = dict()
        for item in ans['FIELD-PROVIDER']:
            key_value: List[str] = item.split('=')
            key: str = key_value[0]
            value: str = key_value[1]
            name_address_dict[key] = getattr(fake, value)()
        print(name_address_dict)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('NUMBER', type=int, help='positive number of generated instances')
    parser.add_argument('FIELD-PROVIDER', nargs='+', metavar='KEY=VALUE')
    print_name_address(parser.parse_args())

"""
Write test for print_name_address function
Use Mock for mocking args argument a
Example:
    >>> m = Mock()
    >>> m.method.return_value = 123
    >>> m.method()
    123
"""
