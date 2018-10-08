class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m > 0:
            n = len(matrix[0])
        else:
            return 0
        height = [0 for _ in range(n)]
        left = [0 for _ in range(n)]
        right = [n for _ in range(n)]
        res = 0
        for i in range(m):
            cur_l = 0
            cur_r = n
            for j in range(n):
                if matrix[i][j] == "1":
                        height[j] += 1
                else:
                    height[j] = 0
            for j in range(n):
                if matrix[i][j] == "1":
                    left[j] = max(left[j], cur_l)
                else:
                    left[j] = 0
                    cur_l = j+1
            for j in range(n-1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], cur_r)
                else:
                    right[j] = n
                    cur_r = j
            for j in range(n):
                res = max(res, (right[j] - left[j])*height[j])
        return res
    
    def maximalRectangle0(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        height = [0 for _ in matrix[0]]
        height.append(0)
        max_area = 0
        for row in matrix:
            row.append("0")
            height = [height[i] + 1 if row[i] == "1" else 0 for i in range(0, len(row))]
            height_stack = []
            for x in range(0, len(height)):
                prev_x = x
                while height_stack and height[x] < height_stack[-1][0]:
                    (prev_h, prev_x) = height_stack.pop()
                    cur_area = prev_h * (x - prev_x)
                    if max_area < cur_area:
                        max_area = cur_area
                if height[x] != 0:
                    height_stack.append((height[x], prev_x))
            
        return max_area
    
    def maximalRectangle1(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans