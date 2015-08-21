def checkio(expression):
    b = "([{}])"
    x = ""
    for n in expression:
        if n in b:
            x += n
    if x.count(b[0]) != x.count(b[5]) or x.count(b[1]) != x.count(b[4]) or x.count(b[2]) != x.count(b[3]):
        return False
    if b[0]+b[3] in x or b[0]+b[4] in x or b[1]+b[3] in x or b[1]+b[5] in x or b[2]+b[4] in x or b[2]+b[5] in x:
        return False
    return True

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("([)]") == False, "false overlap"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"


