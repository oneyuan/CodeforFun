class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        heights.append(0)
        index = []
        res = 0
        for i in range(len(heights)):
            while index and heights[i] < heights[index[-1]]:
                h = heights[index[-1]]
                index.pop()
                if index:
                    wid = i - index[-1] - 1
                else:
                    wid = i
                tmp = wid * h
                if tmp > res:
                    res = tmp
            index.append(i)
        return res
    
    def largestRectangleArea0(self, heights):
        """
        Input: List[int]
        Output: int
        
        Examples:
        Input: [2,1,5,6,2,3]
        Output: 10
        
        Question:
        Empty list? 0
        
        Algorithm:
        Recursion? Nope, removing element wont help, divide and conquer wont help
        Sort? This will mess up the order
        
        1) Two pointers O(n^2)
        Each bar has the width of 1. We can scan left and scan right,
        area = height[i] initially
        Scan left: if number is less than heights[i], area += heights[i]
        Scan right: if number if less than heights[i], area += heights[i]
        
        2) Two stacks
        
        Best example: [4, 5, 6, 3] i at 3
        First stack: Position
        Second stack: Height
        
        Each iteration, the stack will have an increasing sequence
        - if cur_height > top of stack
            - Append cur_height and position to stack
        - if cur_height < top of stack:
            - pop from the height stack until cur_height > top of stack
                - check max = max(res, (i - position) * height)
            append top position + 1 as position, and height as height
            
        pop until stack is empty using same formula
        """
        index = []
        inc_heights = []
        n = len(heights)
        res = 0
        for i in range(len(heights)):
            height = heights[i]
            if not inc_heights and not index:
                index.append(i)
                inc_heights.append(height)  
                continue
            if inc_heights[-1] < height:
                inc_heights.append(height)
                index.append(i)
            elif inc_heights[-1] > height:
                prev_index = 0
                while inc_heights and inc_heights[-1] > height:
                    prev_height = inc_heights.pop()
                    j = index.pop()
                    res = max(res, (i - j) * prev_height)
                    prev_index = j
                if not inc_heights:
                    index.append(0)
                    inc_heights.append(height)
                else:
                    index.append(prev_index)
                    inc_heights.append(height)
            
        while inc_heights:
            prev_height = inc_heights.pop()
            prev_index = index.pop()
            res = max(res, (n - prev_index) * prev_height)
        return res