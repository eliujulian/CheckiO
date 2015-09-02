"""
Sofia has given you a schedule and two dates and told you she needs help planning her weekends. She has asked you to count each day of rest (Saturday and Sunday) starting from the initial date to final date. You should count the initial and final dates if they fall on a Saturday or Sunday.
The dates are given as datetime.date (Read about this module here). The result is an integer.
Input: Start and end date as datetime.date.
Output: The quantity of the rest days as an integer.
Precondition: start_date < end_date.
"""

from datetime import date


def checkio(from_date, to_date):
    result = 0
    while from_date != date.fromordinal(to_date.toordinal() + 1):
        if from_date.weekday() > 4:
            result += 1
        from_date = date.fromordinal(from_date.toordinal() + 1)
    return result


from unittest import TestCase


class TestCheckio(TestCase):
    def test_checkio(self):
        self.assertEqual(2, checkio(date(2013, 9, 18), date(2013, 9, 23)))

    def test_checkio_2(self):
        self.assertEqual(8, checkio(date(2013, 1, 1), date(2013, 2, 1)))

    def test_checkio_3(self):
        self.assertEqual(2, checkio(date(2013, 2, 2), date(2013, 2, 3)))
