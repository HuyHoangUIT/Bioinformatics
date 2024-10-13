from collections import defaultdict

class DirectedGraph:
    
    def __init__(self, adjacency_list):
        self.graph = defaultdict(list)
        for vertex, neighbors in adjacency_list.items():
            self.graph[vertex] = neighbors

    def without_vertex(self, vertex):
        new_graph = self.graph.copy()
        del new_graph[vertex]
        for neighbors in new_graph.values():
            if vertex in neighbors:
                neighbors.remove(vertex)
        return DirectedGraph(new_graph)
 
    def sources(self):
        all_vertices = set(self.graph.keys())
        all_neighbors = set(neighbor for neighbors in self.graph.values() for neighbor in neighbors)
        return all_vertices - all_neighbors
    
    def number_of_topological_sortings(self):
        if not self.graph:
            return 1
        else:
            return sum(self.without_vertex(source).number_of_topological_sortings()
                       for source in self.sources())

# Example usage:

graph = {
    'tights': ['leotard', 'boots'],
    'leotard': ['shorts','cape','gloves'],
    'shorts': ['boots','belt'],
    'boots': [],
    'cape': ['hood'],
    'gloves': [],
    'belt':[],
    'hood':[]
}

dg = DirectedGraph(graph)

result = dg.number_of_topological_sortings()

print(result)