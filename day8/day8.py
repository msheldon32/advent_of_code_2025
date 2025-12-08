import sys
import math
import heapq

class Node:
    def __init__(self):
        self.n_children = 1
        self.parent = None

    def get_root(self):
        if not self.parent:
            return self
        self.parent = self.parent.get_root()
        return self.parent

    def union(self, other):
        root = self.get_root()
        other_root = other.get_root()

        if root == other_root:
            return

        if other_root.n_children > root.n_children:
            root, other_root = other_root, root

        other_root.parent = root
        root.n_children += other_root.n_children

TEST = sys.argv[1] == "1"

if TEST:
    filename = "input2"
    n_links = 10
else:
    filename = "input"
    n_links = 1000

points = []

with open(filename) as f:
    for row in f:
        points.append([int(x) for x in row.strip().split(",")])

def get_distance(a, b):
    # squared euclidian distance
    return sum([(x-y)**2 for x, y in zip(a,b)])

distances = []
nodes = [Node() for x in points]

for i, point1 in enumerate(points):
    for r, point2 in enumerate(points[i+1:]):
        j = i+1+r
        d = get_distance(point1, point2)
        heapq.heappush(distances, (d,i,j))

links_seen = 0

while distances and links_seen < n_links:
    if not distances:
        break
    d, i, j = heapq.heappop(distances)
    if nodes[i].get_root() != nodes[j].get_root():
        nodes[i].union(nodes[j])
    links_seen += 1

largest_circuits = []
circuits = []
seen_circuits = set()

for node in nodes:
    root = node.get_root()
    if root not in seen_circuits:
        seen_circuits.add(root)
        circuits.append(root.n_children)

        if (len(largest_circuits) < 3) or root.n_children > largest_circuits[0]:
            largest_circuits.append(root.n_children)
            largest_circuits.sort()
            if len(largest_circuits) > 3:
                largest_circuits.pop(0)

acc = 1
for c in largest_circuits:
    acc *= c
print(f"Product of largest circuits: {acc}")

# Part 2: add the rest
last_c = 0
while distances:
    d, i,j = heapq.heappop(distances)
    if nodes[i].get_root() != nodes[j].get_root():
        last_c = points[i][0] * points[j][0]
        nodes[i].union(nodes[j])

print(f"Last connection: {last_c}")
