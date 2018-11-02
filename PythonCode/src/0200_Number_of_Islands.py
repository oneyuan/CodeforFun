class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m:
            n = len(grid[0])
        else:
            return 0
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return 
            grid[i][j] = "0"
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
    
    def numIslands0(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        # bitmap representation of previous row that is updated
        # as update_loop runs left to right
        cols = len(grid[0])
        bitmap = [0 for _ in range(cols)]
        groups = [0]
        ngroup = 1
        for row in grid:
            for i in range(cols):  # update_loop
                if row[i] == "0":
                    bitmap[i] = 0
                    continue
                up = groups[bitmap[i]]  # gets bitmap of element directly above
                # gets bitmap of left, updated previous iteration
                left = groups[0 if i == 0 else bitmap[i-1]]
                if up == 0 and left == 0:  # found new group
                    # bitmap to reflect a new group has been found
                    bitmap[i] = ngroup
                    groups.append(ngroup)  # update group counter
                    ngroup += 1
                elif up == 0:
                    bitmap[i] = left  # no group up, but group exists
                elif left == 0:  # no group left, but group exists up
                    bitmap[i] = up
                # adjusts the value of the group to reflect that membership in a smaller group has been found
                elif left > up:
                    bitmap[i] = groups[left] = up
                else:
                    bitmap[i] = groups[up] = left
        count = 0
        for i in range(1, len(groups)):
            count += (i == groups[i])
        return count
