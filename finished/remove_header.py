import sys
import os
input_file = sys.argv[1]
temp = input_file + 'temp_output'
with open(input_file, 'r') as inp:
	with open(temp, 'w') as out:
		i = 0
		for line in inp:
			if i == 0:
				out.write(line)
				i += 1
				continue
			if line[0] != 'L':
				out.write(line)
cmd = 'mv ' + temp + ' ' + input_file
os.system(cmd)
