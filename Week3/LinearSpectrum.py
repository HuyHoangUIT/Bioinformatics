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

with open("input.txt", "r") as file:
    string = file.readline().rstrip()

res = LinearSpectrum(string)

with open("output.txt", "w") as file:
    for i in res:
        file.write(str(i) + " ")
