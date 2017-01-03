sample = [4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, None, 1, 2]
seq = []
start = 1
for i in range(1, len(sample)):
	#find a candidate pattern length
	if sample[0] == sample[i] or sample[i] == None or sample[0] == None:
		seq = sample[:i]
		if i == 1 and sample[0] == None:
			seq = sample[1:2]
		found = True
		for x in range(i, len(sample), i):	
			test_range = sample[x:x+i]
			print test_range
			for y in range(len(test_range)):
				print seq
				if test_range[y] == None or seq[y] == None:
					continue
				if test_range[y] == seq[y]:
					continue
				if test_range[y] != seq[y]:
					found = False
					break
		if found: 
			print "we found the pattern"
			print seq
			exit()
print "No pattern!"

