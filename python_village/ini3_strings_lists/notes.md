# Problem Summary

Given a string and four integer indices `a`, `b`, `c`, and `d`,
extract two substrings:

- from index `a` through `b`
- from index `c` through `d`

and print them separated by a space.

Unlike normal Python slicing, the ending indices must be included.

# Approach

I stored the full string in `s` and used slicing to extract both parts.

Since Python slices exclude the final index, I used:

`s[a:b+1]`

and

`s[c:d+1]`

to make the ranges inclusive.

The two substrings were joined with a space between them and printed.

# What This Exercise Reinforced

- string slicing
- zero-based indexing
- inclusive vs exclusive slice boundaries
- string concatenation

# Common Pitfalls

The main mistake would be forgetting that Python slicing excludes the
ending index.

Using:

`s[a:b]`

would incorrectly omit `s[b]`.

Another common issue is confusion with indexing, since Python starts
counting from 0 rather than 1.

# Takeaway

This exercise reinforced careful handling of slice boundaries and showed
how Python string slicing follows the same rules as list slicing.

This pattern is especially useful in sequence manipulation tasks,
which is highly relevant for bioinformatics work.
