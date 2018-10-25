import os
import sys


# Coordinate file for matrix
input_file = sys.argv[1]
model_file = sys.argv[2]
# Read in the file
with open('load_model.sh', 'r') as file :
	filedata = file.read()
filedata = filedata.replace('IFILE', input_file)
filedata = filedata.replace('MODELF', model_file)
filedata = filedata.replace('OUTPUT', input_file + 'all_scored.txt')
# Write the file out again
with open(input_file+'_load.sh', 'w') as file:
	file.write(filedata)
# Making the job list for dead simple queue
