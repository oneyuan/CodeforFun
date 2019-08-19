#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        res = [0 for _ in range(n)]
        stack = []
        for i in range(n-1, -1, -1):
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res

    def dailyTemperatures0(self, T: List[int]) -> List[int]:
        res = [0]*len(T)
        i = len(T)-2
        cons = len(T)-1
        while i >= 0:
            q = i+1
            while True:
                if T[i] < T[q]:
                    res[i] = q-i
                    break
                else:
                    if res[q] == 0:
                        res[i] = 0
                        break
                    q += res[q]
            i -= 1
        return res

