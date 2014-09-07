import sys

def ParseInput(path):
    with open(path) as fh:
        pattern = fh.next().strip()
        seq = fh.next().strip()
    return pattern, seq

def FindPattern(sequence, pattern):
    positions = list()
    k = len(pattern)
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        if pattern == kmer:
            positions.append(i)
    for i in positions:
        sys.stdout.write(i.__str__() + " ")
    print ""

print "Assignment 1A: Word Counting"

inputFilePath = sys.argv[1]
pattern, sequence = ParseInput(inputFilePath)
FindPattern(sequence, pattern)
