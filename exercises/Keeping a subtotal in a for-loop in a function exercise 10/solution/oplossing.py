def DnaFrequentie(dna_streng):
    A = 0
    C = 0
    G = 0
    T = 0

    for nucleotide in dna_streng:
        if nucleotide == "A":
            A = A + 1
        elif nucleotide == "C":
            C = C + 1
        elif nucleotide == "G":
            G = G + 1
        elif nucleotide == "T":
            T = T + 1
    
    return [A, C, G, T]