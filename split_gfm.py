import os
import sys


# Coordinate file for matrix
input_file = sys.argv[1]

# Root name for split files
keyword = sys.argv[2]

# Type of SV in this coordinate file (DEL, DUP, or INV)
sv_type = sys.argv[3]

# Template gfm job, with TYPE_SV, INPUT_FILE, and OUTPUT_FILE in the appropriate locations
batch_template = sys.argv[4]

# Splitting the input file
cmd1 = 'split -l 100 ' + input_file + ' ' + keyword
os.system(cmd1)

# List of files in current directory
xfiles = os.listdir('.')

for filename in xfiles:
	if keyword  not in filename:	
		continue
	
	# Read in the file
	with open(batch_template, 'r') as file :
		filedata = file.read()
	print filename
	# Replace the target string
	filedata = filedata.replace('TYPE_SV', sv_type)
	filedata = filedata.replace('INPUT_FILE', filename)
	filedata = filedata.replace('OUTPUT_FILE', filename + "_feature_matrix.tsv")
	# Write the file out again
	with open(filename+'_job.sh', 'w') as file:
		file.write(filedata)
# Making the job list for dead simple queue
listname = keyword + '_JOB_LIST'
with open(listname, 'w') as joblist:
	xfiles = os.listdir('.')	
	for filename in xfiles:
		if keyword in filename and 'job.sh' in filename:	
			joblist.write('sh ' + filename + '\n')		

# Running dSQ and dispatching the job queue

cmd2 = 'dSQ.py --jobfile ' + listname + ' > ' + keyword + '_run.sh'
cmd3 = 'sbatch ' + keyword + '_run.sh'
os.system(cmd2)
os.system(cmd3)
