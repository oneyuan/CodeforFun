class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j, k = 0, 0
        for i in range(n):
            tmp = nums[i]
            nums[i] = 2
            if tmp < 2:
                nums[j] = 1
                j += 1
            if tmp == 0:
                nums[k] = 0
                k += 1
    
    def sortColors0(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) <= 1:
            return
        cur0 = 0
        cur2 = len(nums) - 1
        i = 0
        while i <= cur2:
            if nums[i] == 0:
                # swap with cur0
                j = cur0
                while j < i and nums[j] == 0:
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]
                cur0 = j
            elif nums[i] == 2:
                # swap with cur2
                j = cur2
                while j > i and nums[j] == 2:
                    j -= 1
                if j == i:
                    print(nums)
                    return
                nums[i], nums[j] = nums[j], nums[i]
                cur2 = j
                i -= 1
            i += 1