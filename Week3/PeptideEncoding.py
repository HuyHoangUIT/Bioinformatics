codon_table = {}
with open("RNA_codon_table_1.txt", "r") as file:
    for line in file:
        line = line.rstrip().split(" ")
        codon_table[line[0]] = line[1]

def ReverseComplement(Text):
    complement = {"A": "T", "C": "G", "G": "C", "T": "A"}
    return "".join(complement[base] for base in reversed(Text))

def ProteinTranslation(string):
    rna = string.replace('T', 'U')
    peptide = ""
    for i in range (0, len(rna) - 2, 3):
        codon = rna[i:i+3]
        peptide += codon_table[codon]
    return peptide.replace('*', '')

def PeptideEncoding(string, peptide):
    res = []
    lp = len(peptide)*3
    for i in range (len(string) - lp + 1):
        codon = ProteinTranslation(string[i:i+lp])
        reversed = ProteinTranslation(ReverseComplement(string[i:i+lp]))
        if codon == peptide or reversed == peptide:
            res.append(string[i:i+lp])
    return res

array = []
with open("input.txt", "r") as file:
    for line in file:
        array.append(line.replace("\n", ""))

string = "".join(array)
peptide = "VKLFPWFNQY"
res = PeptideEncoding(string, peptide)

with open("output.txt", "w") as file:
    file.write('\n'.join(res))