class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backTracking(res, tmp, candidates, target, j):
            if target < 0:
                return
            elif target == 0:
                t = tmp.copy()
                res.append(t)
            else:
                for i in range(j, len(candidates)):
                    tmp.append(candidates[i])
                    backTracking(res, tmp, candidates, target-candidates[i], i)
                    tmp.pop()
        
        res = []
        tmp = []
        candidates.sort()
        backTracking(res, tmp, candidates, target, 0)
        return res
    
    def combinationSum0(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        def dfs(remain, stack):
            if remain == 0:
                result.append(stack[:])
                return 

            for item in candidates:
                if item > remain: 
                    break
                if stack and item < stack[-1]: 
                    continue
                else:
                    dfs(remain - item, stack + [item])
            return

        dfs(target, [])
        return result
        
#         if not candidates:
#             return [[]]
#         ans = []
#         def backtrack(target, each, ans, begin):
#             if sum(each) == target:
#                 ans.append(each[:])
#                 # print(ans)
#                 return
#             for i in range(begin, len(candidates)):
#                 if sum(each) > target:
#                     continue
#                 each.append(candidates[i])
#                 backtrack(target, each, ans, i)
#                 each.pop()
#             return
#         candidates.sort()
#         backtrack(target, [], ans, 0)
#         return ans