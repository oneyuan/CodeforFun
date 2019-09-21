#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (35.11%)
# Likes:    1209
# Dislikes: 86
# Total Accepted:    173.3K
# Total Submissions: 477.5K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, return
# the ordering of courses you should take to finish all courses.
# 
# There may be multiple correct orders, you just need to return one of them. If
# it is impossible to finish all courses, return an empty array.
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished   
# course 0. So the correct course order is [0,1] .
# 
# Example 2:
# 
# 
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both     
# ⁠            courses 1 and 2. Both courses 1 and 2 should be taken after you
# finished course 0. 
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3] .
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 
# 
#
import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {k:[] for k in range(numCourses)}
        indegree = {}
        for dest, src in prerequisites:
            adj[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1
        queue = [k for k in range(numCourses) if k not in indegree]
        res = []
        while queue:
            vertex = queue.pop()
            res.append(vertex)
            if vertex in adj:
                for i in adj[vertex]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        queue.append(i)
        return res if len(res) == numCourses else []

    def findOrder(self, verts: int, edges: List[List[int]]) -> List[int]:
        cnt = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        for s, e in edges:
            cnt[s] += 1
            graph[e].append(s)
        
        queue = collections.deque(set(range(verts))-set(cnt))
        course = []
        while queue:
            cur = queue.popleft()
            course.append(cur)
            for child in graph[cur]:
                cnt[child] -= 1
                if cnt[child] == 0:
                    queue.append(child)
        
        return course if verts == len(course) else []

