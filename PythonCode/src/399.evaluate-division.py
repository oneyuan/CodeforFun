#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
# https://leetcode.com/problems/evaluate-division/description/
#
# algorithms
# Medium (47.70%)
# Likes:    1427
# Dislikes: 112
# Total Accepted:    86.8K
# Total Submissions: 180.2K
# Testcase Example:  '[["a","b"],["b","c"]]\n[2.0,3.0]\n[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
#
# Equations are given in the format A / B = k, where A and B are variables
# represented as strings, and k is a real number (floating point number). Given
# some queries, return the answers. If the answer does not exist, return -1.0.
# 
# Example:
# Given  a / b = 2.0, b / c = 3.0.
# queries are:  a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return  [6.0, 0.5, -1.0, 1.0, -1.0 ].
# 
# The input is:  vector<pair<string, string>> equations, vector<double>&
# values, vector<pair<string, string>> queries , where equations.size() ==
# values.size(), and the values are positive. This represents the equations.
# Return  vector<double>.
# 
# According to the example above:
# 
# 
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]
# ]. 
# 
# 
# 
# The input is always valid. You may assume that evaluating the queries will
# result in no division by zero and there is no contradiction.
# 
#
import collections
import itertools

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        query = collections.defaultdict(dict)
        for (num1,num2), value in zip(equations, values):
            query[num1][num2] = value
            query[num2][num1] = 1/value
            query[num1][num1] = query[num2][num2] = 1
        for k, i, j in itertools.permutations(query, 3):
            if k in query[i] and j in query[k]:
                query[i][j] = query[i][k] * query[k][j]
        return [query[v].get(c, -1.0) for v, c in queries]

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        return self.usingGraph(equations, values, queries)
    
    def usingGraph(self, equations, values, queries):
        g = collections.defaultdict(list)
        N = len(equations)
        for i in range(N):
            g[equations[i][0]].append([equations[i][1], values[i]])
            g[equations[i][1]].append([equations[i][0], 1 / values[i]])
            
        def dfs(a, b):
            if not a in g or not b in g:
                return -1.0
            if a == b:
                return 1.0
            seen.add(a)
            for c, v in g[a]:
                if not c in seen:
                    tmp = dfs(c, b)
                    if tmp == -1.0:
                        continue
                    return v * tmp
            return -1.0
        
        
        res = []
        for q in queries:
            seen = set()
            res.append(dfs(q[0], q[1]))
        return res
        

