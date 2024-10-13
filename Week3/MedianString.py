import os
import sys

def HammingDistance(String1, String2):
    count = 0
    
    for i in range (len(String1)):
        if String1[i] != String2[i]:
            count += 1
    return count

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = len(Pattern)
    distance = 0
    for string in Dna:
        tmp = float('inf')
        for i in range (len(Dna[0]) - len(Pattern) + 1):
            substr = string[i:i+k]
            if HammingDistance(Pattern, substr) < tmp:
               tmp = HammingDistance(Pattern, substr)
        distance += tmp
    return distance

def MedianString(k, dna):
    distance = float('inf')
    pattern = ""

    for i in range(len(dna[0]) - k + 1):
        current_pattern = dna[0][i:i+k]
        current_distance = DistanceBetweenPatternAndStrings(current_pattern, dna)

        if current_distance < distance:
            distance = current_distance
            pattern = current_pattern

    return pattern
            
array = [
    "AAATTGACGCAT",
    "GACGACCACGTT",
    "CGTCAGCGCCTG",
    "GCTGAGCACCGG",
    "AGTTCGGGACAG"
    ]
print(MedianString(3, array))
        