import math
from typing import Dict, Optional, Tuple


class Vertex:
    def __init__(self, key: int) -> None:
        self._id = key
        self.connected_to: Dict["Vertex", int] = {}
        self.visited = False

    def add_neighbor(self, nbr, weight=0) -> None:
        self.connected_to[nbr] = weight

    def get_connections(self) -> Tuple["Vertex"]:
        return tuple(self.connected_to.keys())

    def get_id(self) -> int:
        return self._id

    def __str__(self) -> str:
        return f"{self._id}"

    def __repr__(self) -> str:
        return self.__str__()


class Graph:
    def __init__(self) -> None:
        self.vertices_dict: Dict[int, Vertex] = {}
        self.num_vertices: int = 0

    def add_vertex(self, key: int):
        if id not in self.vertices_dict:
            self.num_vertices += 1
            new_vertex = Vertex(key)
            self.vertices_dict[key] = new_vertex
            return new_vertex
        raise ValueError(f"Vertex with key {key} already exists")

    def get_vertex(self, key: int) -> Optional[Vertex]:
        if key in self.vertices_dict:
            return self.vertices_dict[key]
        return None

    def get_vertices(self) -> tuple:
        return tuple(self.vertices_dict.keys())

    def add_edge(self, from_key: int, to_key: int, weight=0) -> None:
        if from_key not in self.vertices_dict:
            self.add_vertex(from_key)
        if to_key not in self.vertices_dict:
            self.add_vertex(to_key)
        self.vertices_dict[from_key].add_neighbor(self.vertices_dict[to_key], weight)

    def get_edge(self, from_key: int, to_key: int) -> int | None:
        if from_key not in self.vertices_dict or to_key not in self.vertices_dict:
            raise ValueError("Wrong key of vertex!")

        from_vertex = self.vertices_dict[from_key]
        to_vertex = self.vertices_dict[to_key]

        if to_vertex in from_vertex.get_connections():
            return from_vertex.connected_to[to_vertex]
        if from_vertex in to_vertex.get_connections():
            return to_vertex.connected_to[from_vertex]
        return 0

    def get_all_shortest_paths(self):
        distances_dict = {
            key: {vert_key: 0 if key == vert_key else math.inf for vert_key in self.vertices_dict}
            for key, vertex in self.vertices_dict.items()
        }

        for key in self.vertices_dict:
            vert_list = [(key, 0)]
            distances = {key: 0}

            while vert_list:
                vertex_key, distance = vert_list.pop(0)

                for neighbor in self.get_vertex(vertex_key).get_connections():
                    neighbor_key = neighbor.get_id()
                    weight = self.get_edge(vertex_key, neighbor_key)

                    new_distance = distance + weight
                    if new_distance < distances.get(neighbor_key, math.inf):
                        distances[neighbor_key] = new_distance
                        vert_list.append((neighbor_key, new_distance))

            for target, distance in distances.items():
                distances_dict[key][target] = distance

        return distances_dict

    def __iter__(self):
        return iter(self.vertices_dict.values())

    def __contains__(self, key: int):
        return key in self.vertices_dict

    def print_shortest_paths(self):
        print('Shortest paths in graph: ')
        for key, value in self.get_all_shortest_paths().items():
            print(f'From vertex {key} to: {value}')


if __name__ == "__main__":
    g = Graph()

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)
    g.print_shortest_paths()
    g_short_paths = g.get_all_shortest_paths()

    assert g_short_paths[5][5] == 0
    assert g_short_paths[4][0] == 1
    assert g_short_paths[4][5] == 3
    assert g_short_paths[0][4] == 10
    assert g_short_paths[5][3] == 10
    assert g_short_paths[1][5] == 16
    assert g_short_paths[1][0] == 21

    print("____________________________")
    ng = Graph()
    ng.add_edge(0, 1, 5)
    ng.add_edge(0, 2, 1)
    ng.add_edge(1, 2, 7)
    ng.add_edge(1, 3, 2)
    ng.add_edge(3, 1, 4)
    ng.add_edge(2, 0, 6)
    ng.add_edge(2, 3, 9)
    ng.add_edge(3, 0, 2)
    ng.add_edge(3, 4, 2)

    ng.print_shortest_paths()
    ng_short_paths = ng.get_all_shortest_paths()

    assert ng_short_paths[3][3] == 0
    assert ng_short_paths[1][3] == 2
    assert ng_short_paths[3][1] == 4
    assert ng_short_paths[2][1] == 11
    assert ng_short_paths[2][0] == 6
    assert ng_short_paths[0][3] == 7
    assert ng_short_paths[3][4] == 2
    assert ng_short_paths[4][3] == math.inf
