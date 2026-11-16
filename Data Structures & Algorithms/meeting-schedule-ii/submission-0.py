"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if len(intervals) == 1: return 1
        if len(intervals) == 0: return 0

        min_room = []
        intervals.sort(key=lambda x: x.start)

        for interval in intervals:

            start = interval.start
            end = interval.end

            if min_room and min_room[0] <= start:
                heapq.heappop(min_room)
            heapq.heappush(min_room, interval.end)
            

        return len(min_room)