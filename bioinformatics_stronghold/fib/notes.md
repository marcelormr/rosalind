# FIB - Rabbits and Recurrence Relations

## Problem Summary

Starting with one rabbit pair, calculate how many rabbit pairs exist after `n` months.

Each reproduction-age rabbit pair produces `k` new rabbit pairs every month.

The population follows a modified Fibonacci recurrence relation.

---

## Recurrence Relation

The rabbit population is defined by:

```text id="fib3"
F(n) = F(n-1) + k * F(n-2)
```

Where:

- F(n-1) = rabbits alive last month
- F(n-2) = rabbits old enough to reproduce
- k = number of offspring pairs produced

Base cases:

- F(1) = 1
- F(2) = 1

---

## Approach

Track:

- previous generation
- current generation

For each month:

1. Calculate the next generation
2. Shift variables forward
3. Repeat until reaching month n

This avoids storing the entire sequence.

---

## What This Exercise Reinforced

- Recurrence relations
- Iterative dynamic programming
- State transition logic
- Variable updating patterns
- Fibonacci-style sequence generation

---

## Common Pitfalls

- Updating variables in the wrong order
- Forgetting to multiply by k
- Off-by-one errors in loop conditions
- Confusing current vs previous generation values

---

## Alternative Approaches

This problem could also be solved using:

- recursion
- memoization
- arrays/lists storing all generations

However, iterative variable tracking is:

- simpler
- faster
- more memory efficient

---

## Complexity

- Time complexity: O(n)
- Space complexity: O(1)

Only a fixed number of variables are stored regardless of input size.

---

## Takeaway

This exercise introduces dynamic programming through recurrence relations. Many computational biology problems use similar state-transition patterns to model population growth, probabilities, and sequence evolution.
