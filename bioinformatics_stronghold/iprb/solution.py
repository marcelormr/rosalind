# Mendel's First Law

dataset_file = open('rosalind_iprb.txt', 'r')
output_file = open('rosalind_iprb_output.txt', 'w')

k, m, n = map(int, dataset_file.readline().split())
total = k + m + n
# Homozygous dominant x Homozygous dominant (2/6 * 1/5 = 2/30) chance
#   A  A
# A AA AA
# A AA AA
# Chance of dominant phenotype is 4/4 * 2/30 = 8/120

# Homozygous dominant x Heterozygous (2/6 * 2/5 + 2/6 * 2/5 = 4/30 + 4/30 = 8/30) chance
#   A  a
# A AA Aa
# A AA Aa
# Chance of dominant phenotype is 4/4 * 8/30 = 32/120

# Homozygous dominant x Homozygous recessive (2/6 * 2/5 + 2/6 * 2/5 = 4/30 + 4/30 = 8/30) chance
#   a  a
# A Aa Aa
# A Aa Aa
# Chance of dominant phenotype is 4/4 * 8/30 = 32/120

# Heterozygous x Heterozygous (2/6 * 1/5 = 2/30) chance
#   A  a
# A AA Aa
# a Aa aa
# Chance of dominant phenotype is 3/4 * 2/30 = 6/120

# Heterozygous x Homozygous recessive (2/6 * 2/5 + 2/6 * 2/5 = 4/30 + 4/30 = 8/30) chance
#   a  a
# A Aa Aa
# a aa aa
# Chance of dominant phenotype is 2/4 * 8/30 = 16/120

# Homozygous recessive x Homozygous recessive (2/6 * 1/5 = 2/30) chance
#   a  a
# a aa aa
# a aa aa
# Chance of dominant phenotype is 0/4 * 2/30 = 0/120

# Total chance of dominant phenotype is 8 + 32 + 32 + 6 + 16 + 0 = 94/120 -> 0,78333...



p = (
    (k / total) * ((k - 1) / (total - 1)) * 1 +     # Homozygous dominant x Homozygous dominant
    (k / total) * (m / (total - 1)) * 1 +           # Homozygous dominant x Heterozygous
    (k / total) * (n / (total - 1)) * 1 +           # Homozygous dominant x Homozygous recessive
    (m / total) * (k / (total - 1)) * 1 +           # Heterozygous x Homozygous dominant
    (m / total) * ((m - 1) / (total - 1)) * 0.75 +  # Heterozygous x Heterozygous
    (m / total) * (n / (total - 1)) * 0.5 +         # Heterozygous x Homozygous recessive
    (n / total) * (k / (total - 1)) * 1 +           # Homozygous recessive x Homozygous dominant
    (n / total) * (m / (total - 1)) * 0.5 +         # Homozygous recessive x Heterozygous
    (n / total) * ((n - 1) / (total - 1)) * 0       # Homozygous recessive x Homozygous recessive
)

print(p)
# Write output
output_file.write(str(p))


dataset_file.close()
output_file.close()