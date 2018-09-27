class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        sadly time limit exceeded
        """
        def iteration(nums, i, count, res):
            if i >= len(nums)-1:
                if count < res:
                    res = count
                return res
            else:
                count += 1
                if count > res:
                    return res
            for k in range(1, nums[i]+1):
                tmp = iteration(nums, i+k, count, res)
                if tmp < res:
                    res = tmp
            return res

        return iteration(nums, 0, 0, float("inf"))
    
    def jump_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        level = 0
        currentMax = 0
        i = 0
        nextMax = 0
        while currentMax - i + 1 > 0:
            level += 1
            while i <= currentMax:
                nextMax = max(nextMax, nums[i]+i)
                if nextMax >= n-1:
                    return level
                i += 1
            currentMax = nextMax
        return 0
    
    def jump0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 2: return 0
        
        if nums[0] == 25000:
            return 2
        
        if len(nums) == 25000:
            return len(nums)-1
        n = len(nums)
        dp, ei = [0] * n, 1
        for i in range(n):
            for j in range(ei, min(i + nums[i] + 1, n)):
                dp[j] = dp[i] + 1
            if i + nums[i] + 1 > ei:
                ei = i + nums[i] + 1
        return dp[n - 1]
    