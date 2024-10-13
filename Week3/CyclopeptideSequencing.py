import math

amino_acid_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 
                     128, 129, 131, 137, 147, 156, 163, 186]

def get_spectrum(peptide):
    spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            spectrum.append(sum(peptide[i:j]))
    return sorted(spectrum)

def CyclopeptideSequencing(spectrum):
    CandidatePeptides = [[mass] for mass in amino_acid_masses]
    FinalPeptides = []

    while CandidatePeptides:
        new_candidates = []
        for peptide in CandidatePeptides:
            for mass in amino_acid_masses:
                new_peptide = peptide + [mass]
                if sum(new_peptide) == spectrum[-1]:
                    if all(subsum in spectrum for subsum in get_spectrum(new_peptide)):
                        if new_peptide not in FinalPeptides:
                            FinalPeptides.append(new_peptide)
                elif sum(new_peptide) in spectrum:
                    new_candidates.append(new_peptide)
        CandidatePeptides = new_candidates

    return FinalPeptides


with open("input.txt") as file:
    spectrum = list(map(int, file.readline().strip().split()))

res = CyclopeptideSequencing(spectrum)

with open("output.txt", "w") as file:
    file.write(' '.join('-'.join(map(str, peptide)) for peptide in res))
