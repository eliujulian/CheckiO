"""
diagonal needs refactor
"""
from unittest import TestCase

def checkio(matrix):

    for n in range(1, 10):

        pattern = str(n) * 4

        # Rows and Cols
        for row in matrix:
            if pattern in ''.join([str(m) for m in row]):
                return True
        for col in zip(*matrix):
            if pattern in ''.join([str(m) for m in col]):
                return True

        # Diagonals
        diagonal_matrix = [[] for _ in range(len(matrix))]
        for n in range(len(matrix)):
            for i in range(n + 1):
                diagonal_matrix[n].append(matrix[i][n-i])
        for r in diagonal_matrix:
            if pattern in ''.join([str(m) for m in r]):
                return True

        matrix2 = matrix[::-1]
        diagonal_matrix2 = [[] for _ in range(len(matrix))]
        for n in range(len(matrix)):
            for i in range(n + 1):
                diagonal_matrix2[n].append(matrix2[i][n-i])
        for r in diagonal_matrix2:
            if pattern in ''.join([str(m) for m in r]):
                return True

        matrix3 = [row[::-1] for row in matrix]
        diagonal_matrix3 = [[] for _ in range(len(matrix))]
        for n in range(len(matrix)):
            for i in range(n + 1):
                diagonal_matrix3[n].append(matrix3[i][n-i])
        for r in diagonal_matrix3:
            if pattern in ''.join([str(m) for m in r]):
                return True

        matrix4 = [row[::-1] for row in matrix2]
        diagonal_matrix4 = [[] for _ in range(len(matrix))]
        for n in range(len(matrix)):
            for i in range(n + 1):
                diagonal_matrix4[n].append(matrix4[i][n-i])
        for r in diagonal_matrix4:
            if pattern in ''.join([str(m) for m in r]):
                return True

    return False


class Test(TestCase):
    def test_vertical(self):
        self.assertTrue(checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]))

    def test_nothing_there(self):
        self.assertFalse(checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
            ]))

    def test_long_hoirzontal(self):
        self.assertTrue(checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]))

    def test_diagonal(self):
        self.assertTrue(checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]))

    def test_eight(self):
        self.assertFalse(checkio([[2,7,6,2,1,5,2,8,4,4],[8,7,5,8,9,2,8,9,5,5],[5,7,7,7,4,1,1,2,6,8],[4,6,6,3,2,7,6,6,5,1],[2,6,6,9,8,5,5,6,7,7],[9,4,1,9,1,3,7,2,3,1],[5,1,4,3,6,5,9,3,4,1],[6,5,5,1,7,7,8,2,1,1],[9,5,7,8,2,9,2,6,9,3],[8,2,5,7,3,7,3,8,6,2]]))

