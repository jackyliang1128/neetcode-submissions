"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        
        start.sort()
        end.sort()
        n = len(intervals)

        s = 0
        e = 0
        res = 0
        currMeetings = 0
        while s < n and e < n:
            if start[s] < end[e]:
                currMeetings += 1
                s += 1
            else:
                currMeetings -= 1
                e += 1
            
            res = max(res, currMeetings)

        return res




        