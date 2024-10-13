import os
import sys

from HammingDistance import HammingDistance

def neighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    
    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for text in suffix_neighbors:
        if HammingDistance(pattern[1:], text) < d:
            for nucleotide in 'ACGT':
                neighborhood.add(nucleotide + text)
        else:
            neighborhood.add(pattern[0] + text)
    
    return neighborhood