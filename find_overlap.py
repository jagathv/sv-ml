import csv
import subprocess


''' Generate the overlap metric for an interval'''
def shell_overlap(chrom, bin_start, bin_end, overlap_tsv, output_name): 
	# Write the interval coordinates to a temporary file
	with open(output_name, 'w') as output:
		output.write(chrom + '\t' + str(bin_start) + '\t' + str(bin_end))
	# Call Bedtools intersect on the SV coordinates with the overlap file
	s = 'bedtools intersect -a ' + output_name + ' -b ' + overlap_tsv
	cmd = subprocess.Popen(s, shell=True, stdout=subprocess.PIPE)
	# The area of the SV that overlaps
	overlaps = 0

	# The number of overlapped intervals
	overlapped_intervals = 0
	for line in cmd.stdout:
		start = int(line.split('\t')[1])
		end = int(line.split('\t')[2])
		overlaps += end - start
		overlapped_intervals += 1

		# If this is a partial overlap (not entirely fool-proof, 
		# but very unlikely to incorrectly classify as partial)
		if start == bin_start or end == bin_end:
			overlapped_intervals += 1
	try:
		avg = float(overlaps) / float(bin_end - bin_start)
		return avg 
	except ZeroDivisionError:
		return 0	

def get_bin_overlap(bin_start, bin_end, int_list):
	length = bin_end - bin_start
	if length == 0:
		return 0
	ret = 0
	for interval in int_list:
		int_start = interval[0]
		int_end = interval[1]
		if bin_start <= int_end and bin_end >= int_start:
			if bin_start < int_start:
				if bin_end <= int_end:
					ret += float(bin_end - int_start) / float(length)
				else:
					ret += float(bin_end - bin_start) / float(length)
			else:
				if bin_end > int_end:
					ret += float(int_end - bin_start) / float(length)
				else:
					return 1.0
		return ret

def file_to_dict(coord_file):
	d = {}
	with open(coord_file, 'r') as coords:
		for line in coords:
			data = line.split(' ')
			chrom = data[0]
			start = int(data[1])
			end = int(data[2])
			if chrom in d:
				d[chrom].append((start, end))
			else:
				d[chrom] = [(start, end)]
	return d

def overlap(chrom, interval, overlap_file, metric):
	if metric != 'mean' and metric != 'max':
		raise ValueError("Metric must be mean or max")
#	bins = []
#	for i in range(interval[0], interval[1]+1, 10):
#		bins.append((i, min(interval[1], i + 9)))
#	if len(bins) == 0:
#		if interval[1] - interval[0] > 0:
#			bins.append(interval)
#		else:
#			return 0
#	bin_metrics = [shell_overlap(chrom, nums[0], nums[1], overlap_file, 'temp.txt') for nums in bins]
#	if metric == 'max':
#		return max(bin_metrics)
#	else:
#		try:
#			return float(sum(bin_metrics)) / float(len(bin_metrics))
#		except ZeroDivisionError:
#			return 0
	

if __name__ == '__main__':
	out_data = [['COSMIC_overlap.mean', 'COSMIC_overlap.max']]
	d = 'cosmic_coords.txt'
	with open('1kg_short_coords.txt', 'r') as inputs:
		for line in inputs:
			line = line.split('\t')
			chrom = line[0]
			if chrom == 'Y':
				continue
			start = int(line[1])
			end = int(line[2])
			out_data.append([overlap(chrom, (start, end), d, 'mean'), overlap(chrom, (start, end), d, 'max')])
	with open('dummy_COSMIC_output.txt', 'w') as tsvfile:
			writer = csv.writer(tsvfile, delimiter='\t')
			for row in out_data:
				writer.writerow(row)	
