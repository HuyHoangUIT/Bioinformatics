import random
from collections import defaultdict, deque

degree_dic = {}

def DeBruijn(k, array):
    dic = defaultdict(list)
    for i in array:
        prefix = i[:k - 1]
        suffix = i[1:]
        dic[prefix].append(suffix)
        
        if prefix not in degree_dic:
            degree_dic[prefix] = [0, 0]  
        degree_dic[prefix][1] += 1

        if suffix not in degree_dic:
            degree_dic[suffix] = [0, 0] 
        degree_dic[suffix][0] += 1
    return dic

def EulerianPath(path_dic):
    start = None
    for vertex in degree_dic:
        if degree_dic[vertex][1] - degree_dic[vertex][0] == 1:
            start = vertex
            break
    if start is None:
        start = random.choice(list(path_dic.keys()))
        
    st = deque()
    path = []
    st.append(start)
    while len(st) > 0:
        u = st[-1]
        if u in path_dic and len(path_dic[u]) != 0:
            v = path_dic[u].pop()
            st.append(v)
        else:
            path.append(st.pop())
    return path[::-1]

def StringReconstruction(k, patterns):
    db = DeBruijn(k, patterns)
    ep = EulerianPath(db)
    
    res = ep[0]
    for i in range(1, len(ep)):
        res += ep[i][-1]         
    return res

with open("input.txt", "r") as file:
    k = int(file.readline().rstrip())
    array = file.readline().rstrip().split()
file.close()

res = StringReconstruction(k, array)

with open("output.txt", "w") as file:
    file.write(res)
file.close()
