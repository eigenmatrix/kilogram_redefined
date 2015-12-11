
def adder(data):
    a, b, c = data[0], data[1], data[2]
    sum = a + b + carry
    if sum > 10:
        out = sum - 10
        carry_out = 1
    elif sum == 10:
        out = 0
        carry_out = 1
    else:
        out = sum
        carry_out = 0

    return [out, carry_out]

a = [1,2,4,5,4,3,2,1,5,5,4,3,2]
b = [6,5,1]

import math
if __name__ == "__main__":
    output = []
    carry = 0
    a = a[::-1]
    b = b[::-1]
    size = max(len(a), len(b))
    for i in range(size):
        
        if i >= len(b):
            forward = adder([a[i], 0, carry])
        elif i >= len(a):
            forward = adder([0, b[i], carry])
        else:
            forward = adder([a[i], b[i], carry])
        output.append(forward[0])
        carry = forward[1]
    print(output[::-1])


