FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def end_digit_needed(num):
    if num % 100 > 9 and num % 100 < 20:
        return SECOND_TEN[num % 100 - 10]
    elif num % 10 != 0:
        return FIRST_TEN[num % 10 - 1]
    else:
        return ""

def dec_needed(num):
    dec = (num % 100) // 10
    if dec > 1:
        return OTHER_TENS[dec-2]
    else:
        return ""

def hundreds(num):
    if num > 99:
        return FIRST_TEN[num // 100 - 1] + " " + HUNDRED
    else:
        return ""

def checkio(number):
    result = hundreds(number) + " " + dec_needed(number) + " " + end_digit_needed(number)
    return result.rstrip().lstrip().replace("  ", " ")

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"

