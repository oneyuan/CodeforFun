# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
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
    
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        return self.merge(intervals)
    

    def insert0(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        inter = []
        merged = False
        sn, en = newInterval.start, newInterval.end
        i = 0
        while i < len(intervals):
            interval = intervals[i]
            if merged:
                inter.append(interval)
                i += 1
                continue
            s, e = interval.start, interval.end
            if en < s:
                inter.append(newInterval)
                merged = True
                inter.append(interval)
                i += 1
            elif sn <= e:
                j = i
                while j < len(intervals) and intervals[j].start <= en:
                    j += 1
                interval = Interval(min(sn, s), max(intervals[j-1].end, en))
                inter.append(interval)
                merged = True
                i = j
            else:
                inter.append(interval)
                i += 1
        if not merged:
            inter.append(newInterval)
        return inter