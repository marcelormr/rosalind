# GC - Computing GC Content

## Problem Summary

Given multiple DNA sequences in FASTA format, determine which sequence has the highest GC-content.

GC-content is the percentage of bases in a DNA sequence that are either:
- `G`
- `C`

The output must contain:
1. The ID of the sequence with highest GC-content
2. Its GC-content percentage

---

## FASTA Format

FASTA files contain:
- a header line beginning with `>`
- one or more sequence lines below it

Example:

```text
>Rosalind_6404
CCTGCGGAAGATCG
GCACTAGAATAGC
```
Important detail:

- sequence data may span multiple lines
- all lines below a header belong to that sequence until the next >

---

## Approach

1. Parse FASTA Data

Use:

- dictionary keys = sequence IDs
- dictionary values = full DNA sequences

Maintain a `current_id` variable to remember which sequence is currently being built.

When a line starts with `>`:
- create a new dictionary entry
- update `current_id`

Otherwise:
- append the DNA line to the current sequence

---

2. Compute GC Content

For each sequence:
- count how many bases are `G` or `C`
- divide by total sequence length
- multiply by 100

Formula:

GC-content = (GC count / total length) × 100

---

3. Find Maximum GC Content

Loop through all computed GC percentages:

- track highest value found so far
- track corresponding sequence ID

---

## What This Exercise Reinforced

- Parsing FASTA formatted files
- Dictionary usage for sequence storage
- Stateful parsing using `current_id`
- String accumulation with `+=`
- Frequency counting patterns
- Percentage calculations
- Multi-pass data processing

---

## Common Pitfalls
- Resetting `current_id` inside the loop
Forgetting to remove `>`
Replacing sequences instead of appending
Using DNA sequence lines as dictionary keys
Forgetting .strip()`
Dividing by incorrect total length

---

## Complexity

Let:
- `n` = total number of nucleotides

### Time Complexity
- O(n)
Each nucleotide is processed a constant number of times.

### Space Complexity
- O(n)
All DNA sequences are stored in memory.

---

## Takeaway
This exercise introduces one of the most fundamental bioinformatics tasks: 
parsing FASTA files.

FASTA parsing appears constantly in:

- genome analysis
- sequence alignment
- BLAST workflows
- motif finding
- phylogenetics
- real-world bioinformatics pipelines

Understanding how to structure and process biological sequence data is more important here than the GC calculation itself.
