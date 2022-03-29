from task_5 import make_request
import pytest
import unittest
from unittest.mock import Mock, patch, MagicMock
from urllib import request, response
from typing import Tuple


class TestUrlOpening(unittest.TestCase):
    @patch('task_5.urlopen')
    def test_correct_response(self, mock_urlopen):
        cm = MagicMock()
        cm.getcode.return_value = 200
        cm.read.return_value = b'Some data'
        cm.__enter__.return_value = cm
        mock_urlopen.return_value = cm

        resp: Tuple[int, str] = make_request('https://google.com')
        self.assertEqual(200, resp[0])
        self.assertEqual('Some data', resp[1])


if __name__ == '__main__':
    unittest.main()
