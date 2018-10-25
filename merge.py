import sys
f1 = sys.argv[1]
f2 = sys.argv[2]
f3 = sys.argv[3]
with open(f1) as in1:
	with open(f2) as in2:
		with open(f3, 'w') as out:
			d = {}
			for line in f1:
				lin = line.split('\t')
				key = str(lin[:3])
				d[key] = line
			for line in f2:
				lin = line.split('\t')
				key = str(lin[:3])	
