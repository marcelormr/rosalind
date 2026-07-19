# Consensus and Profile

dna_strings = []
current_sequence = ""
# Parse FASTA file
with open("rosalind_cons.txt") as file:
    for line in file:
        line = line.strip()

        if line.startswith(">"):
            if current_sequence != "":
                dna_strings.append(current_sequence)
            current_sequence = ""
        else:
            current_sequence += line

# Don't forget the last sequence
dna_strings.append(current_sequence)

# Generate the matrix
profile_matrix = [] # Creates an empty matrix

for i in range(4): # Once for each nucleobase
    row = [] #Creates an empty list

    for j in range(len(dna_strings[0])): # Once for each DNA string
        row.append(0)

    profile_matrix.append(row)

# Build the profile matrix values
j = 0
for dna_string in dna_strings:
    for nucleobase in dna_string:
        match nucleobase:
            case 'A':
                profile_matrix[0][j] += 1
            case 'C':
                profile_matrix[1][j] += 1
            case 'G':
                profile_matrix[2][j] += 1
            case 'T':
                profile_matrix[3][j] += 1
        j += 1
    j = 0

# Generate the consensus string
with open('rosalind_cons_output.txt', 'w') as output_file:
    biggest_value = 0
    biggest_value_position = 0
    i = 0
    j = 0
    consensus_string = ''
    while j < len(profile_matrix[0]): # Look into every row
        while i < 4: # Look into every column
            if profile_matrix[i][j] > biggest_value:
                biggest_value = profile_matrix[i][j]
                biggest_value_position = i
            i += 1
        match biggest_value_position:
            case 0:
                consensus_string = consensus_string + 'A'
            case 1:
                consensus_string = consensus_string + 'C'
            case 2:
                consensus_string = consensus_string + 'G'
            case 3:
                consensus_string = consensus_string + 'T'
        i = 0
        biggest_value = 0
        j += 1
    output_file.write(consensus_string + '\n')

    line_count = 0

    for line in profile_matrix:
        match line_count:
            case 0:
                output_file.write('A: ')
            case 1:
                output_file.write('C: ')
            case 2:
                output_file.write('G: ')
            case 3:
                output_file.write('T: ')
        for value in line:
            output_file.write(str(value) + " ")

        output_file.write('\n')
        line_count += 1