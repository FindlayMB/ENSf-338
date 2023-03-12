import sys

old_capacity = 0
lst = []

for i in range(64):
    lst.append(i)
    new_capacity = sys.getsizeof(lst)
    if new_capacity != old_capacity:
        print(f"Capacity changed from {old_capacity} bytes to {new_capacity} bytes at {i} elements")
        old_capacity = new_capacity
