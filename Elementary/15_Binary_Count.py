from unittest import TestCase


def checkio(number):
    return bin(number).count("1")


class Test(TestCase):
    def test_1(self):
        self.assertEqual(1, checkio(4))

    def test_2(self):
        self.assertEqual(4, checkio(15))
        self.assertEqual(1, checkio(1))
        self.assertEqual(9, checkio(1022))
