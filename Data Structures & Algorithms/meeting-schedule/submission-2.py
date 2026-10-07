"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        n = len(intervals)

        if n == 0 or n == 1:
            return True
        
        res = [intervals[0]]

        for i in range(1, n, 1):
            if intervals[i].start < res[-1].end:
                return False
            
            res.append(intervals[i])
        
        return True
