"""
using datetime module find number of days from custom date to now
Custom date is a string with format "2021-12-24"
If entered string pattern does not match, raise a custom Exception
If entered date is from future, return negative value for number of days
"""
from datetime import datetime, timedelta


class WrongFormatException(Exception):
    def __init__(self, message='Entered wrong date format'):
        self.message = message
        super().__init__(self.message)


def calculate_days(from_date: str) -> int:
    try:
        now_date: datetime = datetime.now()
        entered_date: datetime = datetime.fromisoformat(from_date)
        days_difference: int = (now_date - entered_date).days
        return days_difference
    except ValueError:
        raise WrongFormatException


"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""
