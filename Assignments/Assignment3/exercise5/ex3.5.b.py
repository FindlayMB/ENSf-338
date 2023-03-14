from timeit import timeit
import random
import heapq
import matplotlib.pyplot as plt
import numpy as np


class InefficientPriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)
        self.queue.sort(reverse=True)

    def pop(self):
        if len(self.queue) == 0:
            return None
        max_value = self.queue[0]
        max_index = 0
        for i in range(1, len(self.queue)):
            if self.queue[i] > max_value:
                max_value = self.queue[i]
                max_index = i
        del self.queue[max_index]
        return max_value


class EfficientPriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        heapq.heappush(self.queue, item)

    def pop(self):
        return heapq.heappop(self.queue)


insert_time_inefficient = []
insert_time_efficient = []

extract_time_inefficient = []
extract_time_efficient = []

nums = [random.randint(0, 1000) for _ in range(0, 1000)]

pq1 = InefficientPriorityQueue()
pq2 = EfficientPriorityQueue()


for i in range(1000):

    insert_time_inefficient.append(
        timeit(lambda: [pq1.push(j) for j in nums], number=1)
    )
    extract_time_inefficient.append(
        timeit(lambda: [pq1.pop() for j in nums], number=1)
    )

    insert_time_efficient.append(
        timeit(lambda: [pq2.push(j) for j in nums], number=1)
    )
    extract_time_efficient.append(
        timeit(lambda: [pq2.pop() for j in nums], number=1)
    )


print("Aggregate of measured values:")
print("Insertion timing:")
print(f"Efficient implementation: {np.mean(insert_time_efficient):.6f}")
print(f"Inefficient implementation: {np.mean(insert_time_inefficient):.6f}")
print("\nExtraction timing:")
print(f"Efficient implementation: {np.mean(extract_time_efficient):.6f}")
print(f"Inefficient implementation: {np.mean(extract_time_inefficient):.6f}")


plt.figure(1)
plt.hist([insert_time_efficient, insert_time_inefficient],
         alpha=1, bins=10, label=["efficient", "inefficient"])
plt.title('Insertion timing')
plt.xlabel('Execution Time (s)')
plt.ylabel('Frequency')
plt.legend()

plt.figure(2)
plt.hist([extract_time_efficient, extract_time_inefficient],
         alpha=1, bins=10, label=["efficient", "inefficient"])
plt.title('Extraction timing')
plt.xlabel('Execution Time (s)')
plt.ylabel('Frequency')
plt.legend()

plt.show()
