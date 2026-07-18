# Translating RNA into Protein

dataset_file = open('rosalind_prot.txt', 'r')
output_file = open('rosalind_prot_output.txt', 'w')

RNA_codon_table = {
    "UUU" : "F",
    "UUC" : "F",
    "UUA" : "L",
    "UUG" : "L",
    "UCU" : "S",
    "UCC" : "S",
    "UCA" : "S",
    "UCG" : "S",
    "UAU" : "Y",
    "UAC" : "Y",
    "UAA" : "Stop",
    "UAG" : "Stop",
    "UGU" : "C",
    "UGC" : "C",
    "UGA" : "Stop",
    "UGG" : "W",
    "CUU" : "L",
    "CUC" : "L",
    "CUA" : "L",
    "CUG" : "L",
    "CCU" : "P",
    "CCC" : "P",
    "CCA" : "P",
    "CCG" : "P",
    "CAU" : "H",
    "CAC" : "H",
    "CAA" : "Q",
    "CAG" : "Q",
    "CGU" : "R",
    "CGC" : "R",
    "CGA" : "R",
    "CGG" : "R",
    "AUU" : "I",
    "AUC" : "I",
    "AUA" : "I",
    "AUG" : "M",
    "ACU" : "T",
    "ACC" : "T",
    "ACA" : "T",
    "ACG" : "T",
    "AAU" : "N",
    "AAC" : "N",
    "AAA" : "K",
    "AAG" : "K",
    "AGU" : "S",
    "AGC" : "S",
    "AGA" : "R",
    "AGG" : "R",
    "GUU" : "V",
    "GUC" : "V",
    "GUA" : "V",
    "GUG" : "V",
    "GCU" : "A",
    "GCC" : "A",
    "GCA" : "A",
    "GCG" : "A",
    "GAU" : "D",
    "GAC" : "D",
    "GAA" : "E",
    "GAG" : "E",
    "GGU" : "G",
    "GGC" : "G",
    "GGA" : "G",
    "GGG" : "G",

}
rna_string = dataset_file.read().strip()
protein_string = ""

current_codon = ""
for rna_base in rna_string:
    if len(current_codon) < 3:
        current_codon += rna_base
        if len(current_codon) == 3:
            if RNA_codon_table[current_codon] == "Stop":
                break
            else:
                protein_string += RNA_codon_table[current_codon]
                current_codon = ""

output_file.write(protein_string)
dataset_file.close()
output_file.close()