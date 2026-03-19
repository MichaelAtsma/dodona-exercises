import random
import time

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

n = 1000000
start = time.time()
letters = random.choices("ACGT", k=n)
end = time.time()
print(f"Generated {n} random letters in {end - start:.2f} seconds.")

start = time.time()
result = DnaFrequentie("".join(letters))
end = time.time()
print(f"Processed a strand of {n} nucleotides in {end - start:.2f} seconds. Result: {result}.")