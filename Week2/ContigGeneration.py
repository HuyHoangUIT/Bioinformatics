import random
from collections import defaultdict

degree_dic = {}

def DeBruijn(k, array):
    dic = defaultdict(list)
    for i in array:
        prefix = i[:k - 1]
        suffix = i[1:]
        dic[prefix].append(suffix)
        
    return dic

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
    
    for v in list(graph.keys()):
        if not is_1_in_1_out(v):
            if out_degree[v] > 0:
                for w in list(graph[v]):
                    non_branching_path = [v, w]
                    while is_1_in_1_out(w):
                        if not graph[w]:  # Check if there are no outgoing edges
                            break
                        u = graph[w][0]  # Get the first element without popping
                        non_branching_path.append(u)
                        w = u
                    paths.append(non_branching_path)
    return paths

def ContigGeneration(array):
    path_dic = DeBruijn(len(array[0]), array)
    contigs = MaximalNonBranchingPaths(path_dic)
    res = []
    for contig in contigs:
        tmp = contig[0]
        for i in contig[1:]:
            tmp += i[-1]
        res.append(tmp)
        
    return res

with open("input.txt", "r") as file:
    array = file.readline().rstrip().split(" ")
file.close()

res = ContigGeneration(array)

with open("output.txt", "w") as file:
    file.write(" ".join(res))
file.close()
