import math
import itertools

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backTrack(res, tmp, start, n, k):
            if k == 0:
                t = tmp.copy()
                res.append(t)
                return 0
            for i in range(start, n+1):
                tmp.append(i)
                backTrack(res, tmp, i+1, n, k-1)
                tmp.pop()
            
        tmp = []
        res = []
        backTrack(res, tmp, 1, n, k)
        return res
    
    def combine0(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return list(itertools.combinations((i for i in range(1, n + 1)), k))
    
    def combine1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        pool=range(1,n+1)
        result=[]
        indices=list(range(k))
        result.append([pool[i] for i in indices])
        while True:
            for i in reversed(range(k)):
                if indices[i]-i!=n-k:
                    break
            else:
                return result
            indices[i]+=1
            for j in range(i+1,k):
                indices[j]=indices[j-1]+1
            result.append([pool[i] for i in indices])
            
    def combine2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []
        nums = list(range(1, k+1))
        
        count = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))
        
        for _ in range(count):
            ret.append(nums.copy())
            
            for j in reversed(range(k)):
                if nums[j] < n - (k - j - 1):
                    nums[j] += 1
                    for l in range(j+1, k):
                        nums[l] = nums[l-1] + 1
                    break
        return ret
    
    
        