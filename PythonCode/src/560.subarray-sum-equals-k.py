#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, s = 0, 0
        dic = {0: 1}
        n = len(nums)
        for i in range(n):
            s += nums[i]
            if (s-k) in dic:
                count += dic[s-k]
            dic[s] = dic.get(s, 0) + 1
        return count

    def subarraySum_1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        count = 0
        for i in range(1, n+1):
            for j in range(i, n+1):
                dp[i][j] = nums[j-1] + dp[i][j-1]
                if dp[i][j] == k:
                    count += 1
        return count

