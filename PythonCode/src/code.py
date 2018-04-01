import heapq
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
    
    def dominantIndex(self, nums): #只有一个元素的列表     按顺序依次递增的列表     递减的列表      含0的列表    初始值设置是否正确
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
    
    