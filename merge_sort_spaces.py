import random 
blank = -99
m = 5
n = 2
trials = 10

for i in xrange(trials):
	a = list(xrange(m + n))
	b = list(xrange(n))

	count = n
	while count:
		num = random.randint(0,m+n - 1)
		if a[num] != blank:
			a[num] = blank
			count -= 1
	a_clone = a[:]
	b_clone = b[:]
	s = a[:] + b[:]
	s.sort()
	s = s[n:]

	placement = 0
	pos_a = 0
	pos_b = 0
	pos_b_a_r = 0
	pos_b_a_w = 0
	a_buf_count = 0
	while placement < len(a):
		while pos_a < len(a) and a[pos_a] == blank:
			pos_a += 1
		if (pos_b >= len(b) and pos_b_a_r >= len(b)) or pos_b_a_w == pos_b_a_r:
			#just compare a with b value
			if pos_a < len(a) and (pos_b >= len(b) or a[pos_a] <= b[pos_b]):
				a[placement] = a[pos_a]
				pos_a += 1	
			else:
				temp = b[pos_b]
				if pos_b_a_w < len(b) and a[placement] != blank:
					b[pos_b_a_w] = a[placement]
					pos_b_a_w += 1
					pos_a += 1
				a[placement] = temp
				pos_b += 1
		else:
			#comparing the first part of b with later part of b
			if pos_b >= len(b) or b[pos_b_a_r] <= b[pos_b]:
				val = b[pos_b_a_r]
				pos_b_a_r += 1
			else:
				val = b[pos_b]
				pos_b += 1
			if pos_b_a_w < len(b) and a[placement] != blank:
				b[pos_b_a_w] = a[placement]
				pos_b_a_w += 1
				pos_a += 1
			a[placement] = val
		placement += 1

	if s != a:
		print("failed")
		print a_clone
		print b_clone
		print a
		print s



