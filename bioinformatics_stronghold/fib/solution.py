# Rabbits and Recurrence Relations

n = 5  # number of months
k = 3  # offspring pairs produced per reproduction-age pair

previous_gen = 0
current_gen = 1

while n > 1:
    next_gen = current_gen + previous_gen * k

    previous_gen = current_gen
    current_gen = next_gen

    n -= 1

print(current_gen)
