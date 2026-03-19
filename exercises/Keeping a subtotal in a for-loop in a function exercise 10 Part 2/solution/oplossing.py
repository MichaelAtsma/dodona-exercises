def DnaComplement(dna_streng):
    dna_complement = ""

    for nucleotide in dna_streng:
        if nucleotide == "A":
            dna_complement = dna_complement + "T"
        elif nucleotide == "C":
            dna_complement = dna_complement + "G"
        elif nucleotide == "G":
            dna_complement = dna_complement + "C"
        elif nucleotide == "T":
            dna_complement = dna_complement + "A"
    
    return dna_complement