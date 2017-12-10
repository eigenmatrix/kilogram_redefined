import random
from timeit import timeit
from math import sqrt
def qsort1(data):
	if data == []:
		return []
	last = data[-1]
	big, small = [], []
	for i in data[:-1]:
		if i >= last:
			big += [i]
		else:
			small += [i]
	return qsort1(small) + [last] + qsort1(big)

def main(data):
	qsort1(data)

if __name__ == '__main__':
	#data = [i for i in range(100)]
	print(timeit("__main__.qsort1([random.randrange(0,10000) for i in range(2000)])", setup="import __main__; import random", number=100))

