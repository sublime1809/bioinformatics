#! /etc/bin/python

import sys

def find_clumps(genome, k, L, f):
    locations = dict()
    for i in range(0, len(genome) - k + 1):
        kmer = genome[i:i+k]
        if not locations.get(kmer):
            locations[kmer] = []
        locations[kmer].append(i)
    clumps = list()
    for i, index in enumerate(locations):
        print 'index, value'
        print index
        value = locations[index]
        print value
        print value[len(value) - 1] - value[0]
        print L
        print f
        if len(value) > f:
            clumps.append(index)
    print 'clumps'
    print clumps

def parse_file(filename):
    with open(filename) as fh:
        genome = fh.next()
        k, L, f = [int(s) for s in fh.next().split(" ")]
    return genome, k, L, f

if __name__ == '__main__':
    filename = sys.argv[1]
    genome, k, L, f = parse_file(filename)
    find_clumps(genome, k, L, f)
