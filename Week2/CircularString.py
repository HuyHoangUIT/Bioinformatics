import random
from collections import defaultdict

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

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
        
    st = Stack()
    path = []
    st.push(start)
    while not st.isEmpty():
        u = st.peek()
        if u in path_dic and len(path_dic[u]) != 0:
            v = path_dic[u].pop()
            st.push(v)
        else:
            path.append(st.pop())
    return path[::-1]

def StringReconstruction(k, patterns):
    db = DeBruijn(k, patterns)
    ep = EulerianPath(db)
    
    res = ep[0]  # Start with the first k-mer
    for i in range(1, len(ep)):
        res += ep[i][-1]  # Append only the last character of each k-mer

    return res[:-(k-1)]  # Remove the redundant overlap characters

def CircularString(k):
    binaries = []
    for i in range(2**k):
        binaries.append(bin(i)[2:].zfill(k))
    return StringReconstruction(k, binaries)

with open("input.txt", "r") as file:
    k = int(file.readline().rstrip())
file.close()

res = CircularString(k)

with open("output.txt", "w") as file:
    file.write(res)
file.close()
