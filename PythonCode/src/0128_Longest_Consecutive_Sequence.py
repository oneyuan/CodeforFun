class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dic = {}
        res = 0
        for i in range(n):
            if nums[i] not in dic:
                left = dic.get(nums[i]-1, 0)
                right = dic.get(nums[i]+1, 0)
                tmp = left + right + 1
                dic[nums[i]] = tmp
                res = max(res, tmp)
                dic[nums[i]-left] = tmp
                dic[nums[i]+right] = tmp
        return res
    
    def longestConsecutive0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums = sorted(set(nums))
        maxlen, start = 1, 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                maxlen = max(maxlen, (i-start))
                start = i
        maxlen = max(maxlen, (len(nums)-start))
        return maxlen
    
    def longestConsecutive1(self, nums):
        longest = 0
        num_set = set(nums)

        for num in num_set:
            if num-1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest
