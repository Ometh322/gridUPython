from task_1 import calculate_days, WrongFormatException
import pytest


@pytest.mark.freeze_time('2022-03-24')
def test_correct_negative_days():
    assert calculate_days('2022-03-25') == -1


@pytest.mark.freeze_time('2022-03-24')
def test_correct_positive_days():
    assert calculate_days('2022-03-23') == 1


@pytest.mark.freeze_time('2022-03-24')
def test_correct_zero_days():
    assert calculate_days('2022-03-24') == 0


@pytest.mark.freeze_time('2022-03-24')
def test_exception(capfd):
    try:
        calculate_days('03-03-2222')
    except WrongFormatException:
        print('caught wrong format exception')
    out, err = capfd.readouterr()
    assert out == 'caught wrong format exception\n'
