"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])
        
        i,j = 0,0
        count=0
        max=0
        while i<len(starts) and j<len(ends):
            if starts[i]<ends[j]:
                count+=1
                if count>max:
                    max=count
                i+=1
            else:
                count-=1
                j+=1

        return max