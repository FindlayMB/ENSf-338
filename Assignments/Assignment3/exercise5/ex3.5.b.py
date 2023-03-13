import time
import random
import heapq
import statistics
import matplotlib.pyplot as plt

class InefficientPriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)
        self.queue.sort(reverse=True)

    def pop(self):
        return self.queue.pop(0)

class EfficientPriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        heapq.heappush(self.queue, item)

    def pop(self):
        return heapq.heappop(self.queue)

num_measurements = 100
measurement_results_inefficient = []
measurement_results_efficient = []

n = 1000
nums = [random.randint(0, n) for _ in range(n)]

for i in range(num_measurements):
    pq1 = InefficientPriorityQueue()
    pq2 = EfficientPriorityQueue()

    start1 = time.time()
    for num in nums:
        pq1.push(num)
    for _ in range(n):
        pq1.pop()
    end1 = time.time()

    start2 = time.time()
    for num in nums:
        pq2.push(num)
    for _ in range(n):
        pq2.pop()
    end2 = time.time()

    measurement_results_inefficient.append(end1 - start1)
    measurement_results_efficient.append(end2 - start2)

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

axs[0].hist(measurement_results_inefficient, bins=10)
axs[0].set_title('Inefficient Implementation')
axs[0].set_xlabel('Execution Time (s)')
axs[0].set_ylabel('Frequency')

axs[1].hist(measurement_results_efficient, bins=10)
axs[1].set_title('Efficient Implementation')
axs[1].set_xlabel('Execution Time (s)')
axs[1].set_ylabel('Frequency')

plt.show()

print(f"Aggregate of measured values for inefficient implementation: {min(measurement_results_inefficient):.6f} seconds")
print(f"Aggregate of measured values for efficient implementation: {statistics.mean(measurement_results_efficient):.6f} seconds")
