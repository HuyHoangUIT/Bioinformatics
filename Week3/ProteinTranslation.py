codon_table = {}
with open("RNA_codon_table_1.txt", "r") as file:
    for line in file:
        line = line.rstrip().split(" ")
        codon_table[line[0]] = line[1]
file.close()

def ProteinTranslation(string):
    peptide = ""
    for i in range (0, len(string) - 2, 3):
        codon = string[i:i+3]
        peptide += codon_table[codon]
    return peptide.replace('*', '')

with open("input.txt", "r") as file:
    string = file.readline().rstrip()
file.close()

res = ProteinTranslation(string)

with open("output.txt", "w") as file:
    file.write(res)
file.close()

