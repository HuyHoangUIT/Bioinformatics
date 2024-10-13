import os
import sys

def SkewDiagram(Genome):
    Skew = []
    Skew.append(0)
    
    for i in range (len(Genome)):
        if Genome[i] in ["A", "T"]:
            Skew.append(Skew[i])
        elif Genome[i] == 'G':
            Skew.append(Skew[i] + 1)
        elif Genome[i] == 'C':
            Skew.append(Skew[i] - 1)
    return ' '.join(str(num) for num in Skew)

def main():
    print(SkewDiagram("GAGCCACCGCGATA"))

main()