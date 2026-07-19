# Finding a Motif in DNA

## Problem Summary

Given two DNA strings:

- `s` = the DNA sequence
- `t` = the motif (substring)

Find every starting position where `t` appears inside `s`.

Rosalind uses **1-based indexing**, so the reported positions start at 1 instead of 0.

---

## Approach

1. Read the DNA string `s` and motif `t`.
2. Iterate through every possible starting position in `s`.
3. Use string slicing to extract a substring of length `len(t)`.
4. Compare the substring with `t`.
5. If they match, store the current position (converted to 1-based indexing).
6. Write all positions separated by spaces.

---

## What This Exercise Reinforced

- Using string slicing to compare substrings.
- Understanding substring search.
- Working with Python lists to store multiple results.
- Converting between 0-based and 1-based indexing.
- Formatting output for Rosalind problems.

---

## What Could Be Improved

### 1. Iterate over indices directly

Instead of manually maintaining both `i` and `j`, the slice endpoint can be computed directly:

```python
for i in range(len(s)):
    if s[i:i + len(t)] == t:
```

This removes redundant variables and makes the code easier to read.

### 2. Write the output in one statement

Instead of writing each position individually:

```python
for position in positions:
    output_file.write(str(position) + " ")
```

the output can be generated more cleanly:

```python
output_file.write(" ".join(map(str, positions)))
```

This also avoids a trailing space.

### 3. Use context managers for file handling

Using:

```python
with open(...) as file:
```

automatically closes files and is the recommended Python style.

---

## Complexity

Let:

- `n` = length of `s`
- `m` = length of `t`

- Time complexity: **O(n × m)**

Each starting position performs a substring comparison of up to `m` characters.

- Space complexity: **O(k)**

where `k` is the number of motif occurrences stored in the `positions` list.

---

## Takeaway

This problem introduces one of the most common operations in bioinformatics: searching for sequence motifs. It demonstrates how simple string slicing can efficiently solve substring matching problems and lays the foundation for more advanced sequence-search algorithms used in genome analysis.