class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ""
        factorial = [1]
        su = 1
        for i in range(1,n):
            su = su*i
            factorial.append(su)
        numbers = []
        for i in range(1, n+1):
            numbers.append(i)
        t = n - 1
        k -= 1
        for _ in range(n):
            index = k//factorial[t]
            res += str(numbers[index])
            numbers.remove(numbers[index])
            k -= index*factorial[t]
            t -= 1
        return res
    
    def getPermutation0(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        n_mark_arr = [1]
        for idx in range(1, n):
            n_mark_arr.append(idx * n_mark_arr[-1])
        n_arr = [str(idx) for idx in range(1, 1 + n)]
        
        res = ''
        for i in range(-1, -n-1, -1):
            idx = (k - 1) // n_mark_arr[i]
            k = k % n_mark_arr[i]
            res += n_arr[idx]
            n_arr.pop(idx)
        return res