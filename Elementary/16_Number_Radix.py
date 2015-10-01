"""
Do you remember the radix and Numeral systems from math class? Let's practice with it.
You are given a positive number as a string along with the radix for it. Your function should convert it into decimal form. The radix is less than 37 and greater than 1. The task uses digits and the letters A-Z for the strings.
Watch out for cases when the number cannot be converted. For example: "1A" cannot be converted with radix 9. For these cases your function should return -1.
Input: Two arguments. A number as string and a radix as an integer.
Output: The converted number as an integer.
Precondition:
re.match("\A[A-Z0-9]\Z", str_number)
0 < len(str_number) ? 10
2 ? radix ? 36
"""

from unittest import TestCase


def checkio(str_number, radix):
    try:
        return int(str_number, base=radix)
    except:
        return -1


class Test(TestCase):
    def test_1(self):
        self.assertEqual(175, checkio("AF", 16))
        self.assertEqual(5, checkio("101", 2))
        self.assertEqual(26, checkio("101", 5))
        self.assertEqual(35, checkio("Z", 36))
        self.assertEqual(-1, checkio("AB", 10))
