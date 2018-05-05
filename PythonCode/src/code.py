#-*- coding: utf-8 -*-
import heapq
import math
import copy
from builtins import int
#from pstats import count_calls
import collections
import sys

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
    