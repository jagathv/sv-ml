import sys
from random import choice, shuffle, sample

class Sequence():

	def __init__(self, index_file):
		self.chroms = chroms_from_index(index_file)

	def distribute_sv(self, length_file):
		lengths = list_from_lengths(length_file)
		for length in lengths:
			self.chroms[choice(self.chroms.keys())].add_sv(length)
		
	def create_svs(self):
		for chrom in self.chroms:
			self.chroms[chrom].create_svs()

	def write_svs(self, output_file):
		with open(output_file, 'w') as out:
			out.write("Chromosome\tStart\tEnd\n")
			for chrom in self.chroms:
				for coord in self.chroms[chrom].get_coords():
					out.write(coord)

class Chromosome():

	def __init__(self, name, length):
		self.name = name
		self.length = length
		self.sv = []
		self.sv_sum = 0
		self.sv_coords = []
		self.created_svs = False
		self.added_svs = False

	def add_sv(self, sv_size):
		self.added_svs = True
		self.sv.append(sv_size)
		self.sv_sum += sv_size
		if self.sv_sum > self.length:
			raise ValueError("Too many SV's for chromosome " + str(self.name))
	
	def create_svs(self):
		if not self.added_svs:
			self.created_svs = True
			return
		self.created_svs = True
		truncated_size = self.length - self.sv_sum
		possible_locations = range(truncated_size)
		sv_loc = sample(possible_locations, len(self.sv))
		sv_loc.sort()
		shuffle(self.sv)
		prefix_sum = []
		prefix = 0
		for i in range(len(self.sv)):
			prefix_sum.append(prefix)
			prefix += self.sv[i]
		for i in range(len(self.sv)):
			self.sv_coords.append([self.name, sv_loc[i] + prefix_sum[i], sv_loc[i] + prefix_sum[i] + self.sv[i]])  
	
	def get_coords(self):
		if not self.created_svs:
			raise ValueError("Error: SV's not yet created in chromosome " + self.name)
		str_coords = []
		for coord in self.sv_coords:
			s = 'chr' + coord[0]
			s += '\t' + str(coord[1]) + '\t' + str(coord[2]) + '\n'
			str_coords.append(s)
		return str_coords
		


def chroms_from_index(index_file):
	ret_dict = {}
	with open(index_file) as index:
		for line in index:
			line_data  = line.split('\t')
			chrom = line_data[0]
			length = int(line_data[1])
			ret_dict[chrom] = Chromosome(chrom, length)
	return ret_dict

def list_from_lengths(length_file):
	with open(length_file) as lengths:
		return [int(line) for line in lengths]

if __name__ == '__main__':
	length_file = sys.argv[1]
	index_file = sys.argv[2]
	output_file = sys.argv[3]
	num_svs = sum(1 for line in open(length_file))
	genome = Sequence(index_file)
	print("Queueing SV's to be created in each chromosome...")
	genome.distribute_sv(length_file)
	print("Creating SV's in each chromosome...")
	genome.create_svs()
	print("Outputting " + str(num_svs) + " SV's to " + output_file)
	genome.write_svs(output_file)	
