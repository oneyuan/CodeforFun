class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        using stack
        """
        res = 0
        s = []
        for i in range(len(height)):
            while s and height[i] > height[s[-1]]:
                top = s.pop()
                if s:
                    w = i - s[-1] - 1
                    l = min(height[s[-1]], height[i]) - height[top]
                    res += (w * l)
            s.append(i)
        return res
    
    def trap1(self, height):
        """
        :type height: List[int]
        :rtype: int
        brute forth
        """
        res = 0
        n = len(height)
        for i in range(1, n-1):
            max_left = max(height[:i])
            max_right = max(height[i+1:])
            tmp = min(max_left, max_right) - height[i]
            if tmp > 0:
                res += tmp
        return res
    
    def trap2(self, height):
        """
        :type height: List[int]
        :rtype: int
        dynamic programming
        """
        res = 0
        n = len(height)
        left, right = 0, 0
        r_left = []
        r_right = []
        for  i in range(n):
            if height[i] > left:
                left = height[i]
                r_left.append(0)
            else:
                r_left.append(left-height[i])
        for j in range(n-1, -1, -1):
            if height[j] > right:
                right = height[j]
                r_right.append(0)
            else:
                r_right.append(right-height[j])
        for i in range(n):
            res += (min(r_left[i], r_right[n-i-1]))
        return res
    
    def trap3(self, height):
        """
        :type height: List[int]
        :rtype: int
        two pointers
        """
        res = 0
        if not height:
            return 0
        left = height[0]
        right = height[-1]
        l = 0
        r = len(height) - 1
        while l < r:
            if left < right:
                l += 1
                if height[l] < left:
                    res += (left - height[l])
                else:
                    left = height[l]
            else:
                r -= 1
                if height[r] < right:
                    res += (right - height[r])
                else:
                    right = height[r]
        return res
    
    def trap0(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        global_max = height.index(max(height))
        part1 = height[1:global_max + 1]
        part2 = height[global_max:]
        part2.reverse()
        total_rain = 0
        left_boundary = height[0]
        for h in part1:
            if h > left_boundary:
                left_boundary = h
            else:
                total_rain += left_boundary - h
        left_boundary = height[-1]
        for h in part2:
            if h > left_boundary:
                left_boundary = h
            else:
                total_rain += left_boundary - h
        return total_rain
                    