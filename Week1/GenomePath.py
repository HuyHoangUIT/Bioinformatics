import os
import sys

def GenomePath(dna):
    res = dna[0]
    for i in range(1, len(dna)):
        res  += dna[i][-1]
    return res

with open('input.txt', 'r') as file:
    array = file.read()
file.close()

res = GenomePath(array.split())
with open('output.txt', 'w') as file:
    file.write(res)
file.close()