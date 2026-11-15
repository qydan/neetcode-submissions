"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
    
        intervals.sort(key=lambda x : x.start)
        ending_time = intervals[0].end

        for interval in intervals[1:]:
            start = interval.start
            end = interval.end

            if start >= ending_time:
                ending_time = max(ending_time, end)
            else:
                return False

        return True
