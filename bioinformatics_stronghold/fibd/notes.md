# Mortal Fibonacci Rabbits

## Problem Summary

Given `n` months and a rabbit lifespan of `m` months, calculate the total number of rabbit pairs after `n` months.

The rabbits reproduce when they are older than 0 months and die after reaching their maximum lifespan.

## Approach

I represented the rabbit population as a list.

Each position in the list represents the age of a rabbit pair:

```text
index 0 → newborn rabbits
index 1 → 1-month-old rabbits
index 2 → 2-month-old rabbits
...
```

The list has `m` positions because rabbits live for `m` months.

For example, with `m = 3`:

```text
[1, 0, 0]

index 0 → newborn
index 1 → 1 month old
index 2 → 2 months old
```

The initial population is one newborn pair.

For each month:

1. Make a copy of the current population.
2. Create a new list filled with zeros.
3. Calculate the newborn rabbits by summing all rabbits older than 0 months.
4. Move each existing age group one position forward.
5. Rabbits that were at the maximum age are not copied into the new population, so they die.
6. Repeat until reaching month `n`.
7. Sum the final population to get the total number of rabbit pairs.

## Important Parts of the Code

### Copying the population

```python
previous_population = current_population.copy()
```

A copy is necessary because the previous population is used to calculate the next population.

If I used:

```python
previous_population = current_population
```

both variables would refer to the same list.

### Calculating newborn rabbits

```python
current_population[0] = sum(previous_population[1:])
```

`previous_population[1:]` contains every age group except newborns.

Therefore, all rabbits older than 0 months are counted as reproducing rabbits.

### Aging the rabbits

```python
for age in range(1, m):
    current_population[age] = previous_population[age - 1]
```

Each age group moves forward by one position.

For example:

```text
previous: [2, 1, 1]
next:     [2, 2, 1]
```

The first `2` in the next population represents the newborn rabbits produced by the older rabbits.

### Rabbit mortality

There is no position beyond `m - 1`.

Therefore, rabbits at the maximum age are not copied into the next population and disappear from the simulation.

## File Handling

The input is read from `rosalind_fibd.txt`:

```python
with open("rosalind_fibd.txt", "r") as file:
    n, m = map(int, file.read().split())
```

The final answer is written to `rosalind_fibd_output.txt`.

Using `with open()` automatically closes the files after use.

## Example

For:

```text
n = 6
m = 3
```

the population changes as follows:

```text
Month 1: [1, 0, 0]
Month 2: [0, 1, 0]
Month 3: [1, 0, 1]
Month 4: [1, 1, 0]
Month 5: [1, 1, 1]
Month 6: [2, 1, 1]
```

The final population is:

```text
2 + 1 + 1 = 4
```

Therefore, the answer is:

```text
4
```

## What This Exercise Reinforced

* Representing biological populations using lists.
* Using list indexes to represent age.
* Simulating a population over discrete time steps.
* Copying lists to preserve the previous state.
* Using slicing and `sum()` to calculate reproduction.
* Using loops to update population state.
* Modeling mortality by limiting the number of age groups.
* Reading input and writing output using files.

## Complexity

Let `n` be the number of months and `m` the rabbit lifespan.

Each month processes the `m` age groups.

* Time complexity: `O(n × m)`
* Space complexity: `O(m)`

## Takeaway

This problem extends the basic Fibonacci rabbit problem by adding mortality.

Instead of storing only the total number of rabbits, the solution stores rabbits by age. This makes it possible to model both reproduction and death over time.

