import math

# Points Definition
points = [(5,12),(7,24),(3,4),(9, 10),(5,9),(15,86)]

# Euclidean Distance
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Distances
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Distance
min_distance = min(distances)
print("Min Distance:", min_distance)
