import math

# Distance calculation function (Euclidean distance)
def distance(v, w, m):
    return math.sqrt(sum((v[i] - w[i])**2 for i in range(m)))

# Function to find the closest center to a DataPoint
def find_closest_center(DataPoint, Centers, m):
    min_distance = float("inf")
    closest = None
    for center in Centers:
        dist = distance(DataPoint, center, m)
        if dist < min_distance:
            min_distance = dist
            closest = center
    return closest

# Assign points to the closest centers
def Clustering(Data, Centers, m):
    clusters = {tuple(center): [] for center in Centers}
    for point in Data:
        closest_center = find_closest_center(point, Centers, m)
        clusters[tuple(closest_center)].append(point)
    return clusters

# Lloyd's Algorithm for clustering
# Lloyd's Algorithm for clustering
def LloydAlgorithm(Data, k, m):
    Centers = Data[:k]  # Select the first k points as initial centers
    
    while True:
        # Assign points to the closest center
        Clusters = Clustering(Data, Centers, m)
        
        # Calculate new centers
        new_Centers = []
        for center in Centers:
            cluster_points = Clusters[tuple(center)]
            if cluster_points:
                # Compute the mean of the points in this cluster
                new_center = [sum(coord[i] for coord in cluster_points) / len(cluster_points) for i in range(m)]
                new_Centers.append(new_center)
        
        # Stop if the centers don't change (compare each coordinate)
        if all(
            all(round(a[i], 3) == round(b[i], 3) for i in range(m))
            for a, b in zip(new_Centers, Centers)
        ):
            break
        
        Centers = new_Centers
    
    return Centers

# Reading input data
Data = []
with open("input.txt") as infile:
    k, m = map(int, infile.readline().rstrip().split())
    for line in infile:
        Data.append([float(x) for x in line.split()])

# Execute Lloyd's Algorithm
Centers = LloydAlgorithm(Data, k, m)

# Writing output data with precision to at least 3 decimal places
with open("output.txt", "w") as outfile:
    for center in Centers:
        outfile.write(" ".join(f"{x:.3f}" for x in center) + "\n")
