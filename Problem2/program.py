import sys

def get_complement(dna):
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complement = ""
    for i in dna:
        complement += complements[i]
    return complement[::-1]


def read_dna(filename):
    with open(filename) as fh:
        dna = fh.next().strip()
    return dna


filename = sys.argv[1]
dna = read_dna(filename)
print get_complement(dna)
