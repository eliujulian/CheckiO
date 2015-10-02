def checkio(array):
    if len(array) == 0:
        return 0
    return sum([n for i, n in enumerate(array) if i % 2 == 0]) * array[-1]


if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
