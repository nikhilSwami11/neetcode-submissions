"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        sorted_intervals = sorted(intervals, key=lambda x: x.start)

        min_heap = []

        for i in sorted_intervals:
            start = i.start
            end = i.end
            if len(min_heap)>0 and start >= min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap,end)
        return len(min_heap)


        

