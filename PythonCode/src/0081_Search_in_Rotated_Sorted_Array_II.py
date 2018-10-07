class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]: # tricky part
                l += 1
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
    
    def search0(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        length = len(nums)
        if length == 1:
            return target == nums[0]
        def s(start,end):
            while nums[start] == nums[end] and start < end:
                start += 1
            if start == end and nums[start] != target:
                return -2
            if nums[start] < nums[end]:
                if target < nums[start] or target > nums[end]:
                    return -2
            elif nums[start] > nums[end]:
                if target < nums[start] and target > nums[end]:
                    return -2
            if end - start <= 3:
                index = start
                while index <= end:
                    if target == nums[index]:
                        return index
                    index += 1
                return -1
            split = ((end - start)>>1) - 1
            result = s(start,start+split)
            if result == -2:
                result = s(start+split+1,end)
            return result
        result = s(0,length - 1)
        return result >= 0