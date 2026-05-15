# RNA - Transcribing DNA into RNA

## Problem Summary

Given a DNA string, create its RNA equivalent by replacing every thymine nucleotide (`T`) with uracil (`U`).

DNA nucleotides:
- A
- C
- G
- T

RNA nucleotides:
- A
- C
- G
- U

---

## Approach

Start with an empty RNA string.

Loop through each nucleotide in the DNA sequence:
- if the nucleotide is `T`, append `U`
- otherwise, append the original nucleotide

Finally, print the completed RNA string.

---

## What This Exercise Reinforced

- Iterating through strings character-by-character
- Building strings dynamically
- Using `if / else` conditional logic
- Understanding basic DNA → RNA transcription rules

---

## Common Pitfalls

- Forgetting that RNA uses `U` instead of `T`
- Accidentally modifying the original string directly
- Replacing the wrong nucleotide
- Forgetting to append non-`T` characters

---

## Alternative Approach

This problem could also be solved more simply using Python's built-in `.replace()` method:

```python
u = t.replace('T', 'U')
```

This is cleaner and more efficient.

However, solving the problem manually with a loop reinforces:

- string iteration
- conditional branching
- manual string construction

---

## Complexity
- Time complexity: O(n)
- Space complexity: O(n)

Where n is the length of the DNA string.

---

## Takeaway

Many bioinformatics problems involve transforming biological sequences according to fixed substitution rules. This exercise introduces sequence transformation while reinforcing core string manipulation fundamentals in Python.
