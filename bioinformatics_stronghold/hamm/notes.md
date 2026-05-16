# Counting Point Mutations (Hamming Distance)

## Problem Summary
Given two DNA strings of equal length, compute the Hamming distance, i.e., the number of positions where the two strings differ.

---

## What the solution does
The solution:
- Reads two DNA strings from a file
- Iterates through both strings position by position
- Counts mismatches between corresponding characters
- Outputs the total number of mismatches

---

## What could be improved

### 1. Avoid manual indexing
Using a `while` loop with `position` is error-prone and unnecessary in Python.

Better approach:
- Use `zip(s, t)` for direct pairwise iteration
- Removes need for indexing and length tracking

---

### 2. Handle newline characters properly
`readline()` includes `\n`, which can silently affect logic.

Better approach:
- Use `.strip()` when reading input strings

---

### 3. Avoid off-by-one adjustments
`len(s) - 1` is a workaround for newline handling, not a real fix.

Correct approach:
- Clean input first instead of adjusting length manually

---

### 4. Improve readability
The current version uses:
- manual counters
- explicit indexing
- loop control variables

This makes the code harder to read than necessary for a simple comparison task.

---

## Cleaner pattern (recommended)
- Iterate directly over paired characters
- Use `zip`
- Keep logic minimal

---

## Complexity
- Time: O(n), where n is string length
- Space: O(1)

---

## Takeaway
This problem is fundamentally about pairwise comparison. In Python, idiomatic iteration (`zip`) is preferred over manual indexing for correctness, clarity, and reduced risk of boundary errors.
