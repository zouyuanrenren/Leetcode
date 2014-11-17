'''
Created on 17 Nov 2014

@author: zouyuanrenren
'''
from _ctypes import pointer

'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''

'''
A deep copy copies the data instead of the pointer.
To avoid redundant copies, use a hashmap 
The basic idea is:
1. going through each node in the original list;
2. if the node has not been maintained in the hashmap, create a copy and put into the hashmap;
3. if the copy's next node has not been copied, create a copy of the original's next and put into the hashmap;
4. if the copy's random node has not been copied, reate a copy of the original's random and put into the hashmap.
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None:
            return None
        nodemap = {}
        current = head
        newhead = RandomListNode(0)
        pre = newhead
        while current != None:
            if not nodemap.has_key(current):
                nodemap[current] = RandomListNode(current.label)
            copied = nodemap[current]
            if copied.next == None and current.next != None:
                if not nodemap.has_key(current.next):
                    nodemap[current.next] = RandomListNode(current.next.label)
                copied.next = nodemap[current.next]
            if copied.random == None and current.random != None:
                if not nodemap.has_key(current.random):
                    nodemap[current.random] = RandomListNode(current.random.label)
                copied.random = nodemap[current.random]
            pre.next = copied
            pre = copied                
            current = current.next
        return newhead.next


list = [1,2,3,4,5]
head = RandomListNode(0)
tail = head
for item in list:
    tail.next = RandomListNode(item)
    tail.random = tail.next
    tail = tail.next

sol = Solution()
head = sol.copyRandomList(head.next)
while head != None:
    print head.label,
    head = head.random
print
        
