class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        nums = []
        k = m + n
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        if i == m:
            while j < n:
                nums.append(nums2[j])
                j += 1
        elif j == n:
            while i < m:
                nums.append(nums1[i])
                i += 1
        if k % 2 == 0:
            t = int(k/2)
            return (nums[t] + nums[t-1]) / 2.0
        else:
            return float(nums[k//2])
    
    def findMedianSortedArrays0(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 1:
            return float(nums[len(nums)//2])
        return (nums[len(nums)//2-1] + nums[len(nums)//2]) / 2