# Mortal Fibonacci Rabbits

# Read input
with open("rosalind_fibd.txt", "r") as file:
    n, m = map(int, file.read().split())

# Index = rabbit age
# Example with m = 3:
# rabbits[0] -> 0 month old rabbits
# rabbits[1] -> 1 month old rabbits
# rabbits[2] -> 2 month old rabbits

current_population = [0] * m

# Initial population: 1 newborn pair
current_population[0] = 1

while n > 1:  # Initial state is month 1
    previous_population = current_population.copy()

    # Create a new empty population
    current_population = [0] * m

    # Newborn rabbits are produced by all rabbits older than 0 months
    current_population[0] = sum(previous_population[1:])

    # Age rabbits by one month
    for age in range(1, m):
        current_population[age] = previous_population[age - 1]

    n -= 1

# Write output
with open("rosalind_fibd_output.txt", "w") as output_file:
    output_file.write(str(sum(current_population)))