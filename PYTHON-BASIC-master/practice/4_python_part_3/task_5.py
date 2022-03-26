"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8

"""
from typing import Tuple
from urllib.request import urlopen
from urllib import response


def make_request(url: str) -> Tuple[int, str]:
    resp: response = urlopen(url)
    response_code: int = int(resp.getcode())
    response_data: str = resp.read().decode('utf-8')
    return response_code, response_data


"""
Write test for make_request function
Use Mock for mocking request with urlopen https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 200
    >>> m.method2.return_value = b'some text'
    >>> m.method()
    200
    >>> m.method2()
    b'some text'
"""
