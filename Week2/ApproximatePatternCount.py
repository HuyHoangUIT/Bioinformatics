import os
import sys

def HammingDistance(String1, String2):
    count = 0
    
    for i in range (len(String1)):
        if String1[i] != String2[i]:
            count += 1
    return count

def ApproximatePatternCount(String1, String2, d):
    PosArr = []
    C = 0
    for i in range (len(String2) - len(String1) + 1):
        if HammingDistance(String1, String2[i:i+len(String1)]) <= d:
            PosArr.append(i)
            C += 1
    return C
    
def main():
    print(ApproximatePatternCount("ATTCGG", "TCTGAGTGTAATTAAGGCCGTAGTTTCGTCGTTGAGGTGGGCTACTATCATATCATCGGGGATCACATTATTAGTAATTCGGACTAAGTTTGACCCCTGGCAAGCATGGAGCCATGCCGGGATACTGAGTGGTTCCCTCCAAAGGGTTGATTCTACTGCCGCATATTGATATACGTTTCGAGCGACATTCATCCGTCGCTGGTTGATGTAAACGATCAAGTTTTACACTGTTTTATTCTTTTCATATCGCTACTCTAGAGCATGGTGTAATATGTCGTCGGAGGCTGTGTCTTGATAATAACCACGTAGAAGCATGTAACCCGTCGAGGGCCACTTATCTGCGCATCCATGGTAATTGTAACCCCAGAGAGTGTCGCGCGAG", 3))

main()