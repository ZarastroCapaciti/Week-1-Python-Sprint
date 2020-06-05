def translateDNA(dna):

    dna1 = dna[0:3]
    dna2 = dna[3:6]
    dna3 = dna[-3:]

    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'', 'TAG':'',
        'TGC':'C', 'TGT':'C', 'TGA':'', 'TGG':'W',
    }

    protein =""
    if len(dna1)%3 == 0:
        for i in range(0, len(dna1), 3):
            codon = dna1[i:i + 3]
            protein += table[codon]

    if len(dna2)%3 == 0:
        for i in range(0, len(dna2), 3):
            codon = dna2[i:i + 3]
            protein += table[codon]

    if len(dna3)%3 == 0:
        for i in range(0, len(dna3), 3):
            codon = dna3[i:i + 3]
            protein += table[codon]

    return protein

def mutate():
    file1 = open("DNAFile.txt", "r+")

    normalDNA = file1.read()
    normalDNA = normalDNA.replace("\n", "")

    normalDNA = normalDNA.replace("a", "A")

    file1.close()

    file2 = open("normalDNA.txt", "w")

    file2.write(normalDNA)

    file2.close()

    file1 = open("DNAFile.txt", "r+")

    normalDNA = file1.read()
    normalDNA = normalDNA.replace("\n", "")

    normalDNA = normalDNA.replace("a", "T")

    file1.close()

    file3 = open("mutatedDNA.txt", "w")

    file3.write(normalDNA)

    file3.close()

def txtTranslate():
    file2 = open("normalDNA.txt", "r")
    file3 = open("mutatedDNA.txt", "r")

    return file2.read() + "\n" + file3.read()

mutate()
print(txtTranslate())
print(translateDNA("ATACCCGTA"))