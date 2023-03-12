import json
import time
import matplotlib.pyplot as plt

# Load the data from ex2data.json and ex2task.json
def time_binary_search(arr, target, task_num):
    """
    Time the performance of binary search on the given array for the given task number.
    :param arr: The array to search.
    :param target: The value to search for.
    :param task_num: The task number.
    :return: The best midpoint for the task and the time taken for that midpoint.
    """
    task = tasks[str(task_num)]
    midpoints = task['midpoints']
    best_time = float('inf')
    best_midpoint = None
    
    for midpoint in midpoints:
        start_time = time.time()
        binary_search(arr, target, midpoint)
        end_time = time.time()
        time_taken = end_time - start_time
        
        if time_taken < best_time:
            best_time = time_taken
            best_midpoint = midpoint
    
    return best_midpoint, best_time

# Load the data from ex2data.json and ex2task.json
# Load the data from ex2data.json and ex2task.json
# Load the data from ex2data.json and ex2task.json
# Load the data from ex2data.json and ex2task.json
# Load the data from ex2data.json and ex2task.json
# Load the data from ex2data.json and ex2task.json
with open('ex2data.json', 'r') as f:
    data = json.load(f)
    data = [{str(k): v for k, v in d.items()} for d in data] # Convert keys to strings for each dictionary in the list

with open('ex2tasks.json', 'r') as file:
    tasks = json.load(file)
    tasks = [{str(k): v for k, v in d.items()} for d in tasks] # Convert keys to strings for each dictionary in the list

# List to store chosen midpoints for each task
midpoints = []

# Time the performance of binary search for each task
for i in range(1, 4):
    task = tasks[i-1]
    arr = data[task['data']]
    target = task['target']
    
    best_midpoint, best_time = time_binary_search(arr, target, i)
    
    midpoints.append(best_midpoint)
    print(f"Task {i}: Best midpoint is {best_midpoint} with time {best_time:.5f}")

# Create scatter plot of task and corresponding chosen midpoint
plt.scatter(range(1, 4), midpoints)
plt.xlabel('Task')
plt.ylabel('Chosen Midpoint')
plt.title('Chosen Midpoints for Binary Search')
plt.show()



def binary_search(arr, target, first_midpoint=None):
    """
    Perform a binary search on the given array to find the target value.
    :param arr: The array to search.
    :param target: The value to search for.
    :param first_midpoint: The initial midpoint to use (optional).
    :return: The index of the target value, or -1 if not found.
    """
    left = 0
    right = len(arr) - 1
    
    if first_midpoint is None:
        midpoint = (left + right) // 2
    else:
        midpoint = first_midpoint
    
    while left <= right:
        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] < target:
            left = midpoint + 1
        else:
            right = midpoint - 1
            
        midpoint = (left + right) // 2
    
    return -1
