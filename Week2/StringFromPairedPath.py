from collections import defaultdict, deque

def DeBruijnPaired(k, d, pairs):
    graph = defaultdict(list)
    for pair in pairs:
        prefix1 = pair[0][:k-1]
        suffix1 = pair[0][1:]
        prefix2 = pair[1][:k-1]
        suffix2 = pair[1][1:]
        graph[(prefix1, prefix2)].append((suffix1, suffix2))
    return graph

def find_start(graph):
    in_deg, out_deg = defaultdict(int), defaultdict(int)
    for u in graph:
        out_deg[u] += len(graph[u])
        for v in graph[u]:
            in_deg[v] += 1
    start, end = None, None
    for node in set(in_deg) | set(out_deg):
        if out_deg[node] > in_deg[node]:
            start = node
        if in_deg[node] > out_deg[node]:
            end = node
    return start if start else next(iter(graph))

def EulerianPath(graph):
    start_node = find_start(graph)
    stack = [start_node]
    path = deque()
    while stack:
        u = stack[-1]
        if graph[u]:
            v = graph[u].pop()
            stack.append(v)
        else:
            path.appendleft(stack.pop())
    return path

def StringFromPairedPath(k, d, path):
    prefix_string = path[0][0]
    suffix_string = path[0][1]
    
    for i in range(1, len(path)):
        prefix_string += path[i][0][-1]
        suffix_string += path[i][1][-1]
    
    return prefix_string + suffix_string[-(k+d):]

def StringReconstructionPaired(k, d, pairs):
    graph = DeBruijnPaired(k, d, pairs)
    eulerian_path = EulerianPath(graph)
    return StringFromPairedPath(k, d, eulerian_path)

with open("input.txt", "r") as file:
    k, d = map(int, file.readline().rstrip().split())
    pairs = []
    kmers = file.readline().rstrip().split(" ")
    for kmer in kmers:
        left, right = kmer.split("|")
        pairs.append((left, right))

result = StringReconstructionPaired(k, d, pairs)

with open("output.txt", "w") as file:
    file.write(result)
