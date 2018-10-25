with open('common_fragile_sites.txt', 'r') as inp:
	with open('new_fragile', 'w') as out:
		for line in inp:
			lst = line.split()	
			out.write(lst[0] + '\t' + lst[1] + '\t' + lst[2] + '\n')
 
