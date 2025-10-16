# Fibonacci Sequence Generator

This program generates the Fibonacci sequence up to a specified number of terms.

## Problem Statement

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. The task is to write a Python program that generates the Fibonacci sequence up to `n` terms, where `n` is provided by the user.

## Example

If the user enters `n = 7`, the output should be:

```
Fibonacci sequence:
0
1
1
2
3
5
8
```

## Constraints

- The input `n` will be a non-negative integer.
- The program should handle `n = 0` and `n = 1` correctly.

## Complexity Analysis

- **Time Complexity**: O(n), where `n` is the number of terms. The program iterates `n` times to generate the sequence.
- **Space Complexity**: O(n), as we store the Fibonacci numbers in a list.