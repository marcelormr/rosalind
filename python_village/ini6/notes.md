# INI6 - Dictionaries (Word Frequency)

## Problem
Count how many times each word appears in a given string. Words are separated by spaces and are case-sensitive.

## Idea
Use a dictionary to map each word to its frequency.

- Key = word
- Value = number of occurrences

## Approach

1. Create an empty dictionary
2. Split the string into words using `.split(' ')`
3. Loop through each word:
   - If the word is already in the dictionary, increment its value
   - Otherwise, add it with value 1
4. Print each key-value pair

## What This Exercise Reinforced

- Dictionaries are key-value structures ideal for counting problems.
- .split(' ') converts a string into tokens (words).
- Conditional insertion pattern:
   - if key exists → update
   - else → initialize
- Iteration over .items() allows structured output.

## Common Pitfalls

- Forgetting that dictionaries are case-sensitive.
- Using incorrect splitting method (e.g. not accounting for multiple spaces).
- Confusing keys vs values when updating counts.
- Printing dictionary directly instead of iterating when formatted output is needed.

## Complexity

- Time complexity: O(n), where n is number of words.
- Space complexity: O(k), where k is number of unique words.

## Takeaway

Dictionaries are the standard tool for frequency counting problems. This pattern appears frequently in text processing, bioinformatics (k-mers), and data aggregation tasks.
