class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m > 0:
            n = len(grid[0])
        else:
            return 0
        cost = [[0 for _ in range(n)] for _ in range(m)]
        cost[0][0] = grid[0][0]
        for j in range(1, n):
            cost[0][j] = grid[0][j] = grid[0][j] + cost[0][j-1]
        for i in range(1, m):
            cost[i][0] = grid[i][0] + cost[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                cost[i][j] = min(cost[i-1][j], cost[i][j-1]) + grid[i][j]
        return cost[-1][-1]
    
    def minPathSum0(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[-1])
        pre_row = [float('inf')]*n
        pre_row[-1] = 0
        for i_row in reversed(range(m)):
            pre_row[-1] += grid[i_row][-1]
            for i_col in reversed(range(n-1)):
                pre_row[i_col] = min(pre_row[i_col], pre_row[i_col+1]) + grid[i_row][i_col]
        return pre_row[0]