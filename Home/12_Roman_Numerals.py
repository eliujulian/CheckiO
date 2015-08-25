"""
Symbol Value
I 1 (unus)
V 5 (quinque)
X 10 (decem)
L 50 (quinquaginta)
C 100 (centum)
D 500 (quingenti)
M 1,000 (mille)
"""
def checkio(data):
    result = ""
    if data > 999:
        result += "M" * (data // 1000)
        data -= (data // 1000) * 1000
    if data > 899:
        result += "CM"
        data -= 900
    if data > 499:
        result += "D" * (data // 500)
        data -= (data // 500) * 500
    if data > 399:
        result += "CD"
        data -= 400
    if data > 99:
        result += "C" * (data // 100)
        data -= (data // 100) * 100
    if data > 89:
        result += "XC"
        data -= 90
    if data > 49:
        result += "L"
        data -= 50
    if data > 39:
        result += "XL"
        data -= 40
    if data > 9:
        result += "X" * (data // 10)
        data -= (data // 10) * 10
    if data == 9:
        result += "IX"
        data -= 9
    if data > 4:
        result += "V"
        data -= 5
    if data == 4:
        result += "IV"
        data -= 4
    if data > 0:
        result += "I" * data
    return result

if __name__ == '__main__':
    assert checkio(1) == 'I', '1'
    assert checkio(2) == 'II', '2'
    assert checkio(3) == 'III', '3'
    assert checkio(4) == 'IV', '4'
    assert checkio(5) == 'V', '5'
    assert checkio(6) == 'VI', '6'
    assert checkio(7) == 'VII', '7'
    assert checkio(8) == 'VIII', '8'
    assert checkio(9) == 'IX', '9'
    assert checkio(10) == 'X', '10'
    assert checkio(19) == 'XIX', '19'
    assert checkio(20) == 'XX', '20'
    assert checkio(50) == 'L', '50'
    assert checkio(51) == 'LI', '51'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(400) == 'CD', '400'
    assert checkio(700) == 'DCC', '700'
    assert checkio(999) == 'CMXCIX', '999'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
