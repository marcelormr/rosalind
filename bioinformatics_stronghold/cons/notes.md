# Consensus and Profile

## Problem Summary

Given a collection of DNA strings in FASTA format, determine:

- The consensus string (the most common nucleobase at each position).
- The profile matrix showing how many times each nucleobase appears at every position.

All DNA strings have the same length.

---

## Approach

### 1. Parse the FASTA file

Read the input line by line.

- Header lines begin with `>`.
- Sequence lines are concatenated until the next header is found.
- Each completed DNA sequence is stored in a list.

Don't forget to append the final sequence after the loop finishes.

---

### 2. Create the profile matrix

Create a 4 × n matrix filled with zeros, where:

- Row 0 represents `A`
- Row 1 represents `C`
- Row 2 represents `G`
- Row 3 represents `T`

The number of columns equals the DNA sequence length.

---

### 3. Build the profile matrix

For every DNA sequence:

- Visit each nucleobase.
- Increase the corresponding row at that position.

For example:

- `A` → row 0
- `C` → row 1
- `G` → row 2
- `T` → row 3

After processing all sequences, each column contains the nucleobase frequencies for that position.

---

### 4. Generate the consensus string

For every column of the profile matrix:

- Find the largest value.
- Determine which nucleobase produced that value.
- Append that nucleobase to the consensus string.

---

### 5. Write the output

Write:

1. The consensus string.
2. Each row of the profile matrix in the required Rosalind format.

---

## What This Exercise Reinforced

- Parsing FASTA files with multiline sequences.
- Building a matrix using nested lists.
- Counting frequencies across multiple sequences.
- Traversing rows and columns independently.
- Converting frequency information into a consensus sequence.
- Working with nested loops and indexes.

---

## What Could Be Improved

### 1. Use a dictionary instead of `match`

Instead of matching every nucleobase manually,

```python
match nucleobase:
```

a dictionary can map nucleobases directly to row indices:

```python
row = {"A": 0, "C": 1, "G": 2, "T": 3}
profile_matrix[row[nucleobase]][j] += 1
```

This removes repetitive code and is easier to extend.

### 2. Use `max()` when building the consensus

Instead of manually searching for the largest value with nested loops, Python can determine the maximum directly.

This results in shorter and easier-to-read code.

### 3. Generate row labels from a list

Instead of using `match` to write

```
A:
C:
G:
T:
```

a simple list can be used:

```python
labels = ["A", "C", "G", "T"]
```

which removes another repetitive block of code.

### 4. Separate the solution into functions

The program naturally divides into several tasks:

- Parsing FASTA
- Building the profile matrix
- Building the consensus string
- Writing the output

Separating these into functions would improve readability and reusability.

---

## Complexity

Let:

- **m** = number of DNA strings
- **n** = length of each DNA string

Time complexity: **O(m × n)**

Every nucleobase is processed exactly once.

Space complexity: **O(m × n)**

The DNA sequences are stored in memory, along with a profile matrix of fixed height (4 rows).

---

## Takeaway

This problem combines biological sequence processing with frequency counting.

It introduces an important bioinformatics concept—the profile matrix—which forms the basis for multiple sequence alignment, motif discovery, and consensus sequence generation. It also reinforces parsing FASTA files and organizing information in matrix form.