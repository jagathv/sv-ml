from __future__ import print_function
import vcf
import sys
import matplotlib.pyplot as plt
from Bio import SeqIO
import allel



''' Get GC content of a sequence '''
def gc_content(seq):
    gc = 0
    for let in seq:
        if let == 'G' or let == 'C':
            gc += 1
    return float(gc) / float(len(seq))

def dict_from_ref(reference):
    return SeqIO.to_dict(SeqIO.parse(reference, 'fasta'))

''' Initialize the VCF reader for a file '''
def get_reader(file):
    reader = allel.read_vcf(file, fields='*')
    return reader


''' Create SIM instructions to emulate creation of an SV similar to given SV,
    given the ALT and CS fields of an SV'''
def sv_to_instruction(reader, i):
    s = ''
    alt = str(reader['variants/ALT'][i][0])
    cs = str(reader['variants/CS'][i])
    instr_dict = {
        'INS': 'INR ',
        'DUP': 'DUP ',
        'ALU': 'INR ',
        'DEL': 'DEL ',
        'INV': 'INV '
    }
    found = False
    for key in instr_dict.keys():
        if key in alt or key in cs:
            found = True
            s += instr_dict[key]
            break
    if not found:
        raise ValueError("VCF does not contain a type in the\
                                            following strings: ", alt, ' ', cs)
    length = get_length(reader, i)
    s += str(length)
    return s


''' Get the length of an SV '''
def get_length(reader, i):
    pos = reader['variants/POS'][i]
    end = reader['variants/END'][i]
    length = reader['variants/SVLEN'][i]
    if length < 0:
        length = end - pos
    return length


''' Create a SIM file for SV's similar to given SV's '''
def create_sim(input_file, output_file):
    reader = get_reader(input_file)
    output = open(output_file, 'w')
    for i in range(len(reader['variants/POS'])):
        output.write(sv_to_instruction(reader, i) + '\n')
    output.close()


''' Create a histogram for GC or SV length data '''
def create_hist(input_file, output_file, reference, type):
    ref_dict = dict_from_ref(reference)
    reader = get_reader(input_file)
    if type not in ['GC', 'Length', 'gc', 'length']:
        raise ValueError("Type must be 'gc' or 'length'")
    data = []
    length = 0
    for i in range(len(reader['variants/SVLEN'])):
        pos = reader['variants/POS'][i]
        chrom = reader['variants/CHROM'][i]
        length = get_length(reader, i)
        if type == 'length' or type == 'Length':
            data.append(length)
        else:
            seq = ref_dict[chrom][pos:pos+length]
            data.append(gc_content(seq))
    plt.hist(data, bins='auto')
    plt.title(type +  ' Content Histogram')
    plt.savefig(output_file)
