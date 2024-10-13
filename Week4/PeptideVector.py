_mass_by_amino_acid_ = {"X":4, "Z":5, "G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "L":113, "N":114, "D":115, "Q":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186, "I":113, "K":128}
def PeptideVector(peptide):
    vector = []
    for i in peptide:
        tmp = [0]*_mass_by_amino_acid_[i]
        tmp[-1] = 1
        vector.extend(tmp)
    return vector
      
with open("input.txt") as infile:
    peptide = infile.readline().rstrip()    
vector = PeptideVector(peptide)
string = ' '.join(map(str, vector))

with open("output.txt", "w") as outfile:
    outfile.write(string)