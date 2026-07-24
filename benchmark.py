import time
import numpy as np

# Size of the dataset
N = 1000000

# 1. Slow Pure Python Loop
def slow_loop(arr):
    result = []
    for x in arr:
        result.append(x * 2 + 5)
    return result

# 2. Fast Vectorized Hyper-Drive Implementation
def fast_vectorized(arr):
    return arr * 2 + 5

if __name__ == "__main__":
    data_list = list(range(N))
    data_array = np.arange(N)
    
    print("Running performance benchmarks...")
    
    start = time.time()
    res_slow = slow_loop(data_list)
    end = time.time()
    time_slow = end - start
    print(f"Pure Python Loop Time: {time_slow:.4f} seconds")
    
    start = time.time()
    res_fast = fast_vectorized(data_array)
    end = time.time()
    time_fast = end - start
    print(f"Vectorized Hyper-Drive Time: {time_fast:.4f} seconds")
    
    print(f"--> Speedup Factor: {time_slow / time_fast:.1f}x Faster!")
