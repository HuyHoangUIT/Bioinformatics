from collections import deque

def Coloring(adj, colors):
    ripe = deque()  # Initialize an empty deque to hold ripe nodes

    # Initially identify ripe nodes
    for node in adj:
        if node not in colors and all(neighbor in colors for neighbor in adj[node]):
            ripe.append(node)
    
    # Coloring logic while there are ripe nodes
    while ripe:
        node = ripe.popleft()  # Get and remove the leftmost node from deque
        check = 0
        
        # Check neighbors for counting colored nodes
        for neighbor in adj[node]:
            if colors[neighbor] == "purple":
                colors[node] = "purple"
                break
            if colors[neighbor] == "red":
                check += 1
        
        if node not in colors:  # Check if the node is still uncolored
            if check == len(adj[node]):
                colors[node] = "red"
            elif check == 0:
                colors[node] = "blue"
            else:
                colors[node] = "purple"
        
        # After coloring the current node, check if any neighbors become ripe
        for node in adj:
            if node not in colors and all(neighbor in colors for neighbor in adj[node]):
                ripe.append(node)

    return colors

# Initialize dictionaries for adjacency list and colors
adj = {}
colors = {}

with open("input.txt") as infile:
    # Read adjacency list part
    for line in infile:
        if line.strip() == '-':
            break
        line = list(map(int, line.rstrip().replace(":", "").split()))
        if len(line) > 1:
            adj[line[0]] = line[1:]  # handle multiple neighbors

    # Read colors part
    for line in infile:
        line = line.rstrip().split()
        colors[int(line[0])] = line[1]

# Print initial colors and adjacency list
print(colors)
print(adj)

# Perform the coloring
res = Coloring(adj, colors)

# Write the result to the output file
with open("output.txt", "w") as outfile:
    for key, value in res.items():
        outfile.write(f"{key} {value}\n")
