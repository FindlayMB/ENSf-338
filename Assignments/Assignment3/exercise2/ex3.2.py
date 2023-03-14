import json
import time
import matplotlib.pyplot as plt
from timeit import timeit
# Load the data from ex2data.json and ex2task.json


def binary_search(data, target, midpoint):
    """
    Perform a binary search on the given array to find the target value.
    :param arr: The array to search.
    :param target: The value to search for.
    :param first_midpoint: The initial midpoint to use (optional).
    :return: The index of the target value, or -1 if not found.
    """
    left = 0
    right = len(data) - 1

    while left <= right:
        if data[midpoint] == target:
            return midpoint
        elif data[midpoint] < target:
            left = midpoint + 1
        else:
            right = midpoint - 1

        midpoint = (left + right) // 2

    return -1


def time_binary_search(arr, task, midpoints):
    """
    Time the performance of binary search on the given array for the given task number.
    :param arr: The array to search.
    :param target: The value to search for.
    :param task_num: The task number.
    :return: The best midpoint for the task and the time taken for that midpoint.
    """
    best_time = -1
    best_midpoint = 0
    target = task['target']
    for midpoint in midpoints:
        time_taken = timeit(lambda: binary_search(
            arr, target, midpoint), number=100)
        task['timeList'].append(time_taken)
        if time_taken < best_time or best_time == -1:
            best_time = time_taken
            best_midpoint = midpoint

    task['bestMid'] = best_midpoint
    task['bestTime'][0] = best_time
    task['bestTime'][1] = timeit(lambda: binary_search(
        arr, target, (len(data)//2)), number=100)
    return best_midpoint, best_time


# Load the data from ex2data.json and ex2task.json
with open('ex2data.json', 'r') as f:
    data = json.load(f)
    # Convert keys to strings for each dictionary in the list
    # data = [{str(k): v for k, v in d.items()} for d in data]

with open('ex2tasks.json', 'r') as file:
    tasks = json.load(file)
    # Convert keys to strings for each dictionary in the list
    tasks = [{'target': d,
              'bestMid': 0,
              'bestTime': [0, 0],
              'timeList': []} for d in tasks]

# List to store chosen midpoints for each task
midpoints = [i*50000 + 50000 for i in range(0, 19)]
# Time the performance of binary search for each task
for i, task in enumerate(tasks):
    best_midpoint, best_time = time_binary_search(data, task, midpoints)

    print(
        f"Task {i}: Best midpoint is {best_midpoint} with time {best_time:.6f}")

# time list for times of the normal midpoint
timeNMList = [task['bestTime'][1] for task in tasks]

# time list for times of the best midpoint
timeBMList = [task['bestTime'][0] for task in tasks]

MPList = [task['bestMid'] for task in tasks]

test = [task['target'] for task in tasks]
plt.figure(1)
plt.scatter(test, MPList)
plt.yticks([i*50000 + 50000 for i in range(0, 19)])

plt.figure(2)
plt.scatter(range(0, len(tasks)), timeNMList, label="Normal midpoint")
plt.scatter(range(0, len(tasks)), timeBMList, label="Best midpoint")


plt.xlabel('Task')
plt.ylabel('Time for best midpoint')
plt.title('Chosen Midpoints for Binary Search')
plt.legend()
plt.show()