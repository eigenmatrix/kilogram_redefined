'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = nums[0]
        b = nums[0]
        for i in nums[1:]:
        '''
        If the total sum of the candidate range falls below
        the current number then just start a new range.
        The range prio would have negatively impacted the new sum
        '''
          s = max(i, s + i) 
          b = max(s, b)
        return b
