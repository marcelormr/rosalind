# Translating RNA into Protein

## Problem Summary

Given an RNA string representing an mRNA strand, translate it into the corresponding protein string using the RNA codon table.

Each group of three RNA nucleotides (codon) corresponds to:
- One amino acid
- Or a stop signal that ends translation

The output should be the amino acid sequence encoded by the RNA string.

---

## Approach

1. Create a dictionary containing the RNA codon table:
   - Key = RNA codon (three nucleotides)
   - Value = corresponding amino acid

2. Read the RNA sequence from the input file.

3. Iterate through the RNA string and build codons:
   - Add each nucleotide to the current codon
   - Once three nucleotides are collected, translate the codon

4. Append the translated amino acid to the protein string.

5. Stop translation when a stop codon (`UAA`, `UAG`, or `UGA`) is reached.

6. Write the resulting protein sequence to the output file.

---

## What This Exercise Reinforced

- Using dictionaries as lookup tables for biological data.
- Translating between biological representations:
  - DNA → RNA → Protein
- Processing sequences in fixed-size groups.
- Using codons as the fundamental unit of translation.
- Applying conditional termination with stop codons.

---

## What Could Be Improved

### 1. Use slicing instead of manually building codons

The current solution manually creates codons using `current_codon`.

A more Pythonic approach is iterating in steps of three:

```python
for i in range(0, len(rna_string), 3):
    codon = rna_string[i:i+3]
```
This makes the codon grouping logic clearer.

### 2. Use with open() for file handling

The current approach manually opens and closes files.

Using context managers:
```python
with open("file.txt") as file:
```
automatically closes files and prevents resource leaks.

### 3. Store the codon table separately

The codon table is biological reference data, not part of the algorithm itself.

Keeping it in:

- a separate file
- a constant module
- or a reusable dictionary

would improve organization.

---

## Complexity

Let n be the length of the RNA sequence.

- Time complexity: O(n)

Each nucleotide is processed once.

- Space complexity: O(n)

The resulting protein string is stored in memory.

The codon table requires constant additional space.

---

## Takeaway

RNA translation is a fundamental bioinformatics operation that converts nucleotide information into protein information.

This problem introduces an important programming pattern: using dictionaries as biological lookup tables. The same approach is used in larger bioinformatics tasks involving sequence annotation, mutation analysis, and genome interpretation.
