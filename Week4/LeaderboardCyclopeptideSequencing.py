import itertools

# Amino acid masses and related classes

amino_acid_masses = {"G": 57, "A": 71, "S": 87, "P": 97, "V": 99, "T": 101,
                     "C": 103, "I": 113, "L": 113, "N": 114, "D": 115, "K": 128,
                     "Q": 128, "E": 129, "M": 131, "H": 137, "F": 147, "R": 156,
                     "Y": 163, "W": 186}

unique_masses_amino_acid_names = "GASPVTCINDKEMHFRYW"

def peptide_from_names(code: str):
    masses = [amino_acid_masses[c] for c in code]
    return Peptide(masses)

class Peptide:
    def __init__(self, masses:list):
        self.masses = masses

    def length(self):
        return len(self.masses)

    def total_mass(self):
        return sum(self.masses)

    def append_by_name(self, code:str):
        return Peptide(self.masses + [amino_acid_masses[code]])

    def expand(self, full_dictionary=False):
        if full_dictionary:
            return [Peptide(self.masses + [p]) for p in range(57, 201)]
        return [Peptide(self.masses + [amino_acid_masses[p]]) for p in unique_masses_amino_acid_names]
  
    def to_code(self):
        return [amino_acid_masses.get(m, str(m)) for m in self.masses]

    def __str__(self):
        return f"[peptide {self.masses}]"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.masses < other.masses

    def cyclospectrum(self):
        cyclic = self.masses + self.masses
        spectrum = [0]
        for length in range(1, self.length()):
            for starting in range(0, self.length()):
                total = sum(cyclic[starting:starting+length])
                spectrum.append(total)
        spectrum.append(self.total_mass())
        return Spectrum(spectrum)

    def linearspectrum(self):
        spectrum = [0]
        for length in range(1, self.length() + 1):
            for starting in range(0, self.length() - length + 1):
                total = sum(self.masses[starting:starting+length])
                spectrum.append(total)
        return Spectrum(spectrum)

class Spectrum:
    def __init__(self, spectrum):
        self.spectrum = sorted(spectrum)
        self.total_mass : int = self.spectrum[-1]
  
    def __str__(self):
        return f"[spectrum {self.spectrum.__str__()}]"

    def __repr__(self):
        return self.__str__()

    def score(self, another_spectrum):
        total = 0
        temp_spectrum = another_spectrum.spectrum.copy()
        for mass in self.spectrum:
            if mass in temp_spectrum:
                temp_spectrum.remove(mass)
                total += 1
        return total       

    def is_subspectrum(self, parent):
        temp_spectrum = parent.spectrum.copy()
        for mass in self.spectrum:
            if mass == 0:
                continue
            if mass in temp_spectrum:
                temp_spectrum.remove(mass)
            else:
                return False
        return True

    def leaderboard_cyclopeptide_sequencing(self, n, full_dictionary=False):
        leader = Peptide([])
        candidates = [leader]
        final_peptides = set()
        while len(candidates) > 0:
            candidates = self._expand_all_peptides(candidates, full_dictionary)
            leaderboard = Leaderboard(self)
            for peptide in candidates:
                if peptide.total_mass() == self.total_mass:
                    if self.score(peptide.cyclospectrum()) >= self.score(leader.cyclospectrum()):
                        leader = peptide
                        if self.score(leader.cyclospectrum()) == 83:
                            print("-".join(map(str, leader.masses)))
                    leaderboard.add(peptide)
                elif peptide.total_mass() < self.total_mass:
                    leaderboard.add(peptide)
            candidates = leaderboard.trim(n)
            final_peptides = set(candidates)  # Collect all valid peptides
        return final_peptides

    def _expand_all_peptides(self, candidate_peptides, full_dictionary:bool = False):
        candidate_peptides = [peptide.expand(full_dictionary = full_dictionary) for peptide in candidate_peptides]
        candidate_peptides = [p for sublist in candidate_peptides for p in sublist]
        return candidate_peptides

class Leaderboard:
    def __init__(self, experimental_spectrum:Spectrum):
        self.board = []
        self.experimental_spectrum = experimental_spectrum
  
    def add(self, peptide):
        score = peptide.linearspectrum().score(self.experimental_spectrum)
        t = (score, peptide)
        self.board.append(t)
        return self

    def add_all(self, peptides: list):
        for peptide in peptides:
            self.add(peptide)
        return self
  
    def trim(self, n: int):
        prioritized = list(reversed(sorted(self.board)))
        trimmed = prioritized[0:n]
        while n < len(prioritized) and prioritized[n][0] == prioritized[n-1][0]:
            n += 1
            trimmed = prioritized[0:n]
        return [peptide for _, peptide  in trimmed]

def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip().split()
    N = int(data[0])
    spectrum = Spectrum(list(map(int, data[1:])))
    return N, spectrum

def main():
    N, Spectrum10 = read_input("input.txt")  # File containing Spectrum10
    all_best_peptides = Spectrum10.leaderboard_cyclopeptide_sequencing(N, full_dictionary=True)
    
    with open("output.txt", "w") as file:
        for peptide in all_best_peptides:
            formatted_peptide = '-'.join(map(str, peptide.masses))
            file.write(formatted_peptide + '\n')

if __name__ == "__main__":
    main()