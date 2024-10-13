AminoAcidMass = {}
with open("integer_mass_table.txt", "r") as file:
    for line in file:
        line = line.rstrip().split(" ")
        AminoAcidMass[line[0]] = int(line[1])
file.close()

def CyclicSpectrum(string):
    PrefixMass = [0]
    for i in range(len(string)):
        PrefixMass.append(PrefixMass[-1] + AminoAcidMass[string[i]])
    
    peptideMass = PrefixMass[-1]
    cs = [0]
    for i in range(len(string)):
        for j in range(i + 1, len(PrefixMass)):
            cs.append(PrefixMass[j] - PrefixMass[i])
            if i > 0 and j < len(string):
                cs.append(peptideMass - (PrefixMass[j] - PrefixMass[i]))
    cs.sort()
    return cs

with open("input.txt", "r") as file:
    string = file.readline().rstrip()

res = CyclicSpectrum(string)

with open("output.txt", "w") as file:
    for i in res:
        file.write(str(i) + " ")
