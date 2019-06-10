#
# @lc app=leetcode id=398 lang=python3
#
# [398] Random Pick Index
#
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        n = len(self.nums)
        res = -1
        count = 0
        for i in range(n):
            if self.nums[i] != target:
                continue
            if random.randint(0, count) == 0:
                res = i
            count += 1
        return res

    def pick0(self, target: 'int') -> 'int':
        import random
        ind = None
        cnt = 0
        for i, n in enumerate(self.nums):
            if n == target:
                cnt += 1
                if random.random() < 1.0/cnt:
                    ind = i

        return ind

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

