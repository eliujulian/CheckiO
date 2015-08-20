from unittest import TestCase

def checkio(game_result):
    for n in range(3):
        game_result.append(game_result[0][n] + game_result[1][n] + game_result[2][n])
    game_result.append(game_result[0][0] + game_result[1][1] + game_result[2][2])
    game_result.append(game_result[2][0] + game_result[1][1] + game_result[0][2])
    for n in game_result:
        if n == "XXX":
            return "X"
        elif n == "OOO":
            return "O"
    return "D"


class TestTTT(TestCase):
    def test_X_wins(self):
        self.assertEqual("X", checkio([
        "X.O",
        "XX.",
        "XOO"]))

    def test_empty(self):
        self.assertEqual("D", checkio(["...","...","..."]))

    def test_O_wins(self):
        self.assertEqual("O", checkio([
        "OO.",
        "XOX",
        "XOX"]))

    def test_Draw(self):
        self.assertEqual("D", checkio([
        "OOX",
        "XXO",
        "OXX"]))

    def test_Quer(self):
        self.assertEqual("X", checkio([
        "O.X",
        "XX.",
        "XOO"]))

"""
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
"""