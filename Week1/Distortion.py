import math
from copy import copy

# Distance calculation function (Euclidean distance)
def distance(v, w, m):
    return math.sqrt(sum((v[i] - w[i])**2 for i in range(m)))

# Function to find the closest center to a DataPoint
def find_closest_center(DataPoint, Centers, m):
    min_distance = float("inf")
    for center in Centers:
        dist = distance(DataPoint, center, m)
        if dist < min_distance:
            min_distance = dist
    return min_distance

def Distortion(Data, Centers, k, m):
    Dis = 0.0
    for point in Data:
        Dis += (find_closest_center(point, Centers, m))**2
    return Dis/len(Data)

# Reading input data
Centers = []
Data = []
with open("input.txt") as infile:
    k, m = map(int, infile.readline().rstrip().split())
    for _ in range (k):
        Centers.append([float(x) for x in infile.readline().rstrip().split()])
    infile.readline()
    for line in infile:
        Data.append([float(x) for x in line.split()])
# Execute the FarthestFirstTraversal algorithm
distortion = Distortion(Data, Centers, k, m)

# Writing output data
with open("output.txt", "w") as outfile:
        outfile.write(str(distortion))
