from collections import defaultdict

def TrieMatching(String, patterns):
    position = {pattern: [] for pattern in patterns}
    for pattern in patterns:
        for i in range (len(String) - len(pattern) + 1):
            if String[i:i+len(pattern)] == pattern:
                position[pattern].append(i)
    return position

with open("input.txt") as infile:
    String = infile.readline().rstrip()
    Patterns = infile.readline().rstrip().split()
# Construct the trie and get the edges

position = TrieMatching(String, Patterns)

with open("output.txt", "w") as outfile:
    for pattern in position:
        outfile.write(f"{pattern}: ")
        for pos in position[pattern]:
            outfile.write(f"{pos} ")
        outfile.write("\n")