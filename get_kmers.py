#!/usr/bin/env python3
# get_kmers.py

# set kmer length
kmer_length = 7
# set the stop
stop = len(seq) - kmer_length + 1
for start in range(0, stop):
    kmer = seq[start:start + kmer_length]
    print(kmer)
