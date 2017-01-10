class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        data = sorted(nums)
        median = data[len(data)/2]
        over = 0
        under = 0
        for n in nums:
          if n < median:
            under += (median - n)
          else:
            over += (n - median)
        return over + under
