AminoAcidMass = {}
with open("integer_mass_table.txt", "r") as file:
    for line in file:
        line = line.rstrip().split(" ")
        AminoAcidMass[line[0]] = int(line[1])
file.close()

def LinearSpectrum(string):
    PrefixMass = [0]
    for i in range(len(string)):
        PrefixMass.append(PrefixMass[-1] + AminoAcidMass[string[i]])
    
    ls = [0]
    for i in range(len(string)):
        for j in range(i + 1, len(PrefixMass)):
            ls.append(PrefixMass[j] - PrefixMass[i])
    
    ls.sort()
    return ls

def LinearScore(Peptide, Spectrum):
    LinearPeptide = LinearSpectrum(Peptide)
    score = len(LinearPeptide)
    for i in LinearPeptide:
        if i not in Spectrum:
            score -= 1
        else:
            Spectrum.remove(i)
    return score

with open("input.txt", "r") as file:
    Peptide = file.readline().rstrip()
    Spectrum = list(map(int, file.readline().rstrip().split()))

res = LinearScore(Peptide, Spectrum)

with open("output.txt", "w") as file:
    file.write(str(res))
