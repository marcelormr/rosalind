# Mendel's First Law

## Problem

Given a population containing:

- `k` homozygous dominant organisms (`AA`)
- `m` heterozygous organisms (`Aa`)
- `n` homozygous recessive organisms (`aa`)

Calculate the probability that two randomly selected organisms will produce an offspring with a dominant phenotype.

Organisms are selected without replacement.

---

## Approach

Each possible mating combination has a different probability depending on the number of organisms of each genotype in the population.

The probability of selecting a genotype pair is calculated as:

$$
P(A \times B) = \frac{\text{first genotype count}}{\text{total population}} \times \frac{\text{second genotype count}}{\text{total population} - 1}
$$

The probability of a dominant phenotype from each cross is then multiplied by the probability of that cross occurring.

---

## Genotype Crosses

| Parents | Dominant phenotype probability |
|---------|-------------------------------|
| AA × AA | 1 |
| AA × Aa | 1 |
| AA × aa | 1 |
| Aa × Aa | 3/4 |
| Aa × aa | 1/2 |
| aa × aa | 0 |

The final probability is the sum of all possible crosses.

---

## Key Concepts

- Probability of sequential events.
- Sampling without replacement.
- Punnett squares and Mendelian inheritance.
- Combining probabilities using multiplication and addition rules.

---

## Complexity

Time complexity: O(1)

The solution performs a fixed number of probability calculations regardless of population size.

Space complexity: O(1)

Only a few variables are stored.
