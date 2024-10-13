import os
import sys
from collections import defaultdict

def Composition(k, text):
    result = []
    for i in range(0, len(text) - k + 1):
        chunk = text[i:i + k]
        result.append(chunk)
    return result

def DeBruijn(k, text):
    composition = Composition(k, text)
    dic = defaultdict(list)
    for i in composition:
        prefix = i[:k - 1]
        suffix = i[1:]
        dic[prefix].append(suffix)
    return dic

with open('input.txt', 'r') as file:
    k = file.readline()
    Text = file.readline()
file.close()

res = DeBruijn(int(k), Text)

with open('output.txt', 'w') as file:
    for kmer, neighbors in res.items():
        if neighbors:  
            file.write(f"{kmer}: {' '.join(neighbors)}\n")
file.close()