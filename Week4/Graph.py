from collections import defaultdict
mass_table = {57: 'G', 71: 'A', 87: 'S', 97: 'P', 99: 'V', 101: 'T', 103: 'C', 113: 'I', 114: 'N', 115: 'D', 128: 'K', 129: 'E', 131:'M', 137: 'H', 147: 'F', 156: 'R', 163: 'Y', 186: 'W'}

def Graph(Spectrum):
    graph = defaultdict(int)
    for i in range(len(spectrum)):
        for j in range(i + 1):
            mass = spectrum[i] - spectrum[j]
            if mass in mass_table:
                graph[f'{spectrum[j]}->{spectrum[i]}'] = mass_table[mass]
    return graph

spectrum = [0]
with open("input.txt") as infile:
    spectrum.extend(list(map(int, infile.readline().rstrip().split())))
    
graph = Graph(spectrum)

with open("output.txt", "w") as outfile:
    for key, value in graph.items():
        outfile.write(f'{key}: {value}\n')