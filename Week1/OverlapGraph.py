import os
import sys

def NeighborSearch(kmer, kmers):
    neighbors = []
    for kmer1 in kmers:
        if kmer[1:] == kmer1[:-1]:
            neighbors.append(kmer1)
    return neighbors

def OverlapGraph(dna):
    graph = {}
    for i in range (len(dna)):
        if dna[i] not in graph:
            graph[dna[i]] = []
        else:
            continue
        graph[dna[i]].extend(NeighborSearch(dna[i], dna[i+1:]))
    return graph

with open('input.txt', 'r') as file:
    kmer_list = file.read().split()
file.close()

res = OverlapGraph(kmer_list)

with open('output.txt', 'w') as file:
    for kmer, neighbors in res.items():
        if neighbors:  
            file.write(f"{kmer}: {' '.join(neighbor for neighbor in neighbors)}\n")
file.close()