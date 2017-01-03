import math

def exponent(base, power):
	count = 1
	summ = 1
	max_power = power

	while max_power > 0:
		product = base
		count = 1	
		while count < max_power:
			last = product
			product = product * product
			count = count * 2

		if count > max_power:
			product = product / last
			max_power = max_power - math.ceil(count/2.0)
		else:
			max_power = max_power - count
		summ = summ * product
	return summ
	
for i in range(20):
	print exponent(3,i)