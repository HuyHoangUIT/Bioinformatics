import os
import sys
import random
from collections import deque

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
    while st:
        u = st[-1]
        if u in path_dic and path_dic[u]:
            v = path_dic[u].pop()
            st.append(v)
        else:
            path.append(st.pop())
    return path[::-1]          

path_dic = {}
degree_dic = {}
with open("input.txt", "r") as file:
    for line in file:
        array = line.rstrip().replace(":", " ").split()
        start_vertex = array[0]
        end_vertices = array[1:]

        if start_vertex not in path_dic:
            path_dic[start_vertex] = []
        path_dic[start_vertex].extend(end_vertices)

        if start_vertex not in degree_dic:
            degree_dic[start_vertex] = [0, 0]  
        degree_dic[start_vertex][1] += len(end_vertices)

        for end_vertex in end_vertices:
            if end_vertex not in degree_dic:
                degree_dic[end_vertex] = [0, 0] 
            degree_dic[end_vertex][0] += 1

res = EulerianPath(path_dic)

with open("output.txt", "w") as file:
    file.write(" ".join(res))
