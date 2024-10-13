from collections import defaultdict, deque

def topological_sort(Graph, V):
    # Find in-degree of all vertices
    in_degree = {v: 0 for v in range(V)}
    for u in Graph:
        for v, w in Graph[u]:
            in_degree[v] += 1
    
    # Collect all vertices with in-degree 0
    queue = deque([v for v in in_degree if in_degree[v] == 0])
    topo_order = []
    
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v, w in Graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    return topo_order

def longest_path(Graph, V, start_vertex, end_vertex):
    # Topological sort
    topo_order = topological_sort(Graph, V)
    
    # Initialize distances to -infinity, except the start vertex
    dist = {v: float('-inf') for v in range(V)}
    dist[start_vertex] = 0
    
    # Traverse vertices in topological order
    for u in topo_order:
        if dist[u] != float('-inf'):
            for v, w in Graph[u]:
                if dist[v] < dist[u] + w:
                    dist[v] = dist[u] + w
    
    # Reconstruct the path if needed
    path = []
    if dist[end_vertex] != float('-inf'):
        current = end_vertex
        while current != start_vertex:
            for u in Graph:
                for v, w in Graph[u]:
                    if v == current and dist[current] == dist[u] + w:
                        path.append(current)
                        current = u
                        break
        path.append(start_vertex)
        path.reverse()
    
    return dist[end_vertex], path

# Read input from file
Graph = defaultdict(list)
with open("input.txt") as infile:
    start_vertex, end_vertex = map(int, infile.readline().rstrip().split())
    for line in infile:
        u, v, w = line.rstrip().split()
        Graph[int(u)].append((int(v), int(w)))

# Number of vertices in the graph (can be inferred from input or manually set)
V = max(max(u, v) for u in Graph for v, w in Graph[u]) + 1

# Get the longest path and its length
longest_dist, longest_path = longest_path(Graph, V, start_vertex, end_vertex)

# Output the results
print(longest_dist)
print(" ".join(map(str, longest_path)))
