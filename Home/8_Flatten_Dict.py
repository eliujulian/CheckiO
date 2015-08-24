def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            if isinstance(v, dict):
                stack.append((path + (k,), v))
            else:
                result["/".join((path + (k,)))] = v
        if not current:
            result["/".join(path)] = ""
    return result

if __name__ == '__main__':

    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}

    assert flatten({"outer":{"inner":{}}}) == {"outer/inner":""}
    assert flatten({"job":{"1":"scout","2":"worker","3":"writer","4":"reader","5":"learner"},"name":{"nick":{},"last":"Drone","first":"Second"},"recent":{"places":{"earth":{"NP":"","NY":"2017","Louvre":"2015"}},"times":{"XX":{"1964":"Yes"},"XXI":{"2064":"Nope"}}}}) == {"job/1":"scout","recent/places/earth/NY":"2017","job/3":"writer","job/2":"worker","job/5":"learner","job/4":"reader","recent/times/XXI/2064":"Nope","recent/places/earth/Louvre":"2015","recent/times/XX/1964":"Yes","recent/places/earth/NP":"","name/first":"Second","name/last":"Drone","name/nick":""}

