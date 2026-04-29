# DNA - Counting DNA Nucleotides

## Problem Summary

Given a DNA string, count how many times each nucleotide appears.

The required output order is:

A C G T

---

## Approach

Use four separate counters:

- `a_counter`
- `c_counter`
- `g_counter`
- `t_counter`

Loop through each character in the DNA string:

- if character is `A`, increment `a_counter`
- if character is `C`, increment `c_counter`
- if character is `G`, increment `g_counter`
- if character is `T`, increment `t_counter`

Finally, print the four values in the required order.

---

## What This Exercise Reinforced

- Iterating through strings character by character
- Using `if / elif` conditional branching
- Frequency counting using counters
- Producing clean formatted output

---

## Common Pitfalls

- Printing counts in the wrong order
- Using multiple `if` statements instead of `elif`
- Adding unnecessary validation for invalid characters
- Forgetting that Rosalind guarantees valid DNA input

---

## Complexity

- Time complexity: O(n), where n is the length of the DNA string
- Space complexity: O(1), since only four counters are used

---

## Takeaway

This is the basic counting pattern used throughout bioinformatics. Many larger problems begin with simple symbol frequency counting, especially in DNA, RNA, and protein sequence analysis.
