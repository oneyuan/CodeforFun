class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        count = 0
        pre = nums[0]
        if n == 1:
            return pre
        for num in nums:
            if num != pre:
                if count == 1:
                    return pre
                pre = num
                count = 1
            else:
                count += 1
        return num

    def singleNumber0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for n in nums:
            sum ^= n

        return sum
