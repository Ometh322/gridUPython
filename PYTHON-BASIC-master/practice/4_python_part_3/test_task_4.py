import unittest
from unittest import mock
from task_4 import print_name_address
import argparse
from faker import Faker


@mock.patch('task_4.argparse._sys.argv', ['python3', '1', 'some_name=name'])
@mock.patch("task_4.fake.name()", return_value='Test', create=True)
def test_name_address_correct(mock_fake, capfd):
    parser = argparse.ArgumentParser()
    parser.add_argument('NUMBER', type=int, help='positive number of generated instances')
    parser.add_argument('FIELD-PROVIDER', nargs='+', metavar='KEY=VALUE')
    out, err = capfd.readouterr()
    print_name_address(parser.parse_args())
    assert out == "{'some_name': 'Test'}"