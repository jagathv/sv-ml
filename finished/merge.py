import sys
f1 = sys.argv[1]
f2 = sys.argv[2]
f3 = sys.argv[3]
with open(f1) as in1:
	with open(f2) as in2:
		with open(f3, 'w') as out:
			d = {}
			for line in in1:
				lin = line.split('\t')
				if len(lin) >= 5:
					lin[4] = lin[4].rstrip()
				key = str(lin[2:5])
				d[key] = line
				print key
			for line in in2:
				lin = line.split('\t')
				key = str([lin[0][3:]] + lin[1:3])	
				if key not in d:
					continue
				out.write(d[key].rstrip() + line)
