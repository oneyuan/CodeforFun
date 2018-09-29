class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return pow(x, n)
    
    def myPow1(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        time limited exceeded use bitwise operation can fix it
        """
        if  n == 0:
            return 1
        elif n > 0:
            res = x
            i = 1
            while i < n:
                res = x * res
                i += 1
        else:
            if x == 0:
                return -1
            tmp = x
            i = 1
            while i < -n:
                tmp = x * tmp
                i += 1
            res = 1/tmp
        return res
    
    def myPow0(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = -n
        res = 1.
        while n:
            if n&1 == 1: res *= x
            n >>= 1
            x *= x
        return res