# Finding a Motif in DNA

dataset_file = open('rosalind_subs.txt', 'r')
output_file = open('rosalind_subs_output.txt', 'w')

s = dataset_file.readline().strip()
t = dataset_file.readline().strip()

i = 0
j = len(t)

positions = []

# Iterate through whole string, count everytime it appears, and store the position into 1-based numbering
for symbols in s:
    if s[i:j] == t:
        positions.append(i+1) # convert into 1-based numbering
    i += 1
    j += 1

# Write the output into file
for position in positions:
    output_file.write(str(position) + " ")

dataset_file.close()
output_file.close()