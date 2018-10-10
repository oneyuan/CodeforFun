class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        i = 0
        while i < 1<<n:
            res.append(i^ i>>1)
            i += 1
        return res
    
    