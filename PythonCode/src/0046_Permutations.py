class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backTrack(nums, res, tmp):
            if len(tmp) == len(nums):
                t = tmp.copy()
                res.append(t)
            else:
                for i in range(len(nums)):
                    if nums[i] in tmp:
                        continue
                    else:
                        tmp.append(nums[i])
                        backTrack(nums, res, tmp)
                        tmp.pop()
        
        res = []
        tmp = []
        backTrack(nums, res, tmp)
        return res
    
    def permute0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations
        return list(permutations(nums))
    
    def permute1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(a, b=[]):
            if not a:
                return out.append(list(b))
            for index, num in enumerate(a):
                helper(a[:index] + a[index + 1:], b + [num])
        out = []
        helper(nums)
        return out