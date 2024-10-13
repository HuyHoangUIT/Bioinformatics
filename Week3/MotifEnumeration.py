def HammingDistance(string1, string2):
    distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            distance = distance +1
    return distance

def Neighbors(pattern, d):
    neighborhood = set()
    nucleotides = ["A", "G", "T", "C"]
    if len(pattern) == 1:
        return nucleotides
    if d == 0:
        return set()
    suffixNeighbors = Neighbors(pattern[1:], d)
    for neighbor in suffixNeighbors:
        if HammingDistance(pattern[1:], neighbor) < d:
            for nucleotide in nucleotides:
                neighborhood.add(nucleotide + neighbor)
        else:
            neighborhood.add(pattern[0] + neighbor)
    return list(neighborhood)


def isPatternInAll(pattern, dna, d):
    for string in dna:
        found = False
        for i in range(len(string) - len(pattern) + 1):
            substring = string[i:i+len(pattern)]
            if HammingDistance(pattern, substring) <= d:
                found = True
                break
        if not found:
            return False
    return True

def MotifEnumeration(dnas, k, d):
    Patterns = set()
    for i in range(len(dnas[0]) - k + 1):
        pattern = dnas[0][i:i+k]
        neighborhood = Neighbors(pattern, d)
        for neighbor in neighborhood:
            if isPatternInAll(neighbor, dnas, d):
                Patterns.add(neighbor)
    return list(Patterns)

Dna = ["ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT"]
k = 3
d = 1
result = MotifEnumeration(Dna, k, d)
print(" ".join(sorted(result)))