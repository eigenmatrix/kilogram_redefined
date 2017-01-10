class Solution(object):
  def twoSum(self, nums, target):
      """
      :type nums: List[int]
      :type target: int
      :rtype: List[int]
      """
      d = {}
      pos = 0
      half = target/2
      for n in nums:
        if not(n in d):
          d[n] = pos
        else:
          if n == half:
            return [d[n],pos]
        pos += 1
        
      for n in nums:
        c = target - n
        if c == n:
          continue
        elif (c in d) and (n in d):      
          return [d[c], d[n]]

