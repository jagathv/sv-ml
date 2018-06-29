from __future__ import print_function
import vcf
import sys
import matplotlib.pyplot as plt
import allel
from Bio import SeqIO
import numpy as np

''' Get GC content of a sequence '''
def gc_content(seq):
    gc = 0
    for let in seq:
        if let == 'G' or let == 'C':
            gc += 1
        # elif let == 'N':
            # gc += 0.25
    return float(gc) / float(len(seq))

def allel_get_reader(file):
    callset = allel.read_vcf(file, fields='*')
    return callset

''' Initialize the VCF reader for a file '''
def get_reader(file):
    f = open(file, 'r')
    reader = vcf.Reader(f)
    return reader

''' Print GC content of each SV '''
if __name__ == '__main__':
    sv_file = sys.argv[1]
    reader = allel_get_reader(sv_file)
    for i in range(40):
        id = reader['variants/ALT'][i]
        print(id, ' ', reader['variants/CS'][i])
        if 'CN' in str(id):
            print("THIS HAD CN")
