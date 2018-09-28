class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backTrack(nums, tmp, res, used):
            if len(tmp) == len(nums):
                t = tmp.copy()
                res.append(t)
            else:
                for i in range(len(nums)):
                    if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                        continue
                    else:
                        used[i] = True
                        tmp.append(nums[i])
                        backTrack(nums, tmp, res, used)
                        tmp.pop()
                        used[i] = False
        
        res = []
        tmp = []
        used = [False for _ in range(len(nums))]
        nums.sort()
        backTrack(nums, tmp, res, used)
        return res
    
    def permuteUnique0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        permutations = [[]]
        
        for head in nums: # here we insert either a new element to every slot, or insert an existing element, but only up to the first occurrence
            permutations = [rest[:i]+[head]+rest[i:] for rest in permutations for i in range((rest+[head]).index(head)+1)]
            
        return permutations
    
    