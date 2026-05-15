# REVC - Complementing a Strand of DNA

## Problem Summary

Given a DNA sequence, generate its reverse complement.

DNA complementary pairs:
- A ↔ T
- C ↔ G

The reverse complement is created by:
1. Reversing the DNA sequence
2. Replacing each nucleotide with its complement

---

## Approach

First, reverse the original DNA sequence manually.

Then, loop through the reversed sequence:
- replace `A` with `T`
- replace `T` with `A`
- replace `C` with `G`
- replace `G` with `C`

Build the reverse complement string one character at a time.

---

## What This Exercise Reinforced

- String iteration
- Building strings dynamically
- Using conditional branching with `if / elif`
- Understanding biological base pairing rules
- Multi-step sequence transformations

---

## Common Pitfalls

- Forgetting to reverse before complementing
- Mixing up complement pairs
- Accidentally complementing the original string instead of the reversed string
- Rebuilding strings inefficiently without understanding immutability

---

## Alternative Approaches

Python allows shorter solutions using:
- slicing (`s[::-1]`) for reversing
- dictionaries for nucleotide mapping
- `.replace()` chains

Example:

```python
reverse_sequence = s[::-1]
```

However, manually implementing the logic reinforces:

- sequence manipulation fundamentals
- loop construction
- explicit transformation logic

---

## Complexity
- Time complexity: O(n)
- Space complexity: O(n)

Where n is the length of the DNA sequence.

## Takeaway

Reverse complements are fundamental in bioinformatics because DNA is double-stranded. Many sequence analysis tasks require converting between strands using reverse complement operations.
