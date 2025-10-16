# Fast Fibonacci Calculation using Python's `lru_cache`

This script demonstrates a classic recursive function (Fibonacci sequence) and uses a powerful Python built-in feature to make it **exponentially faster**.

## 💡 The Clever Trick: Memoization

The standard recursive calculation for the $n$-th Fibonacci number is extremely slow because it recalculates the same values over and over again (e.g., to find Fib(5), you calculate Fib(3) twice). This results in $O(2^n)$ complexity.

By applying the built-in `@functools.lru_cache` decorator, we implement **memoization** (a form of dynamic programming). This technique automatically stores the result of every function call and, if the function is called again with the same input, it returns the cached result instantly, reducing the complexity to $O(n)$.

## ⚙️ How to Run

1.  Save the code as `fast_fibonacci.py`.
2.  Run the script from your terminal:

```bash
python fast_fibonacci.py