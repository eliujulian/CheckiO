horizontal_axis = "xabcdefghx"

def safe_pawns(pawns):
    if not pawns:
        return 0
    result = 0
    for pawn in pawns:
        position = (horizontal_axis.index(pawn[0]),int(pawn[1]))
        brother = horizontal_axis[position[0]-1]+str(position[1]-1)
        sister = horizontal_axis[position[0]+1]+str(position[1]-1)
        if brother in pawns or sister in pawns:
            result += 1
    return result



if __name__ == '__main__':
    assert safe_pawns({}) == 0
    assert safe_pawns({"c3"}) == 0
    assert safe_pawns({"c3"}) == 0
    assert safe_pawns({"a2", "b2"}) == 0
    assert safe_pawns({"a2", "b3"}) == 1
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns({"a8", "b1"}) == 0
    assert safe_pawns({"a1","b2","c3","d4","e5","f6","g7","h8"}) == 7

