# take home assessment from layup parts
# Name: David D

import time
import matplotlib.pyplot as plt

def compute_sequence(n_target):
    if not isinstance(n_target, int) or n_target <= 0:
        return "Input n must be postiive and must be an integer"
    if n_target == 1:
        return 1
    if n_target == 2:
        return 2
    
    s_n_minus_2 = 1
    s_n_minus_1 = 2
    
    for n in range(3, n_target + 1):
        if n % 2 == 0: # n is even
            s_n = s_n_minus_1 + s_n_minus_2
        else: # n is odd
            s_n = 2 * s_n_minus_1 - s_n_minus_2

        s_n_minus_2 = s_n_minus_1
        s_n_minus_1 = s_n
    
    # After the loop, s_n_minus_1 would hold the value for S(n_target)
    return s_n_minus_1

def measure_performance():
    # measuring and ploting the runtime performance for different values of n
    
    n_values = [100, 1000, 2000, 4000, 6000, 8000, 10000]
    runtimes = []
    
    for n in n_values:
        start_time = time.time()
        result = compute_sequence(n)
        end_time = time.time()
        runtime = end_time - start_time
        
        runtimes.append(runtime)
        print(f"S({n}) = {result}, Runtime: {runtime:.6f} seconds")
    
    # Plot runtime vs n
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, runtimes, marker='o', color='blue')
    plt.title('Runtime vs n for Layup Sequence')
    plt.xlabel('n')
    plt.ylabel('Runtime (seconds)')
    plt.grid(True)
    plt.savefig('layup_sequence_runtime.png')
    
    return n_values, runtimes

if __name__ == "__main__":
    # part 1: Algorithm Implementation
    n_value = 10000
    start_time = time.time()
    result = compute_sequence(n_value)
    total_runtime = time.time() - start_time
    
    print(f"S({n_value}) = {result}")
    print(f"Runtime: {total_runtime:.6f} seconds")
    print(f"----------------------------------------------------------------------------------------------------------------------------------")
    
    # Part 2: Performance Evaluation
    print("\nMeasuring performance for different values of n")
    n_values, runtimes = measure_performance()
    
    
    """
    REPORT

    2b. Time Complexity Analysis:
    O(n)

    3a. Explanation

    The algorithm has a time complexity of O(n) for each value from 3 to n. A constant 
    number of operations are performed when checking if n is even or odd and performing
    arithmetic. Since we calculate each term exactly once, sequenctially, the time
    complexity is n and grows linearly.

    Space Complexity Analysis: (just a side note)

    The space complexity is O(1) because only three variables are stored
    (s_n_minus_2, s_n_minus_1, and s_n) which stay the same regardless
    of the input size.

    3b. Optimizations:
    1. Using iterative approach instead of recursive to avoid stack overflow issues for
    large n values like 10,000
    
    2. Using constant space, where I only stored the two previous sequence values 
    instead of the entire sequence which reduced memory from O(n) to O(1)

    3. No repeat calculations, where each value in the sequence is computed only once.
    In recursive approach, it would recalculate values which is not efficent.

    """