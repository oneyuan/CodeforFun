#
# @lc app=leetcode id=1054 lang=python3
#
# [1054] Distant Barcodes
#
# https://leetcode.com/problems/distant-barcodes/description/
#
# algorithms
# Medium (36.63%)
# Likes:    60
# Dislikes: 2
# Total Accepted:    3.1K
# Total Submissions: 8.6K
# Testcase Example:  '[1,1,1,2,2,2]'
#
# In a warehouse, there is a row of barcodes, where the i-th barcode is
# barcodes[i].
# 
# Rearrange the barcodes so that no two adjacent barcodes are equal.  You may
# return any answer, and it is guaranteed an answer exists.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,1,1,2,2,2]
# Output: [2,1,2,1,2,1]
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,1,1,1,2,2,3,3]
# Output: [1,3,1,3,2,1,2,1]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= barcodes.length <= 10000
# 1 <= barcodes[i] <= 10000
# 
# 
# 
# 
# 
#
import collections
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = {}
        n = len(barcodes)
        if n == 0:
            return []
        for barcode in barcodes:
            if barcode in count:
                count[barcode] += 1
            else:
                count[barcode] = 1
        barcodes.sort()
        barcodes.sort(key = lambda x:count[x])
        res = [0 for _ in range(n)]
        for i in range(0, n ,2):
            res[i] = barcodes.pop()
        for j in range(1, n, 2):
            res[j] = barcodes.pop()
        return res

    def rearrangeBarcodes0(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        idxes = collections.deque(list(range(0, n, 2)) + list(range(1, n, 2)))
        counter = collections.Counter(barcodes)
        top_1, freq, counter = self.top(counter)
        ans = [None] * n
        for _ in range(freq):
            ans[idxes.popleft()] = top_1
        for num, cnt in counter.items():
            for _ in range(cnt):
                ans[idxes.popleft()] = num
        return ans
    
    def top(self, counter):
        most = 0
        res = None 
        for key, val in counter.items():
            if val > most:
                most = val 
                res = key
        del counter[res]
        return res, most, counter 

