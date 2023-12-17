from typing import Dict, List, Optional, Tuple


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

    def __iter__(self):
        return iter(self.vertices_dict.values())

    def __contains__(self, key: int):
        return key in self.vertices_dict

    def depth_first_search(self, start_key: int, stack: List[Vertex]):
        start_vertex = self.vertices_dict[start_key]
        self.vertices_dict[start_key].visited = True

        for neighbor in start_vertex.connected_to.keys():
            if not neighbor.visited:
                self.depth_first_search(neighbor.get_id(), stack)

        stack.append(start_vertex)

    def transpose(self):
        transposed_graph = Graph()

        for key in self.vertices_dict:
            transposed_graph.add_vertex(key)

        for key, vertex in self.vertices_dict.items():
            for neighbor in vertex.connected_to:
                transposed_graph.add_edge(neighbor.get_id(), key)

        return transposed_graph

    def get_strongly_connected_components(self) -> List[List[int]]:
        stack = []
        scc_list = []

        for key, vertex in self.vertices_dict.items():
            if not vertex.visited:
                self.depth_first_search(key, stack)

        transposed_graph = self.transpose()

        for key, vertex in self.vertices_dict.items():
            vertex.visited = False

        while stack:
            current_vertex = stack.pop()
            helper_scc_list = []

            if not current_vertex.visited:
                transposed_graph.depth_first_search(
                    current_vertex.get_id(), helper_scc_list
                )
                new_group = [
                    vertex for vertex in helper_scc_list if len(helper_scc_list) > 1
                ]
                if new_group:
                    scc_list.append(new_group)

        return scc_list

    def print_connections(self):
        for _, vertex in self.vertices_dict.items():
            for neighbor in vertex.get_connections():
                print(f"(from: {vertex.get_id()}, to: {neighbor.get_id()})")

    def print_scc(self):
        print("SCC in graph: ")
        for group in self.get_strongly_connected_components():
            print(" ".join(map(str, group)))


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
    g.print_connections()
    g.print_scc()
    print("____________________________")
    ng = Graph()
    ng.add_edge(1, 2)
    ng.add_edge(2, 3)
    ng.add_edge(2, 5)
    ng.add_edge(3, 6)
    ng.add_edge(4, 2)
    ng.add_edge(4, 7)
    ng.add_edge(5, 1)
    ng.add_edge(5, 4)
    ng.add_edge(6, 8)
    ng.add_edge(7, 5)
    ng.add_edge(8, 9)
    ng.add_edge(9, 6)
    ng.print_connections()
    ng.print_scc()
