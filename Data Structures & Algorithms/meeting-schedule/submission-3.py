"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda x: x.start)
        if len(intervals) > 1:
            preEnd = intervals[0].end

        for time in intervals[1:]:
            if preEnd > time.start:
                return False
            else:
                preEnd = time.end
        return True

