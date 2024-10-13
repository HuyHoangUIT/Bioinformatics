_amino_acid_by_mass_ = {4:"X", 5:"Z", 57:"G", 71:"A", 87:"S", 97:"P", 99:"V", 101:"T", 103:"C", 113:"L", 114:"N", 115:"D", 128:"Q", 129:"E", 131:"M", 137:"H", 147:"F", 156:"R", 163:"Y", 186:"W"}
def Peptide(vector):
    peptide = ""
    cnt = 1
    for i in vector:
        if i == 1:
            peptide += _amino_acid_by_mass_[cnt]
            cnt = 1
        else:
            cnt += 1
    return peptide
      
with open("input.txt") as infile:
    vector = list(map(int, infile.readline().rstrip().split()))
peptide = Peptide(vector)

with open("output.txt", "w") as outfile:
    outfile.write(peptide)