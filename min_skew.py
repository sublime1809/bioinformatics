import sys

def ParseInput(path):
    with open(path) as fh:
        sequence = fh.next().strip()
    return sequence

def find_skew(sequence):
    counts = dict()
    lowest_skew = 0
    current_skew = 0
    skews = list()
    skews.append(0)
    positions = list()
    for i, nuc in enumerate(sequence):
        if nuc.lower() == 'c':
            current_skew -= 1
        elif nuc.lower() == 'g':
            current_skew += 1
        
        if current_skew < lowest_skew:
            lowest_skew = current_skew
            positions = list()
            positions.append(i+1)     
        elif current_skew == lowest_skew:
            positions.append(i+1)
    for i in positions:
        sys.stdout.write(`i` + " ")
    print ""

print "Assignment 1A: Word Counting"

inputFilePath = sys.argv[1]
sequence = ParseInput(inputFilePath)
find_skew(sequence)
