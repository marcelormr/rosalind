dataset_file = open('rosalind_gc.txt', 'r')
output_file = open('rosalind_gc_output.txt', 'w')

dna_strings = {}
gc_contents = {}

current_id = ""

highest_gc_content = 0.0
highest_gc_id = ""

# Parse FASTA file
for line in dataset_file:

    line = line.strip()

    if line[0] == '>':
        current_id = line[1:]
        dna_strings[current_id] = ""

    else:
        dna_strings[current_id] += line


# Calculate GC content for each sequence
for sequence_id in dna_strings:

    gc_count = 0
    sequence = dna_strings[sequence_id]

    for base in sequence:

        if base == 'G' or base == 'C':
            gc_count += 1

    gc_content = (gc_count / len(sequence)) * 100
    gc_contents[sequence_id] = gc_content

# Find highest GC content
for sequence_id in gc_contents:

    if gc_contents[sequence_id] > highest_gc_content:

        highest_gc_content = gc_contents[sequence_id]
        highest_gc_id = sequence_id

# Write output
output_file.write(highest_gc_id + '\n')
output_file.write(str(highest_gc_content))


dataset_file.close()
output_file.close()