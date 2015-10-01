from unittest import TestCase


def checkio(numbers_array):
    return sorted(numbers_array, key=abs)


class Test(TestCase):
    def test_1(self):
        self.assertEqual([-5, 10, 15, -20], checkio((-20, -5, 10, 15)))
        self.assertEqual([0, 1, 2, 3], checkio((1, 2, 3, 0)))
        self.assertEqual([0, -1, -2, -3], checkio((-1, -2, -3, 0)))
