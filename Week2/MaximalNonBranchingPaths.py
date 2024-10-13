from collections import defaultdict

def MaximalNonBranchingPaths(graph):
    def is_1_in_1_out(v):
        return len(graph[v]) == 1 and in_degree[v] == 1
    
    paths = []
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    
    for v in graph:
        out_degree[v] = len(graph[v])
        for w in graph[v]:
            in_degree[w] += 1
    
    for v in graph:
        if not is_1_in_1_out(v):
            if out_degree[v] > 0:
                for w in graph[v]:
                    non_branching_path = [v, w]
                    while is_1_in_1_out(w):
                        u = graph[w].pop()
                        non_branching_path.append(u)
                        w = u
                    paths.append(non_branching_path)

    visited = set()
    for v in graph:
        if is_1_in_1_out(v) and v not in visited:
            cycle = [v]
            visited.add(v)
            w = graph[v][0]
            while w != v:
                cycle.append(w)
                visited.add(w)
                w = graph[w][0]
            cycle.append(v)
            paths.append(cycle)
    return paths

path_dic = defaultdict(list)
with open("input.txt", "r") as file:
    for line in file:
        array = line.rstrip().replace(":", " ").split()
        start_vertex = array[0]
        end_vertices = array[1:]

        if start_vertex not in path_dic:
            path_dic[start_vertex] = []
        path_dic[start_vertex].extend(end_vertices)

        for end_vertex in end_vertices:
            if end_vertex not in path_dic:
                path_dic[end_vertex] = []

res = MaximalNonBranchingPaths(path_dic)

with open("output.txt", "w") as file:
    for path in res:
        file.write(" ".join(path) + "\n")
