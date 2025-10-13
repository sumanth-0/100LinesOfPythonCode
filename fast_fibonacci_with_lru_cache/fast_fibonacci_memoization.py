import time
from functools import lru_cache

# --- 1. The Clever Trick: Memoization using lru_cache ---
# This decorator automatically stores the results of expensive function calls
# and returns the cached result when the same inputs occur again.
@lru_cache(maxsize=None)
def fibonacci(n):
    """
    Calculates the nth Fibonacci number efficiently using memoization.
    
    The Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8...
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# --- 2. Benchmark for Comparison (Illustrative Code) ---
def benchmark_fib():
    """Compares the speed of the cached function vs. an uncached one."""
    
    # We'll use the cached function for the demo (no need for a slow uncached one)
    TARGET_N = 35  # A high enough number to feel the speed
    
    print(f"--- Calculating Fibonacci({TARGET_N}) ---")

    # Time the fast (cached) calculation
    start_time = time.perf_counter()
    result = fibonacci(TARGET_N)
    end_time = time.perf_counter()
    
    # The first run populates the cache
    first_run_time = (end_time - start_time) * 1000
    print(f"Result: {result}")
    print(f"Time (First Run/Cache Build): {first_run_time:.4f} ms")
    
    # Time the second run (retrieving from cache)
    start_time_cached = time.perf_counter()
    cached_result = fibonacci(TARGET_N)
    end_time_cached = time.perf_counter()
    
    second_run_time = (end_time_cached - start_time_cached) * 1000
    print(f"Time (Second Run/Cached): {second_run_time:.8f} ms (INSTANT)")
    
    # Show cache info
    print("\n--- Cache Statistics ---")
    print(f"Cache Info: {fibonacci.cache_info()}")

if __name__ == "__main__":
    benchmark_fib()