#-*- coding: utf-8 -*-
import heapq
import math
import copy
#from builtins import int, False
#from pstats import count_calls
import collections
import sys
import re
import operator
import queue
import string
from collections import deque


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.res = [0]
        for i in range(len(nums)):
            self.res.append(nums[i] + self.res[i])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.res[j+1] - self.res[i]
    """
    def __init__(self, nums):
        
        :type nums: List[int]
        
        self.dp = nums
        for i in range(1, len(nums)):
            self.dp[i] = self.dp[i-1] + nums[i]
        

    def sumRange(self, i, j):
        
        :type i: int
        :type j: int
        :rtype: int
        
        return self.dp[j] - self.dp[i - 1] if i != 0 else self.dp[j]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)            
    """
    
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    '''
    classdocs
    '''
    def maximumProduct(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        min_num = nums[0]
        s_min = nums[1]
        max_num = nums[-1]
        s_max = nums[-2]
        t_max = nums[-3]
        a = min_num * s_min * max_num
        b = max_num * s_max * t_max
        if a < b:
            return(b)
        else:
            return(a)



    def maximumProduct2(self,nums):   #heapq.nlargest() and heapq.nsmallest() can do best for now  
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = -1000
        s_max = -1000
        t_max = -1000
        min_num = 1000
        s_min = 1000
        
        for i in range(len(nums)):
            if nums[i] > max_num:
                t_max = s_max
                s_max = max_num
                max_num = nums[i]
            elif nums[i] > s_max:
                t_max = s_max
                s_max = nums[i]
            elif nums[i] > t_max:
                t_max = nums[i]
            if nums[i] < min_num:
                s_min = min_num
                min_num = nums[i]
            elif nums[i] < s_min:
                s_min = nums[i]

        print (max_num, s_max, t_max, min_num, s_min)
        a = max_num * s_max * t_max  
        b = min_num * s_min * max_num       
        if a > b:
            return(a)
        else:
            return(b)
        
        
    def maximumProduct0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0]*a[1]*a[2], a[0]*b[0]*b[1])
        
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        M = len(matrix)
        N = len(matrix[0])
        if M> 1 and N >1:
            for i in range(M-1):
                for j in range(N-1):
                    if matrix[i][j] == matrix[i+1][j+1]:
                        a = 0
                    else: 
                        a = 1
                        return False
            if a == 0:
                return True
        else:return True
        
    def isToeplitzMatrix0(self,matrix):
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True
    
    def dominantIndex(self, nums): #ֻ��һ��Ԫ�ص��б�     ��˳�����ε������б�     �ݼ����б�      ��0���б�    ��ʼֵ�����Ƿ���ȷ
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = 0
        s_max = 0
        max_num_index = 0
        if len(nums) != 1:
            for i in range(len(nums)):
                if nums[i] > max_num:
                    s_max = max_num
                    max_num = nums[i]
                    max_num_index = i
                elif nums[i] > s_max:
                    s_max = nums[i]
            if max_num >= 2 * s_max:
                return max_num_index
            else: return -1
        else:return 0
        
    def dominantIndex0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        m = max(nums)
        ind = nums.index(m)
        del nums[ind]
        m_2 = max(nums)
        return ind if m >= 2*m_2 else -1
       

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        Hint: f[i] = cost[i] + min(f[i +1], f[i+2]) f[i is the final cost to climb to top from step i.]
        """
        f = [1] * 1000
        f[len(cost)-1] = cost[-1]
        f[len(cost)-2] = cost[-2]
        i = len(cost) - 3
        while i >= 0:
            f[i] = cost[i] + min(f[i+1], f[i+2])
            i -= 1
        if f[0] < f[1]:
            return f[0]
        else:
            return f[1]
        
    def minCostClimbingStairs0(self, cost):
        n = len(cost)
        
        if n==0 or n==1: return 0 
        
        minCost0, minCost1 = cost[0],cost[1]
        
        for i in range(2,n):
            minCost0, minCost1 = minCost1, min(minCost0, minCost1) + cost[i]
        
        return min(minCost0, minCost1)
    
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [] return -1 sum([]) = 0
        """
        a = 0
        t = sum(nums)
        if len(nums) > 1:
            for i in range(len(nums)):
                x = t - a - nums[i]
                if x  == a:
                    return i
                a += nums[i]
            return -1
        else:
            return -1
        
    def pivotIndex0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1
    
    
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 1:
            return True
        if len(bits) == sum(bits) + 1:
            if sum(bits) % 2 == 1:
                return False
            else:
                return True
        i = -2 
        while abs(i) <= len(bits):
            if bits[i] == 0 and abs(i) % 2 == 0:
                return True
            elif bits[i] == 0 and  abs(i) % 2 == 1:
                return False
            i -= 1
            
            
    def isOneBitCharacter0(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        N = len(bits)
        flag = 0
        i = N-2
        if bits[N-2] == 0:
            return True
        else:
            while i>=0 and bits[i]==1:
                flag += 1
                i -= 1
            if flag%2 == 0:
                return True
            else:
                return False
            
            
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = {}
        b = []
        c = {}
        nums.reverse()
        r = nums[:]
        nums.reverse()
        for i in range(len(nums)):
            if nums[i] in a:
                a[nums[i]] += 1
            else:
                a[nums[i]] = 1
        y = 0
        for x in a:
            if a[x] > y:
                y = a[x]
                b = [x]
            elif a[x] == y:
                b.append(x)
        if len(b) == 1:
            begin = nums.index(b[0])
            end = len(nums) - r.index(b[0]) - 1
            return end - begin + 1
        else:
            for t in range(len(b)):
                begin = nums.index(b[t])
                end = len(nums) - r.index(b[t]) - 1
                c[t] = end - begin + 1
            return min(c.values())
        
    def findShortestSubArray0(self, nums):
        
        diction = {}
        
        for i in nums:
            if i not in diction:
                diction[i] = 1
            else:
                diction[i] += 1
            
        degree = max(list(diction.values()))
        
        if degree == 1:
            return 1
        
        max_value = []
        
        for i in diction:
            if diction[i] == degree:
                max_value.append(i)
        
        min_length = 10000000000
        
        for i in max_value:
            head = 0
            tail = 0
            for j in range(len(nums)):
                if nums[j] == i:
                    head = j
                    break
            for j in range(len(nums)-1,-1,-1):
                if nums[j] == i:
                    tail = j
                    break
            if min_length > tail - head + 1:
                min_length = tail - head + 1
        
        return min_length
    
    
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        a = []
        c = []
        for  i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    a.append((i,j))

        if len(a) == 0:
            return 0

        def lookAround(tup,b,a):
            if (tup[0],tup[1]+1) in a and (tup[0],tup[1]+1) not in b:
                b.append((tup[0],tup[1]+1))
                a.remove((tup[0],tup[1]+1))
                lookAround((tup[0],tup[1]+1),b,a)
            if (tup[0],tup[1]-1) in a and (tup[0],tup[1]-1) not in b:
                b.append((tup[0],tup[1]-1))
                a.remove((tup[0],tup[1]-1))
                lookAround((tup[0],tup[1]-1),b,a)
            if (tup[0]-1,tup[1]) in a and (tup[0]-1,tup[1]) not in b:
                b.append((tup[0]-1,tup[1]))
                a.remove((tup[0]-1,tup[1]))
                lookAround((tup[0]-1,tup[1]),b,a)
            if (tup[0]+1,tup[1]) in a and (tup[0]+1,tup[1]) not in b:
                b.append((tup[0]+1,tup[1]))
                a.remove((tup[0]+1,tup[1]))
                lookAround((tup[0]+1,tup[1]),b,a)
        
        for item in a:
            b = [item]
            lookAround(item,b,a)
            c.append(len(b))

        return max(c)
    
    
    def maxAreaOfIsland0(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(line, column):
            grid[line][column] = 0
            result = 1
            if line>0:
                if grid[line-1][column]:
                    result+=dfs(line-1, column)
            if line<len(grid)-1:
                if grid[line+1][column]:
                    result+=dfs(line+1, column)
            if column>0:
                if grid[line][column-1]:
                    result+=dfs(line, column-1)
            if column<len(grid[line])-1:
                if grid[line][column+1]:
                    result+=dfs(line, column+1)
            return result
        result = 0
        for line in range(len(grid)):
            for column in range(len(grid[line])):
                if grid[line][column]:
                    result = max(result,dfs(line, column))
        return result
        
        
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b= [1]
        count = 1
        if len(nums) == 0:   #consider nums is null
            return 0
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                if i == len(nums) - 2:
                    count += 1
                    b.append(count)
                else:
                    count += 1
            else:
                b.append(count)
                count = 1
        return max(b)
    
    def findLengthOfLCIS0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        cur_len = 1
        max_len = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                cur_len = cur_len + 1
            else:
                cur_len = 1
                
            if cur_len > max_len:
                max_len = cur_len
        return max_len
    
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        #misunderstand the meaning[1] [-1,4,2,3] [4,2,1] [3,4,2,3] [2,3,3,2,4]
        """
        b = []
        count = 1
        if len(nums) == 1:
            return True
        for i in range(1,len(nums)):
            if len(b) > 2:
                return False
            if nums[i] >= nums[i-1]:
                if i == len(nums)-1:
                    count += 1
                    b.append(count)
                else:
                    count += 1
            elif i == len(nums) - 1:
                b.append(count)
                b.append(1)
            else:
                b.append(count)
                count = 1
                c = nums[i-2:i+2]
        if len(b) > 2:
            return False
        elif len(b) == 1:
            return True
        elif b[0] == 1:
            return True
        else:
            if c[1] <= c[3] or c[0] <= c[2]:
                return True
            else:
                return False
            
    def checkPossibility0(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        possibility_flag = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if possibility_flag:
                    return False
                possibility_flag = True
                if (i-2 < 0 or i-2 >= 0 and nums[i-2] < nums[i]) or (i+1 >= len(nums) or i+1 < len(nums) and nums[i+1] > nums[i-1]):
                    pass
                else:
                    return False
        return True
    
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
         a[:], list(a), a*1, copy.copy(a) all can create a new list but
        besides copy.deepcopy there is no way to deep copy a list which contains lists
        """
        N = copy.deepcopy(M)
        for i in range(len(M)):
            for j in range(len(M[0])):
                count = 0
                temp = 0
                for a in (i-1, i , i+1):
                    for b in (j-1, j, j+1):
                        if 0 <= a < len(M) and 0 <= b < len(M[0]):
                            temp += M[a][b]
                            count += 1
                N[i][j] = math.floor(temp/count)
        return N


    def imageSmoother0(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(M), len(M[0])
        if m + n <= 2: return M
        mat = [[0] * n for i in range(m)]
        if m == 1:
            mat[0][0] = (M[0][0] + M[0][1]) // 2
            for j in range(1, n - 1):
                mat[0][j] = (M[0][j - 1] + M[0][j] + M[0][j + 1]) // 3
            mat[0][n - 1] = (M[0][n - 2] + M[0][n - 1]) // 2
            return mat
        if n == 1:
            mat[0][0] = (M[0][0] + M[1][0]) // 2
            for i in range(1, m - 1):
                mat[i][0] = (M[i - 1][0] + M[i][0] + M[i + 1][0]) // 3
            mat[m - 1][0] = (M[m - 2][0] + M[m - 1][0]) //2
            return mat
        
        # m, n >= 2
        # four vertex
        mat[0][0] = (M[0][0] + M[0][1] + M[1][0] + M[1][1]) // 4
        mat[0][n - 1] = (M[0][n - 2] + M[0][n - 1] + M[1][n - 2] + M[1][n - 1]) // 4
        mat[m - 1][0] = (M[m - 2][0] + M[m - 2][1] + M[m - 1][0] + M[m - 1][1]) // 4
        mat[m - 1][n - 1] = (M[m - 2][n - 2] + M[m - 2][n - 1] + M[m - 1][n - 2] + M[m - 1][n - 1]) // 4
        
        # first row
        for i in range(1, n - 1):
            mat[0][i] = (M[0][i - 1] + M[0][i] + M[0][i + 1] + M[1][i - 1] + M[1][i] + M[1][i + 1]) // 6
        # median row
        for i in range(1, m - 1):
            # first col
            mat[i][0] = (M[i - 1][0] + M[i - 1][1] + M[i][0] + M[i][1] + M[i + 1][0] + M[i + 1][1]) // 6
            # core
            for j in range(1, n - 1):
                mat[i][j] = (M[i - 1][j - 1] + M[i - 1][j] + M[i - 1][j + 1] + M[i][j - 1] + M[i][j] + M[i][j + 1] + M[i + 1][j - 1] + M[i + 1][j] + M[i + 1][j + 1]) // 9
            # last col
            mat[i][n - 1] = (M[i - 1][n - 2] + M[i - 1][n - 1] + M[i][n - 2] + M[i][n - 1] + M[i + 1][n - 2] + M[i + 1][n - 1]) // 6
            
        # last row
        for i in range(1, n - 1):
            mat[m - 1][i] = (M[m - 2][i - 1] + M[m - 2][i] + M[m - 2][i + 1] + M[m - 1][i - 1] + M[m - 1][i] + M[m - 1][i + 1]) // 6
        return mat
    
    
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        m = sum(nums[0:k])
        b = [m]
        if len(nums) == k:
            return sum(nums)/k
        print (m)
        for i in range(1,len(nums)-k+1):
            m = m + nums[i+k-1] - nums[i-1]
            b.append(m)
        return max(b)/k
    
    def findMaxAverage0(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """        
        _sum = sum(nums[:k])
        maxsum = _sum        
        for i in range(k, len(nums)):
            _sum = _sum - nums[i-k] + nums[i]            
            if _sum > maxsum:
                maxsum = _sum                            
        return maxsum/k
            
        
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]]
        :type n: int
        :rtype: bool
        state of art
        """
        count = 0
        i = 0
        if (len(flowerbed) + 1) // 2 < sum(flowerbed) + n:
            return False
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 2
            else:
                if i == 0 and flowerbed[i+1] == 0:
                    count +=1
                    i += 2
                elif i == len(flowerbed) -1 and flowerbed[i-1] == 0:
                    count +=1
                    i += 2
                elif i == len(flowerbed) -2 and flowerbed[i+1] == 0:
                    count += 1
                    i += 2
                elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    count += 1
                    i += 2
                else:
                    i += 2
        if count >= n:
            return True
        else:
            return False

    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = []
        if len(nums)==1:
            return 0
        a = sorted(nums)
        i=0
        while i <len(nums):
            if nums[i] == a[i]:
                if i == len(nums)-1:
                    if len(s) == 0:
                        return 0
                i += 1
            else:
                s.append(i)
                i += 1
        return s[-1] - s[0] + 1
    
    def findUnsortedSubarray0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
#left
        while left<len(nums)-1 and nums[left]<=nums[left+1]:
            left+=1
        if left==len(nums)-1:
            return 0
        min_right=min(nums[left+1:])
        while left>=0 and nums[left]>min_right:
            left-=1
#right
        while right>0 and nums[right]>=nums[right-1]:
            right-=1
        if right==0:
            return 0
        max_left=max(nums[:right])
        while right<=len(nums)-1 and max_left>nums[right]:
            right+=1
        return right-left-1
    
    
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row = len(nums)
        colum = len(nums[0])
        count = -1
        t = 0
        matrix = []
        for i in range(r):
            matrix.append([])
        if row * colum != r * c:
            return nums
        for i in range(row):
            for j in range(colum):
                count += 1
                if count <= c-1:
                    matrix[t].append(nums[i][j])
                    if count == c-1:
                        t += 1
                        count = -1
        return matrix
    
    def matrixReshape0(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) == r * c:
            ret = []
            tmp_row = []
            jj = 0
            for row in nums:
                for nm in row:
                    tmp_row.append(nm)
                    jj += 1
                    if jj == c:
                        jj = 0
                        ret.append(tmp_row)
                        tmp_row = []
            return ret
        else:
            return nums
        
    
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        s = 0
        for i in range(0,len(nums),2):
            s += nums[i]
        return s
    
    def arrayPairSum0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])
    
    
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        b = set(nums)
        c = [i for i in b]
        count = 0
        if k == 0:
            for i in d:
                if d[i] > 1:
                    count += 1
            return count
        for j in range(len(c)):
            if c[j] + k in d:
                count += 1
        return count
    
    def findPairs0(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        k maybe negative
        """
        # import collections
        # unique_nums = set(nums)
        # count = 0
        # new_nums = collections.Counter(nums)
        # if k == 0:
        #     for i in unique_nums:
        #         if new_nums[i] > 1:
        #             count +=1
        #     return count
        # elif k < 0:
        #     return 0
        # elif k > 0:
        #     for i in unique_nums:
        #         if i+k in unique_nums:
        #             count += 1
        #     return count
        
# 用counter来做
        # import collections
        # count = 0
        # list_nums = set(nums)
        # if k == 0:
        #     nums = collections.Counter(nums)
        #     for each in nums:
        #         if nums[each] > 1:
        #             count += 1
        #     return count
        # elif k < 0:
        #     return 0
        # elif k > 0:
        #     for i in list_nums:
        #         if i + k in list_nums:
        #             count += 1
        #     return count
        
# 用dict来做

        count = 0
        if k < 0 :
            return count
        if k == 0:
            new_nums = collections.defaultdict(int)
            for i in nums:
                new_nums[i] +=1
            for value in new_nums:
                if new_nums[value] > 1:
                    count += 1
            return count
        if k > 0 :
            nums = set(nums)
            for i in nums:
                if i+k in nums:
                    count += 1
            return count

#         if k < 0:
#             return 0
#         if k == 0:
#             dict = collections.defaultdict(int)
#             for i in nums:
#                 dict[i] += 1
#             ans = 0
#             for value in dict.values():
#                 if value > 1:
#                     ans += 1
#             return ans
#         nums = set(nums)
#         ans = 0
#         for item in nums:
#             if item+k in nums:
#                 ans += 1
#         return ans
        
        
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        r = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if i == len(nums)-1 and r < count:
                    r = count
            else:
                if count > r:
                    r = count
                count = 0
        return r
    
    def findMaxConsecutiveOnes0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        
        count = 0
        countMax =0
        for ele in nums:
            if ele == 1:
                count += 1
            else:
                if count > countMax:
                    countMax = count
                count = 0
        
        if count > countMax:
            countMax = count
        
        return countMax
    
    
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(set(nums)) < 3:
            return max(nums)
        a = [i for i in (set(nums))]
        t,s,m = tuple(sorted([a[0], a[1], a[2]]))
        for i in range(len(nums)):
            if nums[i] > m:
                t = s
                s = m
                m = nums[i]
            elif m > nums[i] > s:
                t = s
                s = nums[i]
            elif s > nums[i] > t:
                t = nums[i]
        return t
    
    def thirdMax0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(list(set(nums)))
        if len(nums)<3:
            return max(nums)
        else:
            return nums[-3]

    
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        for j in range(count,len(nums)):
            nums[j] = 0
            
    def moveZeroes0(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nonzeroes = [x for x in nums if x != 0]
        if nonzeroes and len(nonzeroes) < len(nums):
            nums[:len(nonzeroes)] = nonzeroes
            nums[len(nonzeroes):] = [0] * (len(nums) - len(nonzeroes))
            
    
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r = []
        for i in range(len(nums)):
            index = abs(nums[i])-1
            nums[index] = -abs(nums[index])
        for j in range(len(nums)):
            if nums[j] > 0:
                r.append(j+1)
        return r
            
    
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        nums.append(l)
        for i in range(len(nums)):
            index = abs(nums[i])
            if index == l+1:
                index = 0
            if nums[index] == 0:
                nums[index] = -l-1
                #print(nums)
            else:
                nums[index] = -abs(nums[index])
                #print(nums)
        for j in range(len(nums)):
            if nums[j] >= 0:
                return j
        return l
    
    def missingNumber0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # if len(nums)==1 and nums[0]==0:
        #     return 1
        return int((1+len(nums))*len(nums)/2-sum(nums))
    
    
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
                return True
            else:
                d[nums[i]] = 1
        return False
    
    def containsDuplicate0(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_set = set(nums)
        if len(nums) == len(num_set):
            return False
        return True
    
    
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        state of art
        """
        if len(nums) == 0:
            return False
        elif len(nums) == len(set(nums)):
            return False
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]] = []
                d[nums[i]].append(i)
        for j in d:
            if len(d[j]) > 1: 
                for m in range(len(d[j])-1):
                    if d[j][m+1] - d[j][m] <= k:
                        return True
        return False
    
    def containsNearbyDuplicate1(self, nums, k):
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False
    
    
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def reverse(n,k,nums):
            l = []
            b = 0
            for i in range(n-k):
                l.append(nums[i])
            for j in range(n-k,n):
                temp = nums[j]
                nums[b] = temp
                b += 1
            for j in range(len(l)):
                temp = l[j]
                nums[b] = temp
                b += 1
                
        n = len(nums)
        if n < k:
            k = k-n
            reverse(n,k,nums)
        else:
            reverse(n,k,nums)
        return nums
            
    def rotate0(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:k], nums[k:] = nums[n-k:], nums[:n-k]    
            
     
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for item in dic:
            if dic[item] > len(nums)/2:
                return item
            
    def majorityElement0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1 :
            return nums[0]
        if n%2 :
            find = set(nums[0:(n//2)+1]) & set(nums[n//2:])
        else:
            find = set(nums[0:n//2]) & set(nums[n//2:])
        
        for i in find:
            if nums.count(i)>n//2:
                return i
            
    
    def twoSumTwo(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = 0
        e = 0
        n = len(numbers)
        for i in range(n):
            if numbers[i] == target/2 and numbers[i+1] == target/2:
                s = i
                e = i+1
                break
            elif numbers[i] <= target/2 and numbers[i+1] > target/2:
                s = i
                e = i+1
        if numbers[s] + numbers[e] == target:
            return [s+1,e+1]
        else:
            for i in range(s+1):
                for j in range(e, n):
                    if numbers[i] + numbers[j] == target:
                        return [i+1,j+1]
                    
    def twoSumTwo1(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = []
        left = 0
        right = len(numbers) - 1
        while numbers[left] + numbers[right] != target and left < right:
            Sum = numbers[left] + numbers[right]
            if Sum > target:
                right = right - 1
            else:
                left = left + 1
        if left < right:
            ret.append(left + 1)
            ret.append(right + 1)
            return ret
        else:
            return []
        
    def twoSumTwo0(self, numbers, target):
      
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        def move_rightest_left(self, start, end, target, numbers):
            left = start
            right = end
            while left <= right:
                mid = int((left + right)/2)
                if numbers[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return right
        
        def move_leftest_right(self, start, end, target, numbers):
            left = start
            right = end
            while left <= right:
                mid = int((left + right) / 2)
                if numbers[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return left
        
        ret = []
        left = 0
        right = len(numbers) - 1
        while left < right:
            Sum = numbers[left] + numbers[right]
            if Sum == target:
                ret.append(left + 1)
                ret.append(right + 1)
                return ret
            if Sum > target:
                right = self.move_rightest_left(left, right, target - numbers[left], numbers)
            else:
                left = self.move_leftest_right(left, right, target - numbers[right], numbers)

        return ret


    def maxProfitⅠ(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        min_price = max(prices)
        profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > profit:     
                profit = prices[i] - min_price
        return profit
    
    def maxProfitⅠ0(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        max_prof = 0
        min_p = sys.maxsize
        
        for i in range(len(prices)):
            if prices[i] < min_p:
                min_p = prices[i]
            elif prices[i] - min_p > max_prof:
                max_prof = prices[i] - min_p
            
        return max_prof
    
    
    def maxProfitⅡ(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        profit = 0
        for i in range(len(prices)-1):
            p = prices[i+1] - prices[i]
            if p >= 0:
                profit += p
        return profit
    
    def maxProfitⅡ0(self, prices):
        profits = 0 
        ln = len(prices)
        if not ln:
            return 0
        elif ln == 2:
            return (prices[1]-prices[0]) if prices[1] > prices[0] else 0
        lastPrice = prices[0]
        for price in prices:
            if lastPrice < price:
                profits+= (price-lastPrice)
            lastPrice = price
        return profits
    
    
    def generateOne(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1],[1,1]]
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return[ [1],
                   [1,1]
                   ]
        for i in range(2,numRows):
            res.append([1])
            for j in range(1,i+1):
                if j < i:
                    res[i].append(res[i-1][j-1] + res[i-1][j])
                else:
                    res[i].append(1)
        return res
    
    def generateOne0(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(1,numRows):
            res.append(list(map(lambda x, y : x + y, res[-1]+[0], [0]+res[-1])))
        return res[:numRows]
    
    
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        nums = []
        n = len(digits)
        for i in range(n):
            num += digits[i] * pow(10,(n-i-1))
        num += 1
        t = len(str(num))
        for j in range(t):
            nums.append(num // pow(10,(t-j-1)))
            num -= nums[j] * pow(10,(t-j-1))
        return nums
    
    def plusOne0(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry=1
        for i in range(len(digits)-1, -1, -1):
            digits[i]+=carry
            if digits[i] > 9:
                digits[i]-=10
                carry=1
            else:
                carry=0    
            if carry == 0:
                break    
        if carry == 1:
            digits.insert(0, 1)
        return digits 
    
    
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        Both state of art , but the 0 one is more concise
        """
        i = 0
        j = 0
        k = 0
        res = nums1[:]
        if m == 0:
            for k in range(n):
                nums1[k] = nums2[k]
        while i < m and j < n:
            if res[i] < nums2[j]:
                nums1[k] = res[i]
                k += 1
                if i == m-1:
                    for a in range(j,n):
                        nums1[k] = nums2[a]
                        k+=1
                    break
                else:
                    i += 1
            else:
                nums1[k] = nums2[j]
                k += 1
                if j == n-1:
                    for a in range(i,m):
                        nums1[k] = res[a]
                        k+=1
                    break
                else:
                    j += 1
                    
    def merge0(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        
        nums1[m:] = nums2[:n]
        nums1.sort()
    
    
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        a = []
        a.append(nums[0])
        for i in range(len(nums)):
            if nums[i] != a[-1]:
                a.append(nums[i])
        for j in range(len(a)):
            nums[j] = a[j]
        return len(a)
    
    def removeDuplicates0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(list(set(nums)))
        return len(nums)
        
        """
        index = 0
        while index < len(nums) - 1:
            if nums[index] == nums[index+1]:
                del nums[index]
            else:
                index += 1
        return len(nums)
        """
        
    
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                count -= 1
                j = i + 1
                while j < len(nums):
                    if nums[j] != val and nums[j] != -val-1:
                        nums[i] = nums[j]
                        nums[j] = -val-1
                        break
                    j += 1
            elif nums[i] == -val-1:
                j = i + 1
                while j < len(nums):
                    if nums[j] != val and nums[j] != -val-1:
                        nums[i] = nums[j]
                        nums[j] = -val-1
                        break
                    j += 1
        nums[:] = nums[:count]
        return count
    
    def removeElement0(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index=0
        
        for i in range(0,len(nums)):
            if nums[i]!=val:
                nums[index]=nums[i]
                index=index+1
        return index
    
    
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        for i in range(len(nums)-1):
            if nums[i] < target < nums[i+1]:
                return i+1
            elif target == nums[i]:
                return i
            elif target == nums[i+1]:
                return i+1
            
    def searchInsert0(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        num=[i for i in nums if i<target]
        return len(num)
    
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        k = []
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                if nums[i] * 2 == target:
                    return [dic[nums[i]],i]
            else:
                dic[nums[i]] = i
            k.append(target - nums[i])
        for j in range(len(k)):
            if k[j] in dic:
                if k[j] != nums[j]:
                    return [j,dic[k[j]]]
    
    def twoSum0(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp = {}
        for i in range(len(nums)):
            if target - nums[i] in tmp:
                return(tmp[target - nums[i]], i)
            else:
                tmp[nums[i]] = i;
        
    
    def getRow1(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        i = 0
        while i < rowIndex:
            row = [x+y for x,y in zip([0]+row, row+[0])]
            i += 1
        return row

    def getRow0(self, k):
        """
        :type k: int
        :rtype: List[int]
        """
        res = [1]
        cur = k
        for i in range(k//2):
            res += res[-1] * cur // (i+1),
            cur -= 1
        if k % 2 == 0:
            res = res + res[:-1][::-1]
        else:
            res = res + res[::-1]
        return res
    
    
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(1,n):
            nums[i] = max(nums[i], nums[i-1]+nums[i])
        return max(nums)
    
    def maxSubArray0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # i = 0
        # i_keep = 0
        # j = 1
        # j_keep = 1
        # max_sum = nums[0]-1
        # while j < len(nums) and i < j:
        #     temp_sum = sum(nums[i:j])
        #     if temp_sum >= max_sum:
        #         i_keep = i
        #         j_keep = j
        #         max_sum = temp_sum
        #     elif i == j-1:
        #         i += 1
        #         j += 1
        #     j += 1
        # return max_sum
        
        # brute force
        # max_sum = nums[0]
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)+1):
        #         temp_sum = sum(nums[i:j])
        #         if temp_sum > max_sum and i != j:
        #             max_sum = temp_sum
        # return max_sum

        # outer loop only
        max_sum = csum = nums[0]
        for num in nums[1:]:
            if num >= csum + num:
                csum = num
            else:
                csum += num
            
            if csum > max_sum:
                max_sum = csum
        
        return max_sum
    
    def maxArrayDC(self, nums):
        
        def crossArray(left, right):
            leftSum = 0
            rightSum = 0
            l = min(left)
            r = min(right)
            for i in range(len(left)-1, -1, -1):
                leftSum += left[i]
                l = max(leftSum, l)
            for i in range(0, len(right)):
                rightSum += right[i]
                r = max(rightSum, r)
            return l+r
        
        n = len(nums)
        if n == 1:
            return nums[0]
        mid = n // 2
        left = nums[:mid]
        right = nums[mid:]
        l_max = self.maxArrayDC(left)
        r_max = self.maxArrayDC(right)
        return max(l_max, r_max, crossArray(left, right))
    
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = [0,1,2]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 0:
            return 0
        for i in range(3,n+1):
            k.append(k[i-1]+k[i-2])
        return k[n]
    
    def climbStairs0(self, n):
        """
        :type n: int
        :rtype: int
        """
        dictionary = {}
        number = 0
        if n == 0 or n == 1:
            return 1
        if n in self.dictionary:
            return dictionary[n]
        else:
            number += self.climbStairs(n - 1) + self.climbStairs(n - 2)
            dictionary[n] = number
        return number
    
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [0]
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            k = max(nums[0], nums[1])
            res.append(k)
            return k
        elif n == 0:
            return 0
        t = 3
        res.append(nums[0])
        k = max(nums[0], nums[1])
        res.append(k)
        while t <= n:
            res.append(max(res[t-1], res[t-2] + nums[t-1]))
            t += 1
        return res[n]
    
    def rob1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        The same solution as mine, but ...
        """
        
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
        return dp[-1]
        
    def rob0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        money = [0,nums[0]]
        for i in range(1,len(nums)):
            temp = money[0]
            money[0] = max(money[0],money[1])
            money[1] = temp + nums[i]
        return max(money[0],money[1])  
    
    def isBadVersion(self, version):
        if version >= 7:
            return True
        else:
            return False
    
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def badVersion(begin, end):
            mid = (begin + end) // 2
            gap = end - begin
            #print(self.isBadVersion(begin),begin, end)
            if gap == 1:
                return end
            if self.isBadVersion(mid):
                return badVersion(begin, mid)
            else:
                return badVersion(mid, end)
        return badVersion(0, n)
    
    def firstBadVersion0(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        checking = (end + start)/2
        while (end != start):
            if self.isBadVersion(checking):
                end = checking
            else:
                start =  checking + 1
            checking = (end+start)/2
        
        return start
        
    
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sdic = {}
        tdic = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in sdic:
                sdic[s[i]] += str(i)
            else:
                sdic[s[i]] = str(i)
            if t[i] in tdic:
                tdic[t[i]] += str(i)
            else:
                tdic[t[i]] = str(i)
        sres = list(sdic.values())
        tres = list(tdic.values())
        sres.sort()
        tres.sort()
        if sres == tres:
            return True
        else:
            return False
        
    def isIsomorphic0(self, s1, s2):
        return len(set(zip(s1, s2))) == len(set(s1)) == len(set(s2))
    
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r = len(matrix)
        if r == 0:
            return False
        c = len(matrix[0])
        if c == 0:
            return False
        
        def binarySearch(l, start, end, target):
            mid = (start + end) // 2
            if mid == start:
                return False
            elif l[mid] < target:
                return binarySearch(l, mid, end, target)
            elif l[mid] > target:
                return binarySearch(l, start, mid, target)
            else:
                return True
        
        for i in range(r):
            if matrix[i][0] < target and matrix[i][-1] > target:
                if binarySearch(matrix[i], 0, c-1, target):
                    return True
            elif matrix[i][0] == target or matrix[i][-1] == target:
                return True
     
        return False
    
    def searchMatrix0(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        row, col = 0, n-1
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
    
    
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == k:
            return min(nums)
        else:
            nums.sort()
            return nums[-k]
        
    def findKthLargest0(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums, reverse=True)
        return nums[k - 1]
    
    
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def helper(a, b , c):
            if c == "+":
                return a + b
            elif c == "-":
                return a - b
            elif c == "*":
                return a * b
            
        res = []    
        if input.isdigit():
            return [int(input)]
        for i in range(len(input)):
            if input[i] in "+-*":
                a = self.diffWaysToCompute(input[:i])
                b = self.diffWaysToCompute(input[i+1:])
                for j in a:
                    for k in b:
                        res.append(helper(j, k, input[i]))
        return res
            
    def diffWaysToCompute0(self, input):
        """
        :type input: str
        :rtype: List[int]
        This problem is more like a DP problem rather than a divide and conquer one
        """
        arr = [int(n) for n in re.split(r'[-+*]', input)]
        ops = re.findall(r'[-+*]', input)
        memo = {}
        def helper(start, end):
            if start == end:
                return [arr[start]]
            if start > end:
                return []
            if (start, end) in memo:
                return memo[(start, end)]
            result = []
            for i in range(start, end):
                solutions_right = helper(i+1, end)
                solutions_left = helper(start, i)
                for l in solutions_left:
                    for r in solutions_right:
                        if ops[i] == '+':
                            result.append(l+r)
                        elif ops[i] == '-':
                            result.append(l-r)
                        else:
                            result.append(l*r)
            memo[(start, end)] = result
            return result
        
        return helper(0, len(arr)-1)
    
    def diffWaysToCompute1(self, input): #48ms
        tokens = re.split('(\D)', input)
        nums = map(int, tokens[::2])
        ops = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])
        def build(lo, hi):
            if lo == hi:
                return [nums[lo]]
            return [ops[i](a, b)
                    for i in range(lo, hi)
                    for a in build(lo, i)
                    for b in build(i + 1, hi)]
        return build(0, len(nums) - 1)
    
    def diffWaysToCompute2(self, input): #168ms
        return [eval('a'+c+'b')
                for i, c in enumerate(input) if c in '+-*'
                for a in self.diffWaysToCompute(input[:i])
                for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]

    def diffWaysToCompute3(self, input): #64ms
        return [a+b if c == '+' else a-b if c == '-' else a*b
            for i, c in enumerate(input) if c in '+-*'
            for a in self.diffWaysToCompute(input[:i])
            for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]
    
    
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


    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        [[]] [] [[],[1,2]] [[1,2],[],[2,3]]
        """
        n = len(lists)
        res = []
        if n == 0:
            return res
        elif lists[0] == None and n == 1:
            return res
        for i in range(n):
            if lists[i] != None:
                res.append(lists[i].val)
                t = lists[i].next
                while t != None:
                    res.append(t.val)
                    t = t.next
        res.sort()
        return res
    
    def mergeKLists0(self, lists):
        from operator import attrgetter
        
        sorted_list = []
        for lst in lists:
            while lst is not None:
                sorted_list.append(lst)
                lst = lst.next
        sorted_list = sorted(sorted_list, key = attrgetter('val'))
        dummy  = curr = ListNode(0)
        for node in sorted_list:
            curr.next = curr = node
        return dummy.next
    
    
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        d = {}
        res = 0
        for i in S:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for j in J:
            if j in d:
                res += d[j]
        return res
    
    def numJewelsInStones0(self, J, S):
        jewelCounter = 0

        for stone in S:
            if stone in J:
                jewelCounter = jewelCounter + 1

        return jewelCounter
    
    
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        res = {}
        t = []
        for i in range(len(cpdomains)):
            nums = int(cpdomains[i].split(' ')[0])
            w = cpdomains[i].split(' ')[1].split('.')
            if w[-1] in res:
                res[w[-1]] += nums
            else:
                res[w[-1]] = nums
            if w[-2] + '.' + w[-1] in res:
                res[w[-2] + '.' + w[-1]] += nums
            else:
                res[w[-2] + '.' + w[-1]] = nums
            if len(w) == 3:
                res[cpdomains[i].split(' ')[1]] = nums
        for i in res:
            t.append(str(res[i]) + ' ' + i)
        return t
    
    def subdomainVisits0(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        if not cpdomains:
            return list()
        
        res = dict()
        def add_to_dict(key, value):
            if key in res:
                res[key] += value
            else:
                res[key] = value
        
        for cp in cpdomains:
            count, domain = cp.split(' ')
            count = int(count)
            add_to_dict(domain, count)
            domain_split = domain.split('.')
            if len(domain_split) == 2:
                _, tl = domain_split
                add_to_dict(tl, count)
            else: 
                _, tld, tl = domain_split          
                add_to_dict(tl, count)
                add_to_dict(tld +'.'+tl, count)
        
        foo = list()
        
        for k, v in res.items():
            foo.append('{} {}'.format(v, k))
            
        return foo
    
    
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        k = []
        for i in words:
            q = True
            t = i.lower()
            l = len(i)
            if t[0] in "qwertyuiop":
                res = 1
            elif t[0] in "asdfghjkl":
                res = 2
            else:
                res = 3
            for j in range(1, l):
                if res == 1:
                    if t[j] not in "qwertyuiop":
                        q = False
                elif res == 2:
                    if t[j] not in "asdfghjkl":
                        q = False
                else:
                    if t[j] not in "zxcvbnm":
                        q = False
            if q:
                k.append(i)
        return k
    
    def findWords0(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1='qwertyuiop'
        row2='asdfghjkl'
        row3='zxcvbnm'
        r=[]
        for i in words:
            if set(i.lower()).issubset(set(row1)):
                r.append(i)
            elif set(i.lower()).issubset(set(row2)):
                r.append(i)
            elif set(i.lower()).issubset(set(row3)):
                r.append(i)
        return r
        

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        t = 0
        res = [[0 for i in range(n+1)]]
        for k in range(m):
            tmp = [0]
            for j in range(n):
                tmp.append(grid[k][j])
            tmp.append(0)
            res.append(tmp)
        res.append([0 for i in range(n+1)])
        for i in range(m+1):
            for j in range(n+1):
                if res[i][j] == 1:
                    count = 0
                    if res[i-1][j] == 0:
                        count += 1
                    if res[i+1][j] == 0:
                        count += 1
                    if res[i][j-1] == 0:
                        count += 1
                    if res[i][j+1] == 0:
                        count += 1
                    t += count
        return t
    
    def islandPerimeter0(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
       
        """
        ret = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    ret += 4
                    if j and grid[i][j - 1]:
                        ret -= 2
                    if i and grid[i - 1][j]:
                        ret -= 2
        return ret
    
    
    def getSkyline_1(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        not accepted due to time limit exceeded
        """
        if len(buildings) == 0 or len(buildings[0]) == 0:
            return []
        s = []
        for i in range(len(buildings)):
            s.append([buildings[i][0], "b", buildings[i][2]])
            s.append([buildings[i][1], "e", buildings[i][2]])
        s.sort()
        h = []
        res = []
        for j in range(len(s)):
            if s[j][1] == "b":
                h.append(s[j][2])
            else:
                h.remove(s[j][2])
            if len(h) != 0:
                res.append([s[j][0], max(h)])
            else:
                res.append([s[j][0], 0])
        tmp = 0
        tt = []
        for k in range(len(res)):
            if tmp != res[k][1]:
                tt.append(res[k])
                tmp = res[k][1]
        tp = tt[0][0]
        l = 1
        while l < len(tt):
            if tt[l][0] == tp:
                del tt[l-1]
            else:
                tp = tt[l][0]
                l += 1
        return tt

    def getSkyline01(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        t = sorted(list([x, -y, z] for x, y, z in buildings) + list([z, 0 ,None] for _, z, _ in buildings))
        t.sort()
        hp = [[0,float("inf")]]
        res = [[] for _ in buildings]
        res[0].append(0)
        res[0].append(0)
        i = 1
        for x, y, z in t:
            while x > hp[0][1]:
                heapq.heappop(hp)
            if y:
                heapq.heappush(hp, [y, z])
            if res[-1][1] + hp[0][0]:
                res[i].append(x)
                res[i].append(-hp[0][0])
                i += 1
        for j in range(len(res)):
            if len(res[j]) == 0:
                z = j
        return res[1:z]
            

    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = 0
        j = 0
        count = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count
    
    def findContentChildren0(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        res = 0
        heapq.heapify(g)
        s.sort()
        for num in s:
            if not g:
                break
            elif g[0] <= num:
                res += 1
                heapq.heappop(g)
        return res
    
    
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        def judgeIf(l, t):
            for k in l:
                if t[k] != 0:
                    return False
            return True
        
        t = {}
        res = [0]
        l = []
        for i in range(len(S)):
            if S[i] in t:
                t[S[i]] += 1
            else:
                t[S[i]] = 1
        j = 0
        while j < len(S):
            if S[j] not in l:
                l.append(S[j])
            t[S[j]] -= 1
            if t[S[j]] != 0:
                j += 1
            else:
                j += 1
                if judgeIf(l, t):
                    l = []
                    res.append(j-sum(res))
        return res[1:]
    
    def partitionLabels0(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lst = {}
        n = len(S)
        for i,c in enumerate(S):
            lst[c] = i;
        ans = []
        max = 0
        pre = -1
        for i in range(n):
            if lst[S[i]] > max :
                max = lst[S[i]]
            if max == i :
                ans.append(max-pre)
                pre = max
                max = max+1
        
        return ans
    
    
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda a: [a[0], -a[1]],reverse=True)
        res = []
        for  j in range(len(people)):
            res.insert(people[j][1], people[j])
        return res
        
        
    def reconstructQueue0(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda x: (-x[0], x[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue
    
    
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        pay attention to the last 0 if it exist then everything changes
        """
        def checkPoint(nums, j):
            k = 1
            while j - k >= 0:
                if j == len(nums)-1:
                    if nums[j-k] >= k:
                        return False
                else:
                    if nums[j-k] > k:
                        return False
                k += 1
            return True
        
        if len(nums) == 1:
            return True
        ex = []
        for i in range(len(nums)):
            if nums[i] == 0:
                ex.append(i)
        zt = 0
        for j in ex:
            if checkPoint(nums, j):
                zt = -1
        if zt == -1:
            return False
        else:
            return True
        
        
    def canJump0(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        
        can = True
        smallest_idx = n - 1
        
        for i in range(n - 2, -1, -1):
            can = i + nums[i] >= smallest_idx
            if can:
                smallest_idx = i
        return can
    
    
    def canCompleteCircuit_1(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        Time Limit Exceeded
        """
        def checkSum(t, i):
            j = 0
            s = 0
            while j< len(t):
                if i+j < len(t):
                    s += t[i+j]
                    if s < 0 :
                        return False
                    j += 1
                else:
                    s += t[i+j-len(t)]
                    if s < 0:
                        return False
                    j += 1
            return True
                    
        t = []
        for k in range(len(gas)):
            tmp = gas[k] - cost[k]
            t.append(tmp)
        for i in range(len(t)):
            if t[i] >= 0:
                if checkSum(t, i):
                    return i
        return -1
    
    def canCompleteCircuit0(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        i = len(gas) - 1
        j = 0
        s = 0
        s += (gas[i] - cost[i])
        while i > j:
            if s <= 0:
                i -= 1
                s += (gas[i] - cost[i])
            else:
                s += (gas[j] - cost[j])
                j += 1
        if s >= 0:
            return i
        else:
            return -1
            
    
    def wiggleMaxLength_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        i = 1
        prediff = nums[1] - nums[0]
        if prediff == 0:
            count = 1
        else:
            count = 2
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i-1]
            if prediff >= 0 and diff < 0:
                count += 1
                prediff = diff
            elif prediff <= 0 and diff > 0:
                count += 1
                prediff = diff
        return count
    
    def wiggleMaxLength(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(arr)
        if n < 2:
            return n
        wsl = [0]*n
        wsl[0] = 1
        for cur in range(1, n):
            prev = cur - 1                
            if arr[cur] > arr[prev] and wsl[prev] <= 1:
                wsl[cur] = abs(wsl[prev]) + 1
            elif arr[cur] < arr[prev] and wsl[prev] > 0:
                wsl[cur] = (abs(wsl[prev]) + 1)*(-1)
            else:
                wsl[cur] = wsl[prev]
        return abs(wsl[n-1])
    
    
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j = 0
        for i in range(len(s)):
            j = t.find(s[i])
            if j == -1:
                return False
            else:
                t = t[j+1:]
        return True
    
    def isSubsequence0(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False
        for i in s:
            if i in t:
                index = t.find(i)
                t = t[index + 1:]
            else:
                return False
        return True
    
    
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n = len(num)
        l = list(num)
        if n == k:
            return "0"
        tmp = min(l[:k+1])
        res= [tmp]
        j = l.index(tmp)
        for i in range(2, n-k+1):
            t = l[j+1:k+i]
            tmp = min(t)
            j = j + t.index(tmp) + 1
            res.append(tmp)
        return str(int(''.join(res)))
    
    def removeKdigits0(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        out=[]
        for digit in num:
            while k and out and out[-1] > digit:
                out.pop()
                k-=1
            out.append(digit)
        return ''.join(out[:-k or None]).lstrip('0') or "0"
    
    
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) <= 1:
            return 0
        s = []
        e = []
        r = [[] for i in intervals]
        for i in intervals:
            s.append(i.start)
            e.append(i.end)
        for i in range(len(s)):
            r[i].append(e[i])
            r[i].append(s[i])
        r.sort()
        res = 1
        last = r[0]
        for j in range(1, len(r)):
            if last[0] <= r[j][1]:
                res += 1
                last = r[j]
        return len(intervals) - res
    
    def eraseOverlapIntervals0(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals = sorted(intervals, key = lambda x: x.end)
        current_end = float('-inf')
        cnt = 0
        for interval in intervals:
            if interval.start >= current_end:
                cnt += 1
                current_end = interval.end
        return len(intervals) - cnt
    
    
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        points.sort(key=lambda a:a[1])
        pre = points[0]
        i = 1
        count = 1
        while i < len(points):
            if points[i][0] <= pre[1] and points[i][1] >= pre[1]:
                i += 1
            else:
                count += 1
                pre = points[i]
                i += 1
        return count
    
    def findMinArrowShots0(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        tempend = float('-inf')
        res = 0
        for i in sorted(points, key=lambda i: i[1]):
            if i[0] > tempend:
                tempend = i[1]
                res += 1
        
        return res
    
    
    def leastInterval_1(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dic = {}
        for i in tasks:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        l = list(dic.values())
        l.sort(reverse=True)
        t = len(l)
        count = 0
        while l[0] > 0:
            i = 0
            while i <= n:
                if l[0] == 0:
                    break
                elif i < t and l[i] > 0:
                    l[i] -= 1
                i += 1
                count += 1
            l.sort(reverse=True)
        return count
    
    def leastInterval0(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_count =collections.Counter(tasks).values()
        M = max(task_count)
        mct = list(task_count).count(M)
        return max(len(tasks),(M-1)*(n+1)+mct)
        
    
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        R = 0
        D = 0
        Rr = 0
        Dr = 0
        j = 0
        s = []
        for i in range(len(senate)):
            s.append(senate[i])
            if senate[i] == "R":
                R += 1
            else:
                D += 1
        while R > 0 and D > 0:
            if s[j] == "R":
                if Rr != 0:
                    Rr -= 1
                else:
                    D -= 1
                    Dr += 1
                    s.append("R")
            else:
                if Dr != 0:
                    Dr -= 1
                else:
                    R -= 1
                    Rr += 1 
                    s.append("D")
            j += 1
        if R == 0:
            return "Dire"
        else:
            return "Radiant"
        
    def predictPartyVictory0(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        num = 0  # num of Reeding R
        while ('R' in senate and 'D' in senate):
            res = []
            for i in senate:
                if i=='R':
                    if num>=0:
                        res.append(i)
                    num+=1
                else:
                    if num<=0:
                        res.append(i)
                    num-=1
            senate = res
        return 'Radiant' if 'R' in senate else 'Dire'
    
    
    def isSymmetric_1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = queue.Queue()
        q.put(root)
        q.put(root)
        while not q.empty():
            t1 = q.get()
            t2 = q.get()
            if t1 == None and t2 == None:
                continue
            if t1 == None or t2 == None:
                return False
            if t1.val != t2.val:
                return False
            q.put(t1.left)
            q.put(t2.right)
            q.put(t1.right)
            q.put(t2.left)
        return True
    
    def isSymmetric0(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return self.isSymmetricHelper(root.left, root.right)

    def isSymmetricHelper(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        
        elif root1 != None and root2 != None:
            if root1.val != root2.val:
                return False
            
            
    def levelOrder_1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, kk = [], [root]
        while root and kk:
            tmp = []
            res.append([i.val for i in kk if i])
            for j in kk:
                if j:
                    tmp.extend([j.left, j.right])
            kk = [i for i in tmp if i]
        return res
    
    def levelOrder0(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d = deque([(root, 0)])
        res = []

        tmp = []
        pre_depth = 0
        while d:
            node, depth = d.popleft()
            if node:
                if depth == pre_depth:
                    tmp.append(node.val)
                else:
                    pre_depth = depth
                    res.append(tmp)
                    tmp = [node.val]
                if node.left:
                    d.append((node.left, depth+1))
                if node.right:
                    d.append((node.right, depth+1))

        if tmp:
            res.append(tmp)
        return res
    
    
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level = 1
        res, kk = [], [root]
        while root and kk:
            tmp = []
            if level % 2 == 1:
                res.append([i.val for i in kk if i])
                kk.reverse()
                for j in kk:
                    if j:
                        tmp.append(j.right)
                        tmp.append(j.left)
            else:
                res.append([i.val for i in kk if i])
                kk.reverse()
                for j in kk:
                    if j:
                        tmp.append(j.left)
                        tmp.append(j.right)
            level += 1
            kk = [k for k in tmp if k]
        return res
    
    def zigzagLevelOrder0(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        the run time is the same as the solution above
        """
        if not root:
            return []
        queue = [root]
        direct = True
        layer = []
        res = []
        ans = []
        while queue!=[]:
            a = queue.pop(0)
            if direct:
                if a.left:
                    layer.append(a.left)
                if a.right:
                    layer.append(a.right)
                ans.append(a.val)
            else:
                if a.left:
                    layer.append(a.left)
                if a.right:
                    layer.append(a.right)
                ans.insert(0, a.val)
            if queue == []:
                
                if ans != []:
                    res.append(ans)
                ans = []
                queue = list(layer)
                layer = []
                direct = not direct
         
        
        return res
    
    
    def addTwoNumbers_1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = tmp = ListNode(0)
        n1 = l1
        n2 = l2
        q = 0
        while n1 or n2 or q:
            if n1:
                r1 = n1.val
                n1 = n1.next
            else:
                r1 = 0
            if n2:
                r2 = n2.val
                n2 = n2.next
            else:
                r2 = 0
            t1 = r1 + r2 + q
            t = t1 % 10
            q = t1 // 10
            tmp.next = ListNode(t)
            tmp = tmp.next
        return res.next
    
    def addTwoNumbers0(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = 0
        ret = ListNode(0)
        cur = ret
        while l1 and l2:
            cur.next = ListNode((l1.val + l2.val + c) % 10)
            cur = cur.next
            c = (l1.val + l2.val + c)  // 10
            l1 = l1.next
            l2 = l2.next
        while l1:
            cur.next = ListNode((l1.val + c) % 10)
            cur = cur.next
            c = (l1.val + c)  // 10
            l1 = l1.next
        while l2:
            cur.next = ListNode((l2.val + c) % 10)
            cur = cur.next
            c = (l2.val + c)  // 10
            l2 = l2.next
        if c:
            cur.next = ListNode(c)
            cur = cur.next
        return ret.next
    
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def subString(t):
            tmp = {}
            for i in range(len(t)):
                if t[i] in tmp:
                    return len(tmp)
                tmp[t[i]] = 1
            return len(tmp)
                
        res = 0
        for i in range(len(s)):
            t = subString(s[i:]) 
            if t > res:
                res = t
        return res
    
    def lengthOfLongestSubstring0(self, s):
        chars = {}
        max_len = 0
        start = 0
        
        for i, c in enumerate(s, 1):
            if c in chars and chars[c] > start:
                start = chars[c]# + 1
            elif i - start > max_len:
                max_len = i - start              
            chars[c] = i
        return max_len
    
    
    def longestPalindrome_1(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isPalindrome(t, start, end):
            while end < len(t) and start >= 0 and t[start] == t[end]:
                start -= 1
                end += 1
            return end - start - 1
            
        c = -1
        start = 0
        end = 1
        for i in range(len(s)):
            l1 = isPalindrome(s, i, i)
            l2 = isPalindrome(s, i, i+1)
            l = max(l1, l2)
            if l > c:
                c = l
                start = i-((l-1)//2)
                end = i+1+(l//2)
        return s[start:end]
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # res = ""
        # for i in range(len(s)):
        #     temp = ""
        #     for letter in s[i:]:
        #         temp += letter
        #         if temp == temp[::-1] and len(res) < len(temp):
        #             res = temp
        # return res
        
        size = len(s)
        if size <= 1 or s[::-1] == s:
            return s
        start, maxlen = 0, 1
        for idx in range(1, size):
            temp1 = idx - maxlen - 1
            sub2 = s[temp1 : idx + 1]
            if temp1 >= 0 and sub2[::-1] == sub2:
                start = temp1
                maxlen += 2
                continue
            temp2 = idx - maxlen
            sub1 = s[temp2 : idx + 1]
            if temp2 >= 0 and sub1[::-1] == sub1:
                start = temp2
                maxlen += 1
        return s[start : start + maxlen]
    
    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            neg = 1
            x = -x
        else:
            neg = 0
        s = str(x)
        l = [s[i] for i  in range(len(s))]
        l.reverse()
        res = int("".join(l))
        if neg:
            if res > pow(2, 31):
                return 0
            return -res
        else:
            if res > pow(2, 31)-1:
                return 0
            return res
        
    def reverse0(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            reverse_x = int(str(x)[::-1])
        else:
            reverse_x = -int(str(x)[::-1][:-1])
        
        if -2**31 < reverse_x < 2**31 - 1:
            return reverse_x
        else:
            return 0
        
    
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < len(s):
            res = [s[i] for i in range(numRows)]
        else:
            return s
        if numRows == 1:
            return s
        for i in range(numRows, len(s)):
            c = 2*(numRows - 1)
            t = i % c
            if t in range(numRows):
                res[t] += s[i]
            else:
                res[c-t] += s[i]
        return "".join(res)

    def convert0(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        temp = ['' for i in range(numRows)]
        index = -1
        step = 1
        for i in range(len(s)):
            index += step
            if index == numRows:
                index -= 2
                step = -1
            if index == -1:
                index = 1
                step = 1
            temp[index] += s[i]
        return "".join(temp)
            
    
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        Tpoint = 0 
        plus = 0
        tmp = []
        INT_MAX = pow(2,31) - 1
        INT_MIN = -pow(2,31)
        end = 0
        if len(str) == 0:
            return 0
        for i in range(len(str)):
            if str[i] == "+" and plus == 0 and Tpoint == 0:
                plus = 1
                Tpoint = 1
            elif str[i] == "-" and plus == 0 and Tpoint == 0:
                plus = -1
                Tpoint = 1
            elif str[i] == " " and Tpoint == 0:
                continue
            elif str[i].isdigit() and end == 0:
                Tpoint = 1
                tmp.append(str[i])
            else:
                end = 1
                if Tpoint ==0 and str[i] != "+" and str[i] != "-":
                    return 0
        if len(tmp) == 0:
            return 0
        num = int("".join(tmp))
        if plus == 0 or plus == 1:
            if num > INT_MAX:
                return INT_MAX
            else:
                return num
        elif plus == -1:
            if num > -INT_MIN:
                return INT_MIN
            else:
                return -num
            
    def myAtoi0(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        digits = set(string.digits)
        letters = set(string.ascii_letters)
        wspace = set(string.whitespace)

        try:
            num = ''
            for char in str:
                if char in '-+':
                    if not num:
                        num += char
                    else:
                        break
                elif char in digits:
                    num += char
                elif not num and char in wspace:
                    continue
                else:
                    break
            res = int(num)
            if res > INT_MAX:
                return INT_MAX
            elif res < INT_MIN:
                return INT_MIN
            return res
        except:
            return 0
        
    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        l = [s[i] for i in range(len(s))]
        l.reverse()
        t = "".join(l)
        if s == t:
            return True
        else:
            return False
        
    def isPalindrome0(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
    
    
    def isMatch_1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        firstmatch = bool(s) and p[0] in [s[0], '.']
        if len(p) >= 2 and p[1] == "*":
            return self.isMatch(s, p[2:]) or (firstmatch and self.isMatch(s[1:], p))
        else: 
            return firstmatch and self.isMatch(s[1:], p[1:])
        
    def isMatch0(self, s, p):
        dp = {}
        dp[(-1,-1)] = True;
        return self.dP(dp,s,p,len(s) - 1,len(p) - 1)
    
    def dP(self,dp,s,p,index1,index2):
        if (index1,index2) in dp:
            return dp[(index1,index2)];
        
        if index1 == -1 and index2 != -1 and p[index2] == '*':
            dp[(index1,index2-2)] = self.dP(dp,s,p,index1,index2-2);
            return dp[(index1,index2-2)];
        
        if index1 < 0 or index2 < 0:
            return False;
        if p[index2] == '.':
            dp[(index1,index2)] = self.dP(dp,s,p,index1-1,index2-1);
            return dp[(index1,index2)];
        if p[index2] == '*':
            if s[index1] == p[index2 - 1] or p[index2 - 1] == '.':
                dp[(index1,index2)] = (self.dP(dp,s,p,index1 - 1, index2) or self.dP(dp,s,p,index1,index2-2));
                return dp[(index1,index2)]
            else:
                dp[(index1,index2)] = self.dP(dp,s,p,index1,index2-2);
                return dp[(index1,index2)]
        if s[index1] != p[index2]:
            dp[(index1,index2)] = False;
            return False;
        else:
            dp[(index1,index2)] = self.dP(dp,s,p,index1-1,index2-1);
            return dp[(index1,index2)] 
    
    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        res = 0
        while i < j:
            tmp = min(height[j], height[i]) * (j-i)
            if tmp > res:
                res = tmp
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res
    
    def maxArea0(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j,max_v=0,len(height)-1,0
        while i<j:
            if height[i]<height[j]:
                short_p=height[i]
                v=short_p*(j-i)
                i+=1
                while i<j and height[i]<=short_p:
                    i+=1
            else:
                short_p=height[j]
                v=short_p*(j-i)
                j-=1
                while i<j and height[j]<=short_p:
                    j-=1
            if v>max_v:
                max_v=v
        return max_v
    
    
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        tmp = []
        if num // 1000 :
            m = num // 1000
            num -= m*1000
            for i in range(m):
                tmp.append("M")
        if num // 900:
            num -= 900
            tmp.append("CM")
        elif num // 500:
            num -= 500
            tmp.append("D")
            if num // 100:
                c = num // 100
                num -= c*100
                for i in range(c):
                    tmp.append("C")
        elif num // 400:
            num -= 400
            tmp.append("CD")
            if num // 100:
                c = num // 100
                num -= c*100
                for i in range(c):
                    tmp.append("C")
        else:
            c = num // 100
            num -= c*100
            for i in range(c):
                tmp.append("C")
        if num // 90:
            num -= 90
            tmp.append("XC")
        elif num // 50:
            num -= 50
            tmp.append("L")
            if num // 10:
                x = num // 10
                num -= x*10
                for i in range(x):
                    tmp.append("X")
        elif num // 40:
            num -= 40
            tmp.append("XL")
            if num // 10:
                x = num // 10
                num -= x*10
                for i in range(x):
                    tmp.append("X")
        else:
            x = num // 10
            num -= x*10
            for i in range(x):
                tmp.append("X")
        if num // 9:
            num -= 9
            tmp.append("IX")
        elif num // 5:
            num -= 5
            tmp.append("V")
            if num // 1:
                i = num // 1
                num -= i*1
                for i in range(i):
                    tmp.append("I")
        elif num // 4:
            num -= 4
            tmp.append("IV")
            if num // 1:
                i = num // 1
                num -= i*1
                for i in range(i):
                    tmp.append("I")
        else:
            i = num // 1
            num -= i*1
            for i in range(i):
                tmp.append("I")
        return "".join(tmp)
    
    def intToRoman0(self, num):
        """
        :type num: int
        :rtype: str
        """
        romanList = ["","I","II","III","IV","V","VI","VII","VIII","IX"
                     ,"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"
                     ,"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"
                     ,"","M","MM","MMM"]
        romanNumString = ""
        position = 0
        while num:
            romanNumString = romanList[(num % 10) + (position * 10)] + romanNumString
            num = num // 10
            position += 1
        return romanNumString
    
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I": 0, "V": 0, "X": 0, "L": 0, "C": 0, "D": 0, "M": 0}
        res = 0
        for i in range(len(s)):
            d[s[i]] += 1
        i = 0
        while i < len(s):
            if s[i] == "M":
                res += 1000
                d["M"] -= 1
                i += 1
            elif s[i] == "C":
                if d["M"] == 0 and d["D"] == 0:
                    res += 100
                    i += 1
                else:
                    if d["M"] != 0:
                        res += 900
                        d["M"] -= 1
                    elif d["D"] != 0:
                        d["D"] -= 1
                        res += 400
                    i += 2
                d["C"] -= 1
            elif s[i] == "X":
                if d["C"] == 0 and d["L"] == 0:
                    res += 10
                    i += 1
                else:
                    if d["C"] != 0:
                        res += 90
                        d["C"] -= 1
                    elif d["L"] != 0:
                        res += 40
                        d["L"] -= 1
                    i += 2
                d["X"] -= 1
            elif s[i] == "I":
                if d["V"] == 0 and d["X"] == 0:
                    res += 1
                    i += 1
                else:
                    if d["V"] != 0:
                        res += 4
                        d["V"] -= 1
                    elif d["X"] != 0:
                        res += 9
                        d["X"] -= 1
                    i += 2
                d["I"] -= 1
            elif s[i] == "D":
                res += 500
                d["D"] -= 1
                i += 1
            elif s[i] == "L":
                res += 50
                d["L"] -= 1
                i += 1
            elif s[i] == "V":
                res += 5
                d["V"] -= 1
                i += 1
        return res
    
    roman_to_int_mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    def romanToInt0(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        result = 0
        pre_val = float('inf')
        for c in s:
            val = Solution.roman_to_int_mapping[c]
            if val > pre_val:
                result -= 2 * pre_val
            pre_val = val
            result += val
        return result
    
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        tmp = [strs[0][i] for i in range(len(strs[0]))]
        res = []
        j = 0
        while j < len(tmp):
            for i in strs:
                if j >= len(i) or i[j] != tmp[j]:
                    return "".join(res)
            res.append(tmp[j])
            j += 1
        return strs[0]
    
    def longestCommonPrefix0(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        ["flower","flow","flight"] 
        """
        if not strs:
            return ""
        for i,ch in enumerate(zip(*strs)):
            if len(set(ch)) != 1:
                return strs[0][:i]
        else:
            return min(strs,key = len)
    
    
    def threeSum_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
    
    def threeSum0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from bisect import bisect_left, bisect_right
        m = {}
        result = []
        positive_keys = []
        negative_keys = []
        for n in nums:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1

        if 0 in m and m[0] >= 3:
            result.append([0, 0, 0])

        keys = list(m.keys())
        keys.sort()
        print(keys)
        keys_num = len(keys)

        if keys_num == 0:
            return []

        # a<b<c。a一定小于0，c一定大于0
        end = bisect_left(keys, 0)  # a < 0
        begin = bisect_left(keys, -keys[-1] * 2)  # when b == c, a + b + c = a + 2c <= a + 2*max_c;
        #        print('a in [{}:{}]'.format(begin, end))
        for i in range(begin, end):
            a = keys[i]

            # b == c
            if a != 0 and m[a] >= 2 and -2 * a in m:
                result.append([a, a, -2 * a])

            # b的取值范围
            # -a - b = c <= keys[-1] >>>> b >= -keys[-1] - a
            min_b = -keys[-1] - a
            # b<c >>>> a + 2b < a + b + c = 0 >>>> b < -a/2
            max_b = -a / 2

            b_begin = max(i + 1, bisect_left(keys, min_b))  # b的最小值
            b_end = bisect_right(keys, max_b)  # b的最大值
            #            print('a = {}, {} <= b < {}, in [{}:{}]'.format(a, min_b, max_b, b_begin, b_end))
            for j in range(b_begin, b_end):
                b = keys[j]
                #                print('key[{}] = {}, key[{}] = {}'.format(i, a, j, b))
                c = -a - b
                if c in m:
                    if b > c:
                        continue
                    if b < c or m[b] >= 2:
                        #                        print('========', [a, b, c])
                        result.append([a, b, c])

        #        Solution.case_length.append(len(nums))
        #        Solution.case_index +=1
        #        if Solution.case_index == 1:
        #            print(Solution.case_length)
        #            raise Exception(1)
        return result
    
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        tmp = []
        digits_to_letters_mapping = {
            "2": ['a','b','c'],
            "3": ['d','e','f'],
            "4": ['g','h','i'],
            "5": ['j','k','l'],
            "6": ['m','n','o'],
            "7": ['p','q','r','s'],
            "8": ['t','u','v'],
            "9": ['w','x','y','z']
        }
        for i in range(len(digits)):
            if res:
                for j in res:
                    for k in digits_to_letters_mapping[digits[i]]:
                        tmp.append(j+k)
                res = [l for l in tmp]
                tmp = []
            else:
                res =[l for l in digits_to_letters_mapping[digits[i]]]
        return res
    
    def letterCombinations0(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        MAPPING = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        def helper(digits, dex):
            if dex >= len(digits):
                return ['']
            combos = helper(digits, dex + 1)
            possibles = MAPPING[digits[dex]]
            ans = []
            for combo in combos:
                for possible in possibles:
                    ans.append(possible + combo)
            return ans
        
        
        if len(digits) == 0: return []
        return helper(digits, 0)
    
    
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        distance = float("inf")
        n = len(nums)
        nums.sort()
        for i in range(0, n-2):
            l = i + 1
            r = n - 1
            if i-1 >= 0:
                if nums[i] == nums[i-1]:
                    continue
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                d = abs(s - target)
                if s == target:
                    print (s)
                    return target
                elif d < distance:
                    res = s
                    distance = d
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
        return res
    
    def threeSumClosest0(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 3:
            return sum(nums)
        
        nums = sorted(nums)
        
        if nums[0] + nums[1] + nums[2] > target:
            return nums[0] + nums[1] + nums[2]
        if nums[-1] + nums[-2] + nums[-3] < target:
            return nums[-1] + nums[-2] + nums[-3]
        
        best = float('inf')
        max_index = len(nums) - 2
        result = []
        
        for i in range(len(nums) - 2):
            s, e = i + 1, len(nums) - 1
            if nums[i] + nums[e] + nums[e-1] < target:
                result.append(nums[i] + nums[e] + nums[e-1])
                continue
            if nums[i] + nums[s] + nums[s+1] > target:
                result.append(nums[i] + nums[s] + nums[s+1])
            else:
                while s < e and s <= max_index:
                    r = nums[i] + nums[s] + nums[e]
                    result.append(r)

                    if r > target:
                        e -= 1
                    elif r < target:
                        s += 1
                    else:
                        return target
                
            max_index = s
            
        result = sorted(result, key=lambda x: abs(x - target))
                    
        return result[0]
    
    
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        i = 0
        n = len(nums)
        res = []
        if n < 4:
            return res
        
        nums.sort()
        while i < n-3:
            for j in range(i+1, n-2):
                l = j + 1
                r = n - 1
                while l < r:
                    t = nums[i] + nums[j] + nums[l] + nums[r]
                    if t < target:
                        l += 1
                    elif t > target:
                        r -= 1
                    else:
                        if [nums[i], nums[j], nums[l], nums[r]] not in res:
                                res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
            i += 1
        return res
    
    
    def fourSum0(self, nums, target):
        
        def findNSum(nums, begin, target, N, midret, ret):
            if len(nums) - begin < N or N < 2:
                return

            if N == 2:
                lo = begin
                hi = len(nums) - 1
                while lo < hi:
                    tmp = nums[lo] + nums[hi]
                    if tmp > target:
                        hi -= 1
                    elif tmp < target:
                        lo += 1
                    else:
                        ret.append(midret + [nums[lo], nums[hi]])
                        while lo < hi and nums[hi] == nums[hi - 1]:
                            hi -= 1
                        while lo < hi and nums[lo] == nums[lo + 1]:
                            lo += 1
                        hi -= 1
                        lo += 1
            else:
                for i in range(begin, len(nums) - (N - 1)):
                    if i > begin and nums[i] == nums[i - 1]:
                        continue
                    if nums[i]*N > target or nums[-1]*N < target:
                        break
            # if nums[i] + nums[i + 1] * (N - 1) > target or nums[i] + nums[-1] * (N - 1) < target:
            #     continue
                    findNSum(nums, i + 1, target - nums[i], N - 1, midret + [nums[i]], ret)

        
        nums.sort()
        ret = []
        findNSum(nums, 0, target, 4, [], ret)
        return ret
    
    
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tmp = [head]
        t = head.next
        if not t:
            return []
        while t:
            tmp.append(t)
            t = t.next
        if tmp[-n] == tmp[0]:
            return tmp[1]
        else:
            if tmp[-n].next == None:
                tmp[-n-1].next = None
            else:
                tmp[-n-1].next = tmp[-n+1]
        return head
    
    def removeNthFromEnd0(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Time: O(n)
        # Space: O(1)
        dummy = ListNode(0)
        dummy.next = head
        walker = dummy
        runner = dummy
        # dummy = prev = ListNode(0) 
        # prev.next = head
        
        for i in range(n):
            runner = runner.next
            
        while runner and runner.next:
            runner = runner.next
            walker = walker.next
        
        # if not walker.next:
        #     return head.next
        # else:
        walker.next = walker.next.next
        
        return dummy.next
            
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        tmp = []
        mapping = {
            "(": 1,
            ")": -1,
            "[": 2,
            "]": -2,
            "{": 3,
            "}": -3
        }
        for i in range(len(s)):
            if mapping[s[i]] > 0 :
                tmp.append(mapping[s[i]])
            else:
                try:
                    k = tmp.pop()
                except:
                    return False
                if k != -mapping[s[i]]:
                    return False
        if tmp:
            return False
        else:
            return True
        
    def isValid0(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=[None]
        compare={")":"(","]":"[","}":"{"}
        for i in s:
            if(i in compare):
                if(st.pop()!=compare[i]):
                    return(False)
            else:
                st.append(i)
        print(st)
        return(len(st)==1)
    
    
    