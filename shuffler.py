import random
size = 5
size = size * 2
count = 1000
data_end = [0]*size
data_bot = [0]*size
cards = list(xrange(size))

for x in range(count):
	for i in xrange(size):
		swap = random.randint(i,size-1)
		cards[i], cards[swap] = cards[swap], cards[i]
	data_end[cards[size-1]] += 1
	data_bot[cards[0]] += 1

print(data_bot)
print(data_end)

data_end = [0]*size
data_bot = [0]*size
cards = list(xrange(size))
for x in range(count):
	for i in xrange(size):
		swap = random.randint(0,size-1)
		cards[i], cards[swap] = cards[swap], cards[i]
	data_end[cards[size-1]] += 1
	data_bot[cards[0]] += 1
print("")
print(data_bot)
print(data_end)

print("In conclusion, insufficient data for a meaningful answer.")


