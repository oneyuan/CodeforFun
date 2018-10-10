class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backTrack(res, nums, tmp, start):
            if len(tmp) > 0:
                t = tmp.copy()
                res.append(t)
            for i in range(start, len(nums)):
                tmp.append(nums[i])
                backTrack(res, nums, tmp, i+1)
                tmp.pop()
            
            
        t = [[]]
        res =[[]]
        tmp = []
        dic = {}
        nums.sort()
        backTrack(t, nums, tmp, 0)
        t.sort()
        for i in range(1,len(t)):
            if t[i] != t[i-1]:
                e = t[i].copy()
                res.append(e)
        return res
    
    def subsetsWithDup0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        nums.sort()
        # from collections import Counter
        # counter = Counter(nums)
        # nums_ = list(set(nums))
        # def helper(nums_):
        #     if not nums_: return [[]]
        #     tmp = helper(nums_[1:])
        #     ret = tmp
        #     for i in range(counter[nums_[0]]):
        #         ret += [[nums_[0]]*(i+1)+ ls for ls in tmp]
        #     return ret
        # return helper(nums_)
        count = 0
        cur = nums[0]
        ret = [[]]
        for i in range(len(nums)):
            if cur == nums[i]:
                count += 1
            else:
                tmp = []
                for j in range(count):
                    tmp.extend([a + [nums[i-1]]*(j+1) for a in ret])
                ret += tmp
                count = 1
                cur = nums[i]
        print(count)
        if count > 0:
            tmp = []
            for j in range(count):
                tmp.extend([a + [nums[-1]]*(j+1) for a in ret])
            ret += tmp
        return ret