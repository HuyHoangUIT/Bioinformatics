import os
import sys
import random
from collections import deque

def EulerianCycle(path_dic):
    v = random.choice(list(path_dic.keys()))
    st = deque()
    path = []
    st.push(v)
    while st:
        u = st[-1]
        if len(path_dic[u]) != 0:
            v = path_dic[u].pop()
            st.push(v)
        else:
            path.append(st.pop())
    return path[::-1]          

path_dic = {}
with open("input.txt", "r") as file:
    for line in file:
        array = line.rstrip().replace(":", " ").split()
        path_dic[array[0]] = array[1:]
file.close()

print(path_dic)

res = EulerianCycle(path_dic)

with open("output.txt", "w") as file:
    file.write(" ".join(res))
file.close()