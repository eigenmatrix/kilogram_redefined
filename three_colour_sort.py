#three colours, the cooler way.
#I don't want to create 3 counters because thats too easy

data = [0,1,2,1,2,0,0,0,1,1,1,1,1,2,0]
front = 0
back = len(data) - 1

for c in range(3):
  while front <= back:
    if data[front] == c:
      front += 1
      continue

    while data[back] != c and front != back:
      back -= 1
    if front == back:
      break
    
    data[back] = data[front]
    data[front] = c
    back -= 1
    front += 1
  back = len(data) - 1
print(data)
