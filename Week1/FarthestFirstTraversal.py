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

# FarthestFirstTraversal algorithm implementation
def FarthestFirstTraversal(Data, k, m):
    Centers = [Data.pop(0)]  # Initialize with the first data point and remove it from Data
    while len(Centers) < k:
        # Find the farthest point from any center
        farthest_point = None
        max_distance = float("-inf")
        
        for point in Data:
            # Find the closest center for this point
            closest_center = find_closest_center(point, Centers, m)
            dist_to_closest = distance(point, closest_center, m)
            
            # Update if this point is farther than the current max
            if dist_to_closest > max_distance:
                max_distance = dist_to_closest
                farthest_point = point
        
        # Add the farthest point found to the Centers and remove it from Data
        Centers.append(farthest_point)
        Data.remove(farthest_point)
    
    return Centers

# Reading input data
Data = []
with open("input.txt") as infile:
    k, m = map(int, infile.readline().rstrip().split())
    for line in infile:
        Data.append([float(x) for x in line.split()])

# Execute the FarthestFirstTraversal algorithm
Centers = FarthestFirstTraversal(Data, k, m)

# Writing output data
with open("output.txt", "w") as outfile:
    for center in Centers:
        outfile.write(" ".join(map(str, center)) + "\n")
