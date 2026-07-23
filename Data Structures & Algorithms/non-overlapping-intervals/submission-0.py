class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        removed=0
        LastEnd = intervals[0][1]
        for i in range(1,len(intervals)):
            start = intervals[i][0]
            if start<LastEnd:
                removed+=1
            else:
                LastEnd=intervals[i][1]
        return removed