class Solution(object):
  def twoSum(self, nums, target):
      """
      :type nums: List[int]
      :type target: int
      :rtype: List[int]
      """
      d = {}
      pos = 0
      for n in nums:
        c = target - n
        if (c in d):
         return [d[c], pos]
        d[n] = pos
        pos += 1
      return [None]


