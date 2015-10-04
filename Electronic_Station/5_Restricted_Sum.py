def add_up(data):
    try:
        data[1] += data[0]
        data.remove(data[0])
        return add_up(data)
    except:
        return data

def checkio(data):
    result = add_up(data)
    return result[0]

print(checkio([1, 2, 3]))