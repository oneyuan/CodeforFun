class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        k = []
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                if nums[i] * 2 == target:
                    return [dic[nums[i]],i]
            else:
                dic[nums[i]] = i
            k.append(target - nums[i])
        for j in range(len(k)):
            if k[j] in dic:
                if k[j] != nums[j]:
                    return [j,dic[k[j]]]
    
    def twoSum0(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp = {}
        for i in range(len(nums)):
            if target - nums[i] in tmp:
                return(tmp[target - nums[i]], i)
            else:
                tmp[nums[i]] = i
        