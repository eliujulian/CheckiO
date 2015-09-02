"""
Will work better with zip()
"""

def checkio(data):
    data_t = [[0] * len(data) for _ in range(len(data[0]))]

    for row in range(len(data_t)):
        for col in range(len(data_t[0])):
            data_t[row][col] = data[col][row]

    return data_t


from unittest import TestCase


class TestCheckiO(TestCase):
    def test_type(self):
        self.assertIsInstance((checkio([[0]]).pop()), list)

    def test_1(self):
        self.assertEqual([[1, 4, 7], [2, 5, 8], [3, 6, 9]], checkio([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_2(self):
        self.assertEqual([[1, 4, 7], [2, 5, 8], [3, 6, 9]], checkio([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_3(self):
        self.assertEqual([[1, 8, 7, 4, 7], [4, 2, 8, 9, 8], [3, 6, 3, 6, 1]], checkio([[1, 4, 3], [8, 2, 6], [7, 8, 3], [4, 9, 6], [7, 8, 1]]))

