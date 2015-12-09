"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

num = 100
root = int(math.sqrt(num))

fact_list = list(range(1,root))
for x in range(len(fact_list)):
  if num%fact_list[x] == 0:
      print(fact_list[x])
      
    
    
