import sys

lst = []
capacity = sys.getsizeof(lst)
print(f"List capacity: {capacity} bytes")

for i in range(64):
    lst.append(i)
    new_capacity = sys.getsizeof(lst)
    if new_capacity != capacity:
        print(f"List capacity changed from {capacity} bytes to {new_capacity} bytes at size {i}")
        capacity = new_capacity
