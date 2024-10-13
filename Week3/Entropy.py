import os
import sys
import math

def MatrixCount(matrix):
    motifs = []
    for i in range (len(matrix[0])):
        temp = {}
        for j in range (len(matrix)):
            if matrix[j][i] not in temp:
                temp[matrix[j][i]] = 1
            else:
                temp[matrix[j][i]] += 1
        motifs.append(temp)
    return motifs

def EntropyCal(matrix):
    motifs = MatrixCount(matrix)
    entropy = 0
    for i in range (len(motifs)):
        print (motifs[i])
        for value in motifs[i].values():
            prob = value / len(matrix)
            entropy += -prob * math.log2(prob)
    return entropy

array = [
    "TCGGGGGTTTTT",
    "CCGGTGACTTAC",
    "ACGGGGATTTTC",
    "TTGGGGACTTTT",
    "AAGGGGACTTCC",
    "TTGGGGACTTCC",
    "TCGGGGATTCAT",
    "TCGGGGATTCCT",
    "TAGGGGAACTAC",
    "TCGGGTATAACC"]

print(EntropyCal(array))