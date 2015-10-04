from unittest import TestCase

def checkio(n, m):
    b_n, b_m = bin(n)[2:], bin(m)[2:]
    if len(b_m) > len(b_n):
        b_n, b_m = b_m, b_n
    if len(b_m) < len(b_n):
        b_m = "0" * (len(b_n) - len(b_m)) + b_m
    return sum([1 for n in range(len(b_n)) if b_n[n] != b_m[n]])


class Test(TestCase):
    def test_1(self):
        self.assertEqual(3, checkio(117, 17))

    def test_2(self):
        self.assertEqual(2, checkio(1, 2))

    def test_3(self):
        self.assertEqual(5, checkio(16, 15))
