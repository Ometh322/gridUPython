from task_3 import is_http_domain
import pytest


@pytest.mark.parametrize('test_input, expected', [('http://google.com', True), ('https://vk.com/', True)])
def test_correct_domains(test_input, expected):
    assert is_http_domain(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [('google.com', False), ('https://vk.com//', False), ('hhttps://vk.com/', False)])
def test_incorrect_domains(test_input, expected):
    assert is_http_domain(test_input) == expected