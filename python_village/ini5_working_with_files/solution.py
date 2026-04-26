inputFile = open('rosalind_ini5_input.txt', 'r')
inputFile = inputFile.readlines()
outputFile = open('rosalind_ini5_output.txt', 'w')

lineCounter = 0

for line in inputFile:
    if lineCounter %2 == 1:
        outputFile.write(str(line))
    lineCounter += 1