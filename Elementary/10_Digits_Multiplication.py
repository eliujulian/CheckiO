def checkio(number):
    result = 1
    for n in str(number):
        if int(n) != 0:
            result *= int(n)
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1) == 1
    assert checkio(12) == 2
    assert checkio(101) == 1
    assert checkio(1111) == 1
    assert checkio(99) == 81