# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda x:x.start)
        n = len(intervals)
        if n == 0:
            return []
        elif n == 1:
            return intervals
        tmp = Interval(intervals[0].start, intervals[0].end)
        i = 1
        res = []
        while i < n:
            if intervals[i].start > tmp.end:
                t = Interval(tmp.start, tmp.end)
                res.append(t)
                tmp.start = intervals[i].start
                tmp.end = intervals[i].end
            else:
                e = max(tmp.end, intervals[i].end)
                tmp.end = e
            if i == n-1:
                res.append(tmp)
            i += 1
        return res
    
    def merge0(self, intervals):
        ans = []
        if not intervals: return ans
        intervals.sort(key=lambda x:x.start)
        ans.append(intervals[0])
        for i in intervals:
            if i.start <= ans[-1].end:
                if i.end > ans[-1].end:
                    ans[-1].end = i.end
            else:
                ans.append(i)
        return ans