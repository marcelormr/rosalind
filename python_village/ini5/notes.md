# Problem Summary

Given a text file with multiple lines, create a new file containing
only the even-numbered lines from the original file, using 1-based numbering.

This means keeping lines 2, 4, 6, and so on.

# Approach

I opened the input file in read mode and used `readlines()`
to store all lines in a list.

Then I opened a second file in write mode for the output.

Using a counter starting at `0`, I iterated through each line and checked:

`lineCounter % 2 == 1`

This selects indices `1, 3, 5...`, which correspond to lines
2, 4, 6... because Python uses zero-based indexing.

Matching lines were written to the output file.

# What This Exercise Reinforced

- file handling with `open()`
- reading files using `readlines()`
- writing files using `write()`
- iteration with `for`
- modulo operator `%`
- zero-based indexing

# Common Pitfalls

The main confusion is that checking for odd indices produces
even-numbered lines from a human perspective.

This happens because Python starts counting from 0.

Another possible issue is forgetting that write mode (`w`)
overwrites the existing file.

# Complexity

Time complexity: O(n)

Each line is checked once.

Space complexity: O(n)

Because `readlines()` stores the full file in memory.

This could be improved by iterating directly over the file object
instead of loading the entire file at once.

# Takeaway

This exercise reinforced the relationship between file I/O and indexing logic.

Understanding zero-based indexing is especially important when handling
structured biological data such as FASTA files, tabular results,
and pipeline-generated reports.
