import random
import time
import matplotlib.pyplot as plt


# QuickSort implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)


# Function to generate random numbers and time sorting
def time_quicksort(n):
    # Generate 'n' random integers
    arr = [random.randint(0, 10000) for _ in range(n)]

    # Measure the time taken to sort
    start_time = time.time()
    quicksort(arr)
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    return elapsed_time


# Values of n to test (you can adjust these for more data points)
n_values = [100, 500, 1000, 2000, 5000, 10000, 20000, 50000]
times = []

# Collect the time taken for each value of 'n'
for n in n_values:
    t = time_quicksort(n)
    times.append(t)
    print(f"Time taken to sort {n} elements: {t:.6f} seconds")

# Plotting the graph
plt.plot(n_values, times, marker='o')
plt.title("Time taken vs Number of elements (n)")
plt.xlabel("Number of elements (n)")
plt.ylabel("Time taken (seconds)")
plt.grid(True)
plt.show()
