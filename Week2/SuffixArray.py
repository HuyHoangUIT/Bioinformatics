def SuffixArray(string):
    positions = {}
    for i in range (len(string)):
        positions[string[i:]] = i
    return sorted(positions.keys()), positions

with open("input.txt") as infile:
    string = infile.read().strip()

suffix, positions = SuffixArray(string)

with open("output.txt", "w") as outfile:
    for s in suffix:
        outfile.write(str(positions[s]) + " ")