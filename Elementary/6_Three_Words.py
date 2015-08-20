def checkio(words):
    words += " "
    single_words = []
    start = 0
    counter = 0
    for n in words:
        counter += 1
        if n == " ":
            single_words.append(words[start:counter-1])
            start = counter
    another_counter = 0
    for x in single_words:
        if x.isalpha():
            another_counter += 1
            if another_counter == 3:
                return True
        elif x.isalnum():
            another_counter = 0
    return False



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"


# words.split() would be better for separating