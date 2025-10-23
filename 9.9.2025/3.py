"""import math
def swap_coordinates(point):
    x, y = point
    return (y, x)

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

p1 = (1, 2)
p2 = (2, 3)

print("Swapped p1", swap_coordinates(p1))
print("Distance between p1 and p2", calculate_distance(p1, p2))"""

import math
def swap_coordinates(point):
    x, y = point
    return (y, x)

point = (int(input("Give x-coordinate: ")), int(input("Give y-coordinate: ")))
new_point = swap_coordinates(point)
print(f"Swapped: {new_point}")

point1 = (int(input("Give x1-coordinate: ")), int(input("Give y1-coordinate: ")))
point2 = (int(input("Give x2-coordinate: ")), int(input("Give y2-coordinate: ")))
def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

print("Distance between p1 and p2", calculate_distance(point1, point2))


