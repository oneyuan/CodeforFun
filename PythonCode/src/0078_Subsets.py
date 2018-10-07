class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backTrack(res, tmp, nums, start):
            if len(tmp) > 0:
                t = tmp.copy()
                res.append(t)
            for i in range(start, len(nums)):
                tmp.append(nums[i])
                backTrack(res, tmp, nums, i+1)
                tmp.pop()
        
        res =  [[]]
        tmp = []
        backTrack(res, tmp, nums, 0)
        return res
    
    def subsets0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper(res, [], nums, 0)
        return res
    
    def helper(self, res, path, nums, start):
        res.append(path)
        
        for i in range(start, len(nums)):
            self.helper(res, path + [nums[i]], nums, i + 1)
    