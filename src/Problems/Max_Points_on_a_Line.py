'''
Created on 2 Jan 2015

@author: Yuan
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
        result = 0
        for i in range(len(points)):
            start = points[i]
            dict = {}
            starting = 1
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
            result = max(result, starting)
            for d in dict:
                result = max(result, dict[d]+starting)
        return result



