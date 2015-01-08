'''
Created on 1 Jan 2015

@author: Yuan
'''
'''
the following solution finds:
    1. the first interval that begins no earlier than the start of the new interval
        the interval before can either be independent from the new interval, or be combined the new interval
    2. the first interval that begins no earlier than the end of the new interval
        this interval can either be independent from the new interval, or be combined with the new interval
    3. then we can combine them together
    
An alternative is to treat it as a two list merge sort problem.
One list is the intervals, the other is the [newInterval].
'''
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        newstart = -1
        newend = -1
        for i in range(0, len(intervals)):
            if intervals[i].start >= newInterval.start:
                newstart = i
                break
        if newstart == -1:
            newstart = len(intervals)
        for j in range(0, len(intervals)):
            if intervals[j].end >= newInterval.end:
                newend = j
                break
        if newend == -1:
            newend = len(intervals)
        newlist = []
        includePre = False
        includePos = False
        newBegin = newInterval.start
        newEnd = newInterval.end
        if newstart > 0:
            if intervals[newstart-1].end < newInterval.start:
                includePre = True
            else:
                newBegin = intervals[newstart-1].start
        if newend < len(intervals):
            if intervals[newend].start > newInterval.end:
                includePos = True
            else:
                newEnd = intervals[newend].end
        for index in range(0, newstart - 1):
            newlist.append(intervals[index])
        if includePre:
            newlist.append(intervals[newstart-1])
        newlist.append(Interval(newBegin, newEnd))
        if includePos:
            newlist.append(intervals[newend])
        for index in range(newend+1, len(intervals)):
            newlist.append(intervals[index])
        return newlist

starts = [5]
ends = [7,5,7,10,16]
intervals = []
for i in range(len(starts)):
    intervals.append(Interval(starts[i],ends[i]))
sol = Solution()
intervals = sol.insert(intervals, Interval(4,9))
for interval in intervals:
    print interval.start, interval.end
    
        