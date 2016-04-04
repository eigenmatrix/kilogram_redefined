import random
size = 7
offset = 2
count = 50000

data_bot = [0]*size

for x in range(count):
	cards = list(xrange(size))
	for i in xrange(size):
		swap = random.randint(i,size-1)
		cards[i], cards[swap] = cards[swap], cards[i]
	data_bot[cards[size-offset]] += 1

data_prev = data_bot[:]
data_bot = [0]*size

for x in range(count):
	cards = list(xrange(size))
	for i in xrange(size):
		swap = random.randint(0,size-1)
		cards[i], cards[swap] = cards[swap], cards[i]
	data_bot[cards[size-offset]] += 1

print("Deviations from expected:")
for a in xrange(size):
	print(((float)(data_bot[a]) - (float)(count)/size)/count * 100)


