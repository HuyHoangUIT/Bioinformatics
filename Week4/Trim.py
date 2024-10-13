from collections import Counter

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
    spectrum_counter = Counter(Spectrum)
    score = 0
    for mass in LinearPeptide:
        if spectrum_counter[mass] > 0:
            score += 1
            spectrum_counter[mass] -= 1
    return score

def Trim(Leaderboard, Spectrum, N):
    LinearScores = {}
    for peptide in Leaderboard:
        LinearScores[peptide] = LinearScore(peptide, Spectrum)
    LinearScores = dict(sorted(LinearScores.items(), key=lambda x: x[1], reverse=True))
    lb = list(LinearScores.keys())
    for i in range (N+1, len(lb)):
        if LinearScores[lb[i]] < LinearScores[lb[N]]:
            return lb[:i-1]
    return lb

with open("input.txt", "r") as file:
    Leaderboard = file.readline().rstrip().split()
    Spectrum = list(map(int, file.readline().rstrip().split()))
    N = int(file.readline().rstrip())

res = Trim(Leaderboard, Spectrum, N)

with open("output.txt", "w") as file:
    file.write(str(' '.join(peptide for peptide in res)))
