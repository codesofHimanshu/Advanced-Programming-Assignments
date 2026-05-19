import sys
import gc

class Node:
    def __init__(self, name):
        self.name = name
        self.link = None

    def __del__(self):
        print(f"{self.name} is being destroyed")


print("=== Creating Nodes ===")
A = Node("A")
B = Node("B")

# Create circular reference
A.link = B
B.link = A

print("\n=== Reference Counts ===")
print("Reference count of A:", sys.getrefcount(A))
print("Reference count of B:", sys.getrefcount(B))

# Store object IDs
a_id = id(A)
b_id = id(B)

print("\n=== Deleting Direct References ===")
del A
del B

print("A and B variables deleted.")

print("\n=== Investigating Memory Before GC ===")

found_a = False
found_b = False

for obj in gc.get_objects():
    if id(obj) == a_id:
        found_a = True
    if id(obj) == b_id:
        found_b = True

print("Node A still exists in memory:", found_a)
print("Node B still exists in memory:", found_b)

print("\n=== Running Garbage Collector ===")
unreachable = gc.collect()

print("Unreachable objects collected:", unreachable)

print("\n=== Investigating Memory After GC ===")

found_a = False
found_b = False

for obj in gc.get_objects():
    if id(obj) == a_id:
        found_a = True
    if id(obj) == b_id:
        found_b = True

print("Node A still exists in memory:", found_a)
print("Node B still exists in memory:", found_b)