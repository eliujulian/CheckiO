def min_max(*args, **kwargs):
    key = kwargs.get("key", None)
    min_or_max = kwargs.get("min_max")
    result = compare = None

    print(type(args[0]))

    if not isinstance(args[0], (int, float)) and len(args) == 1:
        args = args[0]

    if key is None:
        for item in args:
            if result is None:
                result = item
            if min_or_max == "min" and item < result:
                result = item
            if min_or_max == "max" and item > result:
                result = item
    else:
        args = [(key(n), n) for n in args]
        for key, value in args:
            if result is None:
                result = value
                compare = key
            if min_or_max == "min" and key < compare:
                result = value
                compare = key
            if min_or_max == "max" and key > compare:
                result = value
                compare = key
    print(result)
    return result


def min(*args, **kwargs):
    return min_max(*args, min_max="min", **kwargs)

def max(*args, **kwargs):
    return min_max(*args, min_max="max", **kwargs)


if __name__ == '__main__':
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    assert min((9,)) == 9, "Test 2"
    assert max(range(6))
    assert min(abs(i) for i in range(-10, 10)) == 0
    assert max([1, 2, 3], [5, 6], [7], [0, 0, 0, 1]) == [7]
