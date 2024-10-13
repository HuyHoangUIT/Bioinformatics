class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store children nodes (edges)
        self.node_id = None  # ID of the current node

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.node_count = 0  # Counter for assigning node IDs
        self.edges = []  # List to store edges in the form of (parent, child, symbol)

    def insert(self, pattern):
        current_node = self.root
        for char in pattern:
            if char not in current_node.children:
                # Create a new node if character is not present
                new_node = TrieNode()
                self.node_count += 1
                new_node.node_id = self.node_count
                current_node.children[char] = new_node
                # Add the edge to the adjacency list
                self.edges.append((current_node.node_id, new_node.node_id, char))
            # Move to the next node
            current_node = current_node.children[char]

def trie_construction(patterns):
    trie = Trie()
    trie.root.node_id = 0  # Label the root node as 0
    for pattern in patterns:
        trie.insert(pattern)
    return trie.edges

# Output the adjacency list

with open("input.txt") as infile:
    Patterns = infile.readline().rstrip().split()
# Construct the trie and get the edges

edges = trie_construction(Patterns)

with open("output.txt", "w") as outfile:
    for edge in edges:
        outfile.write(f"{edge[0]} {edge[1]} {edge[2]}\n")