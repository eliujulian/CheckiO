from unittest import TestCase


def checkio(teleports_string):
    vertices = [int(n) for n in sorted(list(set(teleports_string))) if n.isalnum()]
    graph = [(int(x), int(y)) for x, y in teleports_string.split(",")]

    current_verstice = vertices[0]
    dead_ends = []
    path = [current_verstice]

    while True:
        if set([n for n in path]) == {1, 2, 3, 4, 5, 6, 7, 8} and path[-1] == 1:  # Checking result
            break

        connecting_edges = list(set([n for n in graph if n[0] == current_verstice] +
                                    [n for n in graph if n[1] == current_verstice]))
        adjacent_vertices = set([y for x in connecting_edges for y in x])
        all_possible_path = [(v, path[:] + [v]) for v in adjacent_vertices]
        vertices_to_be_removed = [v for v, w in all_possible_path if w in dead_ends]

        for x in connecting_edges.copy():
            if x[0] in vertices_to_be_removed or x[1] in vertices_to_be_removed:
                connecting_edges.remove(x)

        if len(connecting_edges):  # Moving forward
            current_edge = connecting_edges[0]

            if current_edge[0] == current_verstice:
                new_verstice = current_edge[1]
            elif current_edge[1] == current_verstice:
                new_verstice = current_edge[0]

            if current_edge in graph:
                graph.remove(current_edge)
            elif (current_edge[1], current_edge[0]) in graph:
                graph.remove((current_edge[1], current_edge[0]))

            path.append(new_verstice)
            current_verstice = new_verstice

        else:  # Dead-End, moving backwards
            graph.append((path[-1], path[-2]))
            dead_ends.append(path[:])
            current_verstice = path[-2]
            path.pop()

        adjacent_vertices.clear()
        connecting_edges.clear()
        all_possible_path.clear()

    return ''.join([str(n) for n in path])


def check_solution(func, teleports_str):
    route = func(teleports_str)
    teleports_map = [tuple(sorted([int(x), int(y)])) for x, y in teleports_str.split(",")]
    if route[0] != '1' or route[-1] != '1':
        print("The path must start and end at 1")
        return False
    ch_route = route[0]
    for i in range(len(route) - 1):
        teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
        if teleport not in teleports_map:
            print("No way from {0} to {1}".format(route[i], route[i + 1]))
            return False
        teleports_map.remove(teleport)
        ch_route += route[i + 1]
    for s in range(1, 9):
        if not str(s) in ch_route:
            print("You forgot about {0}".format(s))
            return False
    return True


class TestCheckio(TestCase):
    def test_first(self):
        self.assertTrue(check_solution(checkio, "12,23,34,45,56,67,78,81"))

    def test_second(self):
        self.assertTrue(check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"))

    def test_third(self):
        self.assertTrue(check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"))

    def test_fourth(self):
        self.assertTrue(check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"))

    def test_five(self):
        self.assertTrue(check_solution(checkio, "12,13,14,15,16,17,18,82,83,84,85,86,87"))

    def test_six(self):
        self.assertTrue(check_solution(checkio, "12,17,87,86,85,82,65,43,35,46"))

    def test_seven(self):
        self.assertTrue(check_solution(checkio, "13,14,34,32,35,52,37,38,78,16,26"))

    def test_eight(self):
        self.assertTrue(check_solution(checkio, "12,23,36,68,85,57,74,41,38,62,25"))

    def test_nine(self):
        self.assertTrue(check_solution(checkio, "13,37,78,82,26,64,45,51,75,27,34,36,25,35,17,48,47"))

    def test_ten(self):
        self.assertTrue(check_solution(checkio, "18,84,47,76,62,23,35,51,87,65,38,41,75"))

    def test_eleven(self):
        self.assertTrue(check_solution(checkio, "18,84,43,36,62,25,57,71,16,56,85"))

    def test_twelve(self):
        self.assertTrue(check_solution(checkio, "16,64,45,53,38,87,72,21,74,52,15,73"))

    def test_extra_one(self):
        self.assertTrue(check_solution(checkio, "18,85,53,37,76,62,24,41,48,36,82,13"))

    def test_extra_two(self):
        self.assertTrue(check_solution(checkio, "13,34,48,85,52,26,67,71,45,63,42,78,16,51"))

    def test_extra_three(self):
        self.assertTrue(check_solution(checkio, "14,47,73,38,85,52,26,61,67,45,57,86,51,71"))

    def test_extra_four(self):
        self.assertTrue(check_solution(checkio, "16,67,74,42,25,58,83,31,57,46,26,37"))
