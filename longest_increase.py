data = [10, 9, 2, 5, 3, 7, 101, 18]
data = [9, 5, 2, 8, 7, 3, 1, 6, 4, 5]
data = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

bins = [None] * len(data)

for i in data:
  for b in range(len(bins)):
    binn = bins[b]
    if binn == None:
      if b == 0:
        bins[0] = [i]
      elif bins[b-1][-1] < i:
        bins[b] = bins[b-1] + [i]
      break

    if b != 0 and i > bins[b-1][-1] and i < binn[-1]:
      bins[b] = bins[b-1] + [i]
      break
    elif i < binn[-1]:
      if b == 0 or i > binn[-1]:
        binn[-1] = i
      continue
  
for b in bins:
  if b == None:
    print(prev)
    exit()
  prev = b
