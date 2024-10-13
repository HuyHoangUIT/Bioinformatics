import os
import sys

from HammingDistance import HammingDistance

def ApproximatePatternMatching(String1, String2, d):
    PosArr = []
    for i in range (len(String2) - len(String1) + 1):
        if HammingDistance(String1, String2[i:i+len(String1)]) <= d:
            PosArr.append(i)
    return " ".join(str(num) for num in PosArr)
    
def main():
    Genome = ""
    print(ApproximatePatternMatching("ATGGCGAAGA", "", 4))

main()