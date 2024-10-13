import os
import sys
import math

def ProfileForming(motifs):
    k = len(motifs[0])
    profile = {nucleotide: [0] * k for nucleotide in 'ACGT'}
    t = len(motifs)
    for i in range(k):
        column = [motif[i] for motif in motifs]
        for nucleotide in 'ACGT':
            count = column.count(nucleotide)
            profile[nucleotide][i] = count / t
    return profile

def ProfileMost(text, k, profile):
    max_probability = -1.0
    most_probable_kmer = ""
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        probability = 1.0
        for j, nucleotide in enumerate(kmer):
            probability *= profile[nucleotide][j]
        if probability > max_probability:
            max_probability = probability
            most_probable_kmer = kmer
    return most_probable_kmer

def Score(motifs, t):
    k = len(motifs[0])
    score = 0
    for i in range(k):
        column = [motif[i] for motif in motifs]
        max_count = max(column.count(nucleotide) for nucleotide in 'ACGT')
        score += t - max_count
    return score

def GreedyMotifSearch(dna, k, t):
    best_motifs = [seq[:k] for seq in dna]
    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i:i+k]]
        for j in range(1, t):
            profile = ProfileForming(motifs)
            most_probable_kmer = ProfileMost(dna[j], k, profile)
            motifs.append(most_probable_kmer)

        if Score(motifs, t) < Score(best_motifs, t):
            best_motifs = motifs
    return best_motifs
        
strings = "TTACCTTAAC GATGTCTGTC ACGGCGTTAG CCCTAACGAG CGTCAGAGGT"
k = 4
t = 5
print (' '.join(GreedyMotifSearch(strings.split(), k ,t)))
        
        
