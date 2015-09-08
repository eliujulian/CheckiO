def letter_queue(commands):
    queue = []
    for c in commands:
        if c.startswith("PUSH"):
            queue.append(c[-1])
        elif queue:
            queue.remove(queue[0])
    return ''.join(queue)

if __name__ == '__main__':
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
