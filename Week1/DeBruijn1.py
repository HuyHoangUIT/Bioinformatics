import os
import sys
from collections import defaultdict

def DeBruijn(array):
    k = len(array[0])
    dic = defaultdict(list)
    for i in array:
        prefix = i[:k - 1]
        suffix = i[1:]
        dic[prefix].append(suffix)
    return dic

array = []
with open('input.txt', 'r') as file:
    array = file.read().rstrip().split()
file.close()

res = DeBruijn(array)

with open('output.txt', 'w') as file:
    for kmer, neighbors in res.items():
        file.write(f"{kmer}: {' '.join(neighbors)}\n")
file.close()