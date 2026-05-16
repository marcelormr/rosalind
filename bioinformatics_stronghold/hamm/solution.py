# Counting Point Mutations

dataset_file = open('rosalind_hamm.txt', 'r')
output_file = open('rosalind_hamm_output.txt', 'w')

s = dataset_file.readline()
t = dataset_file.readline()

string_size = len(s)-1
position = 0
hamming_distance = 0

while position < string_size:
    if s[position] != t[position]:
        hamming_distance += 1
    position += 1

output_file.write(str(hamming_distance))

dataset_file.close()
output_file.close()