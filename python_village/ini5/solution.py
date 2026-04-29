input_file = open('rosalind_ini5_input.txt', 'r')
output_file = open('rosalind_ini5_output.txt', 'w')

line_counter = 0

for line in input_file:
    if line_counter % 2 == 1:
        output_file.write(line)
    line_counter += 1
input_file.close()
output_file.close()