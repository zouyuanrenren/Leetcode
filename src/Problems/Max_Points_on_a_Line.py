'''
Created on 2 Jan 2015

@author: Yuan
'''
'''
A typical hash table problem.
For each point i, one can maintain a dictionary where key = slope, val = count of points with slope to i
There are a few corner cases, one need to keep in mind:
    1. point i itself is always a line with a single point
    2. another point can be in the same position as i, they can be included in any line
    3. another point may have the same x (or y) with i, which makes slope = inf
'''
# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points) < 2:
            return len(points)
        Max = 0
        for i in range(len(points)):
            start = points[i]
            dict = {}
            starting = 1
            result = 0
            for j in range(i+1, len(points)):
                p = points[j]
                if p.x == start.x and p.y == start.y:
                    starting += 1
                else:
                    if p.y == start.y:
                        tag = "inf"
                    else:
                        tag = float(p.x-start.x)/float(p.y-start.y)
                    dict[tag] = 1 if tag not in dict else dict[tag] + 1
            result = starting
            for d in dict:
                result = max(result, dict[d]+starting)
            Max = max(Max, result)
        return Max



