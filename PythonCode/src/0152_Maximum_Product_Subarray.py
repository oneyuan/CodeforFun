import sys

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        res = nums[0]
        pos = nums[0]
        neg = nums[0]
        for i in range(1, n):
            if nums[i] < 0:
                pos, neg = neg, pos
            neg = min(nums[i], neg*nums[i])
            pos = max(nums[i], pos*nums[i])
            res = max(pos, res)
        return res
    
    def maxProduct0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        pre_pos = None
        pre_neg = None

        ans = -sys.maxsize

        for i in range(len(nums)):
            if nums[i] > 0:
                pre_pos = (nums[i] * pre_pos) if pre_pos else nums[i]
                pre_neg = (nums[i] * pre_neg) if pre_neg else pre_neg
            else:
                t = pre_pos
                pre_pos = (nums[i] * pre_neg) if pre_neg else pre_neg
                pre_neg = (nums[i] * t) if t else nums[i]

            if pre_neg is not None and pre_neg > ans:
                ans = pre_neg

            if pre_pos is not None and pre_pos > ans:
                ans = pre_pos

        return ans
