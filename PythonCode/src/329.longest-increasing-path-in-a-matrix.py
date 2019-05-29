#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (39.99%)
# Likes:    963
# Dislikes: 18
# Total Accepted:    87K
# Total Submissions: 217.5K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an integer matrix, find the length of the longest increasing path.
# 
# From each cell, you can either move to four directions: left, right, up or
# down. You may NOT move diagonally or move outside of the boundary (i.e.
# wrap-around is not allowed).
# 
# Example 1:
# 
# 
# Input: nums = 
# [
# ⁠ [9,9,4],
# ⁠ [6,6,8],
# ⁠ [2,1,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [1, 2, 6, 9].
# 
# 
# Example 2:
# 
# 
# Input: nums = 
# [
# ⁠ [3,4,5],
# ⁠ [3,2,6],
# ⁠ [2,2,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally
# is not allowed.
# 
# 
#
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def check(matrix, row, col, rows, cols):
            pending = []
            if visited[row][col] != -1:
                return visited[row][col]
            if row-1 >= 0:
                if matrix[row][col] < matrix[row-1][col]:
                    if visited[row-1][col] != -1:
                        pending.append(visited[row-1][col])
                    else:
                        pending.append(check(matrix, row-1, col, rows, cols))
            if row+1 < rows:
                if matrix[row][col] < matrix[row+1][col]:
                    if visited[row+1][col] != -1:
                        pending.append(visited[row+1][col])
                    else:
                        pending.append(check(matrix, row+1, col, rows, cols))
            if col-1 >= 0:
                if matrix[row][col] < matrix[row][col-1]:
                    if visited[row][col-1] != -1:
                        pending.append(visited[row][col-1])
                    else:
                        pending.append(check(matrix, row, col-1, rows, cols))
            if col+1 < cols:
                if matrix[row][col] < matrix[row][col+1]:
                    if visited[row][col+1] != -1:
                        pending.append(visited[row][col+1])
                    else:
                        pending.append(check(matrix, row, col+1, rows, cols))
            if pending:
                visited[row][col] = max(pending)+1
                return max(pending)+1
            else:
                visited[row][col] = 1
                return 1
            
        rows = len(matrix)
        res = []
        if rows:
            cols = len(matrix[0])
        else:
            return 0
        visited = [[-1 for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if visited[row][col] == -1:
                    check(matrix, row, col, rows, cols)
        for i in range(rows):
            for j in range(cols):
                res.append(visited[i][j])
        return max(res)
    
    def longestIncreasingPath0(self, matrix: 'List[List[int]]') -> 'int':
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
            return dp[i][j]

        if not matrix or not matrix[0]: 
            return 0
        M = len(matrix)
        N = len(matrix[0])
        dp = [[0] * N for i in range(M)]
        return max(dfs(x, y) for x in range(M) for y in range(N))

