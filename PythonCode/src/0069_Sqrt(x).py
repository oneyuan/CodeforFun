import math

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        s = 0
        e = x
        while s < e:
            m = (s+e)//2
            if m*m == x:
                return m
            elif m*m > x:
                e = m
            else:
                if s == m:
                    break
                s = m
        return s
    
    def mySqrt0(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.sqrt(x))
    
    def mySqrt1(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if (x == 0):
            return x
        
        low = 1
        high = x
        ans = 1
        while (low <= high):
            mid = low + (high - low) // 2
            if (mid * mid <= x):
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
            
        return ans