class Solution:
    def combinationSum2(self, candidates, target):
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
                if t not in res:
                    res.append(t)
            else:
                for i in range(j, len(candidates)):
                    tmp.append(candidates[i])
                    backTracking(res, tmp, candidates, target-candidates[i], i+1)
                    tmp.pop()
        
        res = []
        tmp = []
        candidates.sort()
        backTracking(res, tmp, candidates, target, 0)
        return res
    
    def combinationSum20(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(idx, csum):
            record.append(None)
            b = None

            for i in range(idx+1, len(candidates)):
                if b == candidates[i]:
                    continue
                else:
                    record[-1] = b = candidates[i]
                    nsum = csum + b

                if nsum == target:
                    yield record[:]
                elif nsum > target:
                    break
                elif target - nsum >= b:
                    yield from dfs(i, nsum)

            record.pop()
 
        record = []
        candidates.sort()
        return list(dfs(-1, 0))