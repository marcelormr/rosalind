# Problem Summary

Given two positive integers `a` and `b` where `a < b`,
calculate the sum of all odd integers from `a` through `b`,
including both endpoints.

# Approach

I used a `for` loop with:

`range(a, b + 1)`

to ensure the final value `b` was included.

For each number, I checked whether it was odd using:

`i % 2 == 1`

If true, the value was added to the variable `total`,
which stores the running sum.

After the loop finished, I printed the final result.

# What This Exercise Reinforced

- `for` loops
- conditional statements with `if`
- modulo operator `%`
- accumulator pattern for summation
- inclusive ranges using `b + 1`

# Common Pitfalls

A common mistake is forgetting that `range()` excludes the final value.

Using:

`range(a, b)`

would incorrectly skip `b`.

Another common issue is misunderstanding odd-number checks.
Using `% 2 == 1` correctly identifies odd integers.

# Complexity

Time complexity: O(n)

where `n = b - a`, since each integer in the interval is checked once.

Space complexity: O(1)

Only a few variables are used regardless of input size.

# Takeaway

This exercise reinforced one of the most common programming patterns:
iterating through a range, applying a condition, and accumulating a result.

This logic appears frequently in data filtering and sequence processing tasks.
