from collections import defaultdict
mass_table = {57: 'G', 71: 'A', 87: 'S', 97: 'P', 99: 'V', 101: 'T', 103: 'C', 113: 'I', 114: 'N', 115: 'D', 128: 'K', 129: 'E', 131:'M', 137: 'H', 147: 'F', 156: 'R', 163: 'Y', 186: 'W'}

def Graph(Spectrum):
    graph = defaultdict(dict)
    for i in range(len(spectrum)):
        for j in range(i + 1):
            mass = spectrum[i] - spectrum[j]
            if mass in mass_table:
                graph[spectrum[j]][spectrum[i]] = mass_table[mass]
    return graph

def DecodingIdeaSpectrum(Spectrum):
    graph = Graph(Spectrum)  # Ensure this builds the graph correctly
    sequence = []
    current = Spectrum[0]

    while current <= Spectrum[-1]:
        if current not in graph:
            break  # Exit if there are no paths from the current node
        
        path = graph[current]
        key, value = next(iter(path.items()))
        sequence.append(value)
        current = key  # Update current to the next key

    return sequence
        

spectrum = [0]
with open("input.txt") as infile:
    spectrum.extend(list(map(int, infile.readline().rstrip().split())))
    
string = DecodingIdeaSpectrum(spectrum)
string = ''.join(string)

with open("output.txt", "w") as outfile:
    outfile.write(string + '\n')