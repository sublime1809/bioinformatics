import sys

def ParseInput(path):
    with open(path) as fh:
        sequence = fh.next().strip()
        k = int(fh.next().strip())
    return sequence, k

def CountWords(sequence, k):
    counts = dict()
    highestCount = 0
    highestWords = list()
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        counts[kmer] = counts[kmer] + 1 if counts.get(kmer) is not None else 1
        if counts[kmer] > highestCount:
            highestCount = counts[kmer]
            highestWords = [kmer]
        elif counts[kmer] == highestCount:
            highestWords.append(kmer)        
    for i in highestWords:
        sys.stdout.write(i + " ")
    print ""

print "Assignment 1A: Word Counting"

inputFilePath = sys.argv[1]
sequence, k = ParseInput(inputFilePath)
CountWords(sequence, k)
