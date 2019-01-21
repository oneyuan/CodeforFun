class Solution:
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