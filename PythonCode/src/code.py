
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