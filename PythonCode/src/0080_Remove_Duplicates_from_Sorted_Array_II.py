class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        if len(nums) == 0:
            return 0
        pre = nums[0]
        i = 0
        while i < len(nums):
            if nums[i] == pre:
                count += 1
                if count > 2:
                    nums.remove(pre)
                else:
                    i += 1
            else:
                pre = nums[i]
                count = 1
                i += 1
        return i
    
    def removeDuplicates0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0       ####wrong: 'i £½ 0' invalid character or identifier   chinese style   £½ vs =
        for n in nums:
            # if n > nums[i-2] or i < 2:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i