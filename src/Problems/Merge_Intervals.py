'''
Created on 2 Jan 2015

@author: Yuan
'''
'''
key idea is to always check the next interval before adding the current interval.
'''
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key = lambda it:it.start)
        if len(intervals) == 0:
            return []
        result = []
        current = intervals[0]
        for i in range(1, len(intervals)):
            next = intervals[i]
            if next.start <= current.end:
                if next.end > current.end:
                    current = Interval(current.start, next.end)
            else:
                result.append(current)
                current = next
        result.append(current)
        return result

input = [[1,4], [2,3]]
intervals = []
for it in input:
    intervals.append(Interval(it[0], it[1]))
for it in Solution().merge(intervals):
    print it.start, it.end
