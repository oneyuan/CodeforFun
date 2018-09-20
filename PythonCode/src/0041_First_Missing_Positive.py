class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        while i < len(nums):
            if nums[i] == "a":
                i += 1
                continue
            if nums[i] <= 0:
                nums[i] = 0
            elif nums[i] > n:
                nums[i] = 0
            else:
                if i < n and i < nums[i]-1:
                    nums.append(nums[nums[i]-1])
                nums[nums[i]-1] = "a"
            i += 1
        for j in range(n):
            if nums[j] != "a":
                return j+1
        return n+1
    
    def firstMissingPositive0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort_nums = sorted(nums)
        if sort_nums != []:
            if sort_nums[0] > 1:
                return 1
            for i in range(len(sort_nums)):
                if sort_nums[i] + 1 > 0:
                    if sort_nums[i] + 1  in sort_nums:
                        continue
                    else:
                        return sort_nums[i] + 1
                else:
                    min_num = 1
                    while(min_num < sort_nums[i+1]):
                        if min_num not in sort_nums:
                            return 1
                        else:
                            min_num += 1
        else:
            return 1